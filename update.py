import math
from model import *

# Thresholds
MATCH_DIST_TSH = 0.5
MATCH_VEL_TSH = 0.5


class Object:
    def __init__(self, object_type, dx, dy, vx, vy, ax, ay):
        self.type = object_type
        self.dx = dx
        self.dy = dy
        self.vx = vx
        self.vy = vy
        self.ax = ax
        self.ay = ay


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


def update(sensor_data: SensorData, objects: list[Object]):
    for camera_obj in sensor_data.camera_data:
        for obj in objects:
            if match(camera_obj, obj):
                obj.dx = camera_obj.dx
                obj.dy = camera_obj.dy
                obj.vx = camera_obj.vx
                obj.vy = camera_obj.vy
            else:
                objects.append(
                    Object(camera_obj.type, camera_obj.dx, camera_obj.dy, camera_obj.vx, camera_obj.vy, 0, 0))

    for corner in sensor_data.corner_data:
        for corner_obj in corner:
            for obj in objects:
                if match(corner_obj, obj):
                    obj.dx = corner_obj.dx
                    obj.dy = corner_obj.dy
                    obj.vx = corner_obj.vx
                    obj.vy = corner_obj.vy
                    obj.ax = corner_obj.ax
                    obj.ay = corner_obj.ay
                else:
                    objects.append(
                        Object(corner_obj.type, corner_obj.dx, corner_obj.dy, corner_obj.vx, corner_obj.vy,
                               corner_obj.ax, corner_obj.ay))
