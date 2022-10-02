import copy
import math
from model import *
from data_handler import *

# from gui import*


# Thresholds
# MATCH_DIST_TSH = 0.5
# MATCH_VEL_TSH = 0.5
# FULL_LIFE = 10
# MAX_RANGE = 500
MATCH_DIST_TSH = 10
MATCH_VEL_TSH = 100
FULL_LIFE = 100
MAX_RANGE = 65
DEAD_RANGE = 6

ESTIMATE_VAR = 1000
MEASUREMENT_VAR = 100


class Object:
    def __init__(self, object_type, dx, dy, vx, vy, ax, ay):
        self.type = object_type
        self.dx = dx
        self.dy = dy
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.life = FULL_LIFE / 2

    def add_measurement(self, dx, dy, vx, vy, ax=None, ay=None):
        k = 0.5
        if ax is None:
            ax = self.ax
        if ay is None:
            ay = self.ay

        self.dx += k * (dx - self.dx)
        self.dy += k * (dy - self.dy)
        self.vx += k * (vx - self.vx)
        self.vy += k * (vy - self.vy)
        self.ax += k * (ax - self.ax)
        self.ay += k * (ay - self.ay)
        self.life += 5

    def is_dead(self):
        if self.life <= 0:
            return 1
        else:
            return 0


class ObjectPool:
    def __init__(self, t):
        self.list = []
        self.t = t
        self.delta_t = 0

    def kill(self):
        """ Remove irrelevant objects """
        for i, obj in enumerate(self.list.copy()):
            if (obj.is_dead() and distance(obj.dx, obj.dy, 0, 0) > DEAD_RANGE) or distance(obj.dx, obj.dy, 0,
                                                                                           0) > MAX_RANGE:
                self.list.remove(obj)

    def predict(self, next_t, vehicle_data: VehicleData):
        """ Kinematics """
        self.delta_t = next_t - self.t
        delta_fi = self.delta_t * vehicle_data.yaw_rate
        for obj in self.list:
            """ Coordinate Transformation"""
            obj.dx = obj.dx * math.cos(delta_fi) + obj.dy * math.sin(delta_fi)
            obj.dy = obj.dy * math.cos(delta_fi) - obj.dx * math.sin(delta_fi)
            obj.vx = obj.vx * math.cos(delta_fi) + obj.vy * math.sin(delta_fi)
            obj.vy = obj.vy * math.cos(delta_fi) - obj.vx * math.sin(delta_fi)
            obj.ax = obj.ax * math.cos(delta_fi) + obj.ay * math.sin(delta_fi)
            obj.ay = obj.ay * math.cos(delta_fi) - obj.ax * math.sin(delta_fi)
            """ Increments """
            obj.dx += obj.vx * self.delta_t
            obj.dy += obj.vy * self.delta_t
            obj.vx += obj.ax * self.delta_t
            obj.vy += obj.ay * self.delta_t
        self.t = next_t
        return 0


def distance(x1, y1, x2, y2):
    """ Euclidean Distance: """
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return d


def match(sensor, obj):
    if distance(sensor.dx, sensor.dy, obj.dx, obj.dy) < MATCH_DIST_TSH:
        return 1
    else:
        return 0


def update(sensor_data: SensorData, objects: ObjectPool):
    objects.t = sensor_data.t
    objects_copy = copy.deepcopy(objects.list)

    for i, obj in enumerate(objects_copy):
        for corner in sensor_data.corner_data:
            match_list = []
            for corner_obj in corner:
                if match(corner_obj, obj):
                    match_list.append(corner_obj)

            if match_list:
                min_index = 0
                min_dist = 100000
                for j, corner_data in enumerate(match_list):
                    d = distance(corner_data.dx, corner_data.dy, obj.dx, obj.dy)
                    if d < min_dist:
                        min_index = j
                        min_dist = d
                objects.list[i].add_measurement(match_list[min_index].dx,
                                                match_list[min_index].dy,
                                                match_list[min_index].vx,
                                                match_list[min_index].vy,
                                                match_list[min_index].ax,
                                                match_list[min_index].ay)
                # objects.list[i].dx = match_list[min_index].dx
                # objects.list[i].dy = match_list[min_index].dy
                # objects.list[i].vx = match_list[min_index].vx
                # objects.list[i].vy = match_list[min_index].vy
                # objects.list[i].ax = match_list[min_index].ax
                # objects.list[i].ay = match_list[min_index].ay
                # objects.list[i].life += 5

    """Check corner data objects"""
    for corner in sensor_data.corner_data:
        for corner_obj in corner:
            matched = False
            for obj in objects_copy:
                if match(corner_obj, obj):
                    matched = True
                    break
            if not matched:
                objects.list.append(
                    Object(None, corner_obj.dx, corner_obj.dy, corner_obj.vx, corner_obj.vy,
                           corner_obj.ax, corner_obj.ay))

    for i, obj in enumerate(objects_copy):
        match_list = []
        for camera_obj in sensor_data.camera_data:
            if match(camera_obj, obj):
                match_list.append(camera_obj)

        if match_list:
            min_index = 0
            min_dist = 100000
            for j, cam_data in enumerate(match_list):
                d = distance(cam_data.dx, cam_data.dy, obj.dx, obj.dy)
                if d < min_dist:
                    min_index = j
                    min_dist = d

            objects.list[i].type = match_list[min_index].type
            objects.list[i].dx = match_list[min_index].dx
            objects.list[i].dy = match_list[min_index].dy
            objects.list[i].vx = match_list[min_index].vx
            objects.list[i].vy = match_list[min_index].vy
            objects.list[i].life += 5

    """Check camera objects"""
    for camera_obj in sensor_data.camera_data:
        matched = False
        for obj in objects_copy:
            if match(camera_obj, obj):
                matched = True
                break
        if not matched:
            objects.list.append(
                Object(camera_obj.type, camera_obj.dx, camera_obj.dy, camera_obj.vx, camera_obj.vy, 0, 0))

    for obj in objects.list:
        """ Kill expired objects: """
        obj.life -= 1


def synced_vehicle_data(index, host_vehicle_dataset: list[VehicleData]):
    return host_vehicle_dataset[index // 2]
