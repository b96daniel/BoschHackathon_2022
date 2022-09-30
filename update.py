import math
from model import*

#Thresholds
MATCH_DIST_TSH = 0.5
MATCH_VEL_TSH = 0.5


class Object:
    def init(self, type, dx, dy, vx, vy, ax, ay):
        self.type = type
        self.dx = dx
        self.dy = dy
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay

class ObjectPool:
    def init(self):
        self.list = []

object_pool_list = []

def distance(x1, y1, x2, y2):
    """ Euclidean Distance: """
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return d

def match(sensor, object):
    if (distance(sensor.dx, sensor.dy, object.dx, object.dy) < MATCH_DIST_TSH) \
    & (distance(sensor.vx, sensor.vy, object.vx, object.vy) < MATCH_VEL_TSH):
        return 1
    else:
        return 0

def update(sensor_data: SensorData, objects: ObjectPool):
    for i, camera in enumerate(sensor_data.camera_data):
        for j, object in enumerate(objects.list):
            if match(camera, object):
                object.dx = camera.dx
                object.dy = camera.dy
                object.vx = camera.vx
                object.vy = camera.vy
            else:
                objects.list.append(Object(camera.type, camera.dx, camera.dy, camera.vx, camera.vy, 0, 0))

    for i, corners in enumerate(sensor_data.corner_data):
        for i, corner in enumerate(corners):
            for k, object in enumerate(objects.list):
                if match(corner, object):
                    object.dx = corner.dx
                    object.dy = corner.dy
                    object.vx = corner.vx
                    object.vy = corner.vy
                    object.ax = corner.ax
                    object.ay = corner.ay                                        
                else:
                    objects.list.append(Object(corner.type, corner.dx, corner.dy, corner.vx, corner.vy, corner.ax, corner.ay))
    


