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
MATCH_VEL_TSH = 5
FULL_LIFE = 10
MAX_RANGE = 500


class Object:
    def __init__(self, object_type, dx, dy, vx, vy, ax, ay):
        self.type = object_type
        self.dx = dx
        self.dy = dy
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay
        self.life = FULL_LIFE

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
        for obj in self.list:
            if obj.is_dead() or distance(obj.dx, obj.dy, 0, 0) > MAX_RANGE:
                self.list.remove(obj)

    def predict(self, next_t, vehicle_data: VehicleData):
        """ Kinematics """
        self.delta_t = next_t - self.t
        for obj in self.list:
            obj.dx += (obj.vx * self.delta_t + vehicle_data.yaw_rate * obj.dy * self.delta_t)
            obj.dy += (obj.vy * self.delta_t - vehicle_data.yaw_rate * obj.dx * self.delta_t)
            obj.vx += obj.ax * self.delta_t
            obj.vy += obj.ay * self.delta_t
        self.t = next_t
        return 0


def distance(x1, y1, x2, y2):
    """ Euclidean Distance: """
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return d


def match(sensor, obj):
    if distance(sensor.dx, sensor.dy, obj.dx, obj.dy) < MATCH_DIST_TSH and \
            distance(sensor.vx, sensor.vy, obj.vx, obj.vy) < MATCH_VEL_TSH:
        # TODO: vel?
        return 1
    else:
        return 0


def update(sensor_data: SensorData, objects: ObjectPool):
    objects.t = sensor_data.t

    """Check camera objects"""
    for camera_obj in sensor_data.camera_data:
        matched = False
        for obj in objects.list:
            if match(camera_obj, obj):
                obj.dx = camera_obj.dx
                obj.dy = camera_obj.dy
                obj.vx = camera_obj.vx
                obj.vy = camera_obj.vy
                obj.life = FULL_LIFE
                matched = True
                break
        if not matched:
            objects.list.append(
                Object(camera_obj.type, camera_obj.dx, camera_obj.dy, camera_obj.vx, camera_obj.vy, 0, 0))

    """Check corner data objects"""
    for corner in sensor_data.corner_data:
        for corner_obj in corner:
            matched = False
            for obj in objects.list:
                if match(corner_obj, obj):
                    obj.dx = corner_obj.dx
                    obj.dy = corner_obj.dy
                    obj.vx = corner_obj.vx
                    obj.vy = corner_obj.vy
                    obj.ax = corner_obj.ax
                    obj.ay = corner_obj.ay
                    obj.life = FULL_LIFE
                    matched = True
                    break
            if not matched:
                objects.list.append(
                    Object(None, corner_obj.dx, corner_obj.dy, corner_obj.vx, corner_obj.vy,
                           corner_obj.ax, corner_obj.ay))

    # TODO: Time instead of cycle
    for obj in objects.list:
        """ Kill expired objects: """
        obj.life -= 1
        if obj.is_dead():
            objects.list.remove(obj)


def synced_vehicle_data(index, host_vehicle_dataset: list[VehicleData]):
    # TODO
    return host_vehicle_dataset[index // 2]
