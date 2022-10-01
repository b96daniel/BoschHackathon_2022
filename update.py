import math
from model import *
from data_handler import*
#from gui import*


# Thresholds
MATCH_DIST_TSH = 0.5
MATCH_VEL_TSH = 0.5
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
        if (self.life <= 0):
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
    if (distance(sensor.dx, sensor.dy, obj.dx, obj.dy) < MATCH_DIST_TSH) \
            and (distance(sensor.vx, sensor.vy, obj.vx, obj.vy) < MATCH_VEL_TSH):
        # TODO: vel?
        return 1
    else:
        return 0


def update(sensor_data: SensorData, objects: ObjectPool):
    objects.t = sensor_data.t
    for camera_obj in sensor_data.camera_data:
        for obj in objects.list:
            if match(camera_obj, obj):
                obj.dx = camera_obj.dx
                obj.dy = camera_obj.dy
                obj.vx = camera_obj.vx
                obj.vy = camera_obj.vy
                obj.life = FULL_LIFE
            else:
                objects.list.append(
                    Object(camera_obj.type, camera_obj.dx, camera_obj.dy, camera_obj.vx, camera_obj.vy, 0, 0))

    for corner in sensor_data.corner_data:
        for corner_obj in corner:
            for obj in objects.list:
                if match(corner_obj, obj):
                    obj.dx = corner_obj.dx
                    obj.dy = corner_obj.dy
                    obj.vx = corner_obj.vx
                    obj.vy = corner_obj.vy
                    obj.ax = corner_obj.ax
                    obj.ay = corner_obj.ay
                    obj.life = FULL_LIFE
                else:
                    objects.list.append(
                        Object(corner_obj.type, corner_obj.dx, corner_obj.dy, corner_obj.vx, corner_obj.vy,
                               corner_obj.ax, corner_obj.ay))
    
    for obj in objects.list:
        """ Kill expired objects: """
        obj.life -= 1
        if obj.is_dead():
            objects.list.remove(obj)

def synced_vehicle_data(index, host_vehicle_dataset: list[VehicleData]):
    if(i > 1):
        return host_vehicle_dataset[index // 2]
    elif (i == 1):
        return host_vehicle_dataset[1]
    else:
        return 0

#Load Data
sensor_dataset = sensor_model_dataset_from_csv("dataset/PSA_ADAS_W3_FC_2022-09-01_14-49_0054.MF4/Group_349.csv")
host_vehicle_dataset = host_vehicle_model_dataset_from_csv("dataset/PSA_ADAS_W3_FC_2022-09-01_15-17_0060.MF4/Group_416.csv")

#Initialize
sensor_data = sensor_dataset[0]
object_pool = ObjectPool(sensor_data.t)
object_pool_list = []

#Loop for prediction steps
for i, sensor_date in enumerate(sensor_dataset):
    update(sensor_data, object_pool)
    next_t = sensor_dataset[i+1].t
    vehicle_data = synced_vehicle_data(i, host_vehicle_dataset)
    object_pool.predict(next_t, vehicle_data)
    object_pool.kill()
    object_pool_list.append(object_pool)


##Play on GUI
#gui = GUI()
#gui.play(object_pool_list)

