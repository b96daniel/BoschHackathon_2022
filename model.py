"""

model.py

Model classes for read CSV data

"""

from enum import Enum


class ObjType(Enum):
    NONE = 0
    TRUCK = 1
    CAR = 2
    MOTORBIKE = 3
    BICYCLE = 4
    PEDESTRIAN = 5
    CAR_OR_TRUCK = 6


class CameraData:
    def __init__(self, dx, dy, vx, vy, type):
        self.dx = float(dx) / 128  # [m]
        self.dy = float(dy) / 128  # [m]
        self.vx = float(vx) / 256  # [m/s]
        self.vy = float(vy) / 256  # [m/s]
        self.type = type  # ObjType

    def __str__(self):
        return "CameraData(" + "dx=" + str(self.dx) + "; dy=" + str(self.dy) + "; vx=" + str(self.vx) + "; vy=" + str(
            self.vy) + "; type=" + str(self.type) + ")"


class CornerData:
    def __init__(self, dx, dy, vx, vy, ax, ay, prob):
        self.dx = float(dx) / 128  # [m]
        self.dy = float(dy) / 128  # [m]
        self.vx = float(vx) / 256  # [m/s]
        self.vy = float(vy) / 256  # [m/s]
        self.ax = float(ax) / 2048  # [m/s^2]
        self.ay = float(ay) / 2048  # [m/s^2]
        self.prob = float(prob) / 128

    def __str__(self):
        return "CornerData(" + "dx=" + str(self.dx) + "; dy=" + str(self.dy) + "; vx=" + str(self.vx) + "; vy=" + str(
            self.vy) \
               + "; ax=" + str(self.ax) + "; ay=" + str(self.ay) + "; prob=" + str(self.prob) + ")"


class VehicleData:
    def __init__(self, t, vx, vy, ax, ay, yaw_rate):
        self.t = float(t)
        self.vx = float(vx) / 256  # [m/s]
        self.vy = float(vy) / 256  # [m/s]
        self.ax = float(ax) / 2048  # [m/s^2]
        self.ay = float(ay) / 2048  # [m/s^2]
        self.yaw_rate = float(yaw_rate) / 16384  # [rad/s] ???

    def __str__(self):
        return "VehicleData(" + "t=" + str(self.t) + "; vx=" + str(self.vx) + "; vy=" + str(self.vy) + "; ax=" + str(
            self.ax) + "; ay=" + str(self.ay) + "; yaw=" + str(self.yaw_rate) + ")"


class SensorData:
    def __init__(self, t, camera_data, corner_data):
        self.t = float(t)
        self.camera_data = camera_data
        self.corner_data = corner_data

    def print(self):
        print(str(self.t) + "\t" + str(self.camera_data[0]) + "\t" + str(self.corner_data[0][0]))


class GpsData:
    def __init__(self, t, dx, dy, vx, vy):
        self.t = float(t)
        self.dx = float(dx)  # [m]
        self.dy = float(dy)  # [m]
        self.vx = float(vx)  # [m/s]
        self.vy = float(vy)  # [m/s]

    def __str__(self):
        return "GpsData(" + "t=" + str(self.t) + "; dx=" + str(self.dx) + "; dy=" + str(self.dy) + "; vx=" + str(
            self.vx) + "; vy=" + str(self.vy) + ")"
