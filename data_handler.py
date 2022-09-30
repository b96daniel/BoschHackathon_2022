"""

data_handler.py



"""

import pandas as pd
from model import *
from column_index_macros import *


# Reads and converts given path .CSV for SensorData class list
def sensor_model_dataset_from_csv(path):
    
    # Read .CSV to pandas dataframe
    df = pd.read_csv(path)

    sensor_dataset = []

    # Iterate throw the rows of the dataframe
    for index, row in df.iterrows():
        # Create CameraData[15] list
        camera_dataset = \
        [
            CameraData(dx=row[CAM_0_DX], dy=row[CAM_0_DY], vx=row[CAM_0_VX], vy=row[CAM_0_VY], type=row[CAM_0_OBJ]),
            CameraData(dx=row[CAM_1_DX], dy=row[CAM_1_DY], vx=row[CAM_1_VX], vy=row[CAM_1_VY], type=row[CAM_1_OBJ]),
            CameraData(dx=row[CAM_2_DX], dy=row[CAM_2_DY], vx=row[CAM_2_VX], vy=row[CAM_2_VY], type=row[CAM_2_OBJ]),
            CameraData(dx=row[CAM_3_DX], dy=row[CAM_3_DY], vx=row[CAM_3_VX], vy=row[CAM_3_VY], type=row[CAM_3_OBJ]),
            CameraData(dx=row[CAM_4_DX], dy=row[CAM_4_DY], vx=row[CAM_4_VX], vy=row[CAM_4_VY], type=row[CAM_4_OBJ]),
            CameraData(dx=row[CAM_5_DX], dy=row[CAM_5_DY], vx=row[CAM_5_VX], vy=row[CAM_5_VY], type=row[CAM_5_OBJ]),
            CameraData(dx=row[CAM_6_DX], dy=row[CAM_6_DY], vx=row[CAM_6_VX], vy=row[CAM_6_VY], type=row[CAM_6_OBJ]),
            CameraData(dx=row[CAM_7_DX], dy=row[CAM_7_DY], vx=row[CAM_7_VX], vy=row[CAM_7_VY], type=row[CAM_7_OBJ]),
            CameraData(dx=row[CAM_8_DX], dy=row[CAM_8_DY], vx=row[CAM_8_VX], vy=row[CAM_8_VY], type=row[CAM_8_OBJ]),
            CameraData(dx=row[CAM_9_DX], dy=row[CAM_9_DY], vx=row[CAM_9_VX], vy=row[CAM_9_VY], type=row[CAM_9_OBJ]),
            CameraData(dx=row[CAM_10_DX], dy=row[CAM_10_DY], vx=row[CAM_10_VX], vy=row[CAM_10_VY], type=row[CAM_10_OBJ]),
            CameraData(dx=row[CAM_11_DX], dy=row[CAM_11_DY], vx=row[CAM_11_VX], vy=row[CAM_11_VY], type=row[CAM_11_OBJ]),
            CameraData(dx=row[CAM_12_DX], dy=row[CAM_12_DY], vx=row[CAM_12_VX], vy=row[CAM_12_VY], type=row[CAM_12_OBJ]),
            CameraData(dx=row[CAM_13_DX], dy=row[CAM_13_DY], vx=row[CAM_13_VX], vy=row[CAM_13_VY], type=row[CAM_13_OBJ]),
            CameraData(dx=row[CAM_14_DX], dy=row[CAM_14_DY], vx=row[CAM_14_VX], vy=row[CAM_14_VY], type=row[CAM_14_OBJ])
        ]

        # Create CornerData[4][10] 2D list
        corner_dataset = \
        [
            [
                CornerData(dx=row[RADAR_0_0_DX], dy=row[RADAR_0_0_DY], vx=row[RADAR_0_0_VX], vy=row[RADAR_0_0_VY], ax=row[RADAR_0_0_AX], ay=row[RADAR_0_0_AY], prob=row[RADAR_0_0_PROB]),
                CornerData(dx=row[RADAR_0_1_DX], dy=row[RADAR_0_1_DY], vx=row[RADAR_0_1_VX], vy=row[RADAR_0_1_VY], ax=row[RADAR_0_1_AX], ay=row[RADAR_0_1_AY], prob=row[RADAR_0_1_PROB]),
                CornerData(dx=row[RADAR_0_2_DX], dy=row[RADAR_0_2_DY], vx=row[RADAR_0_2_VX], vy=row[RADAR_0_2_VY], ax=row[RADAR_0_2_AX], ay=row[RADAR_0_2_AY], prob=row[RADAR_0_2_PROB]),
                CornerData(dx=row[RADAR_0_3_DX], dy=row[RADAR_0_3_DY], vx=row[RADAR_0_3_VX], vy=row[RADAR_0_3_VY], ax=row[RADAR_0_3_AX], ay=row[RADAR_0_3_AY], prob=row[RADAR_0_3_PROB]),
                CornerData(dx=row[RADAR_0_4_DX], dy=row[RADAR_0_4_DY], vx=row[RADAR_0_4_VX], vy=row[RADAR_0_4_VY], ax=row[RADAR_0_4_AX], ay=row[RADAR_0_4_AY], prob=row[RADAR_0_4_PROB]),
                CornerData(dx=row[RADAR_0_5_DX], dy=row[RADAR_0_5_DY], vx=row[RADAR_0_5_VX], vy=row[RADAR_0_5_VY], ax=row[RADAR_0_5_AX], ay=row[RADAR_0_5_AY], prob=row[RADAR_0_5_PROB]),
                CornerData(dx=row[RADAR_0_6_DX], dy=row[RADAR_0_6_DY], vx=row[RADAR_0_6_VX], vy=row[RADAR_0_6_VY], ax=row[RADAR_0_6_AX], ay=row[RADAR_0_6_AY], prob=row[RADAR_0_6_PROB]),
                CornerData(dx=row[RADAR_0_7_DX], dy=row[RADAR_0_7_DY], vx=row[RADAR_0_7_VX], vy=row[RADAR_0_7_VY], ax=row[RADAR_0_7_AX], ay=row[RADAR_0_7_AY], prob=row[RADAR_0_7_PROB]),
                CornerData(dx=row[RADAR_0_8_DX], dy=row[RADAR_0_8_DY], vx=row[RADAR_0_8_VX], vy=row[RADAR_0_8_VY], ax=row[RADAR_0_8_AX], ay=row[RADAR_0_8_AY], prob=row[RADAR_0_8_PROB]),
                CornerData(dx=row[RADAR_0_9_DX], dy=row[RADAR_0_9_DY], vx=row[RADAR_0_9_VX], vy=row[RADAR_0_9_VY], ax=row[RADAR_0_9_AX], ay=row[RADAR_0_9_AY], prob=row[RADAR_0_9_PROB])
            ],
            [
                CornerData(dx=row[RADAR_1_0_DX], dy=row[RADAR_1_0_DY], vx=row[RADAR_1_0_VX], vy=row[RADAR_1_0_VY], ax=row[RADAR_1_0_AX], ay=row[RADAR_1_0_AY], prob=row[RADAR_1_0_PROB]),
                CornerData(dx=row[RADAR_1_1_DX], dy=row[RADAR_1_1_DY], vx=row[RADAR_1_1_VX], vy=row[RADAR_1_1_VY], ax=row[RADAR_1_1_AX], ay=row[RADAR_1_1_AY], prob=row[RADAR_1_1_PROB]),
                CornerData(dx=row[RADAR_1_2_DX], dy=row[RADAR_1_2_DY], vx=row[RADAR_1_2_VX], vy=row[RADAR_1_2_VY], ax=row[RADAR_1_2_AX], ay=row[RADAR_1_2_AY], prob=row[RADAR_1_2_PROB]),
                CornerData(dx=row[RADAR_1_3_DX], dy=row[RADAR_1_3_DY], vx=row[RADAR_1_3_VX], vy=row[RADAR_1_3_VY], ax=row[RADAR_1_3_AX], ay=row[RADAR_1_3_AY], prob=row[RADAR_1_3_PROB]),
                CornerData(dx=row[RADAR_1_4_DX], dy=row[RADAR_1_4_DY], vx=row[RADAR_1_4_VX], vy=row[RADAR_1_4_VY], ax=row[RADAR_1_4_AX], ay=row[RADAR_1_4_AY], prob=row[RADAR_1_4_PROB]),
                CornerData(dx=row[RADAR_1_5_DX], dy=row[RADAR_1_5_DY], vx=row[RADAR_1_5_VX], vy=row[RADAR_1_5_VY], ax=row[RADAR_1_5_AX], ay=row[RADAR_1_5_AY], prob=row[RADAR_1_5_PROB]),
                CornerData(dx=row[RADAR_1_6_DX], dy=row[RADAR_1_6_DY], vx=row[RADAR_1_6_VX], vy=row[RADAR_1_6_VY], ax=row[RADAR_1_6_AX], ay=row[RADAR_1_6_AY], prob=row[RADAR_1_6_PROB]),
                CornerData(dx=row[RADAR_1_7_DX], dy=row[RADAR_1_7_DY], vx=row[RADAR_1_7_VX], vy=row[RADAR_1_7_VY], ax=row[RADAR_1_7_AX], ay=row[RADAR_1_7_AY], prob=row[RADAR_1_7_PROB]),
                CornerData(dx=row[RADAR_1_8_DX], dy=row[RADAR_1_8_DY], vx=row[RADAR_1_8_VX], vy=row[RADAR_1_8_VY], ax=row[RADAR_1_8_AX], ay=row[RADAR_1_8_AY], prob=row[RADAR_1_8_PROB]),
                CornerData(dx=row[RADAR_1_9_DX], dy=row[RADAR_1_9_DY], vx=row[RADAR_1_9_VX], vy=row[RADAR_1_9_VY], ax=row[RADAR_1_9_AX], ay=row[RADAR_1_9_AY], prob=row[RADAR_1_9_PROB])
            ],
            [
                CornerData(dx=row[RADAR_2_0_DX], dy=row[RADAR_2_0_DY], vx=row[RADAR_2_0_VX], vy=row[RADAR_2_0_VY], ax=row[RADAR_2_0_AX], ay=row[RADAR_2_0_AY], prob=row[RADAR_2_0_PROB]),
                CornerData(dx=row[RADAR_2_1_DX], dy=row[RADAR_2_1_DY], vx=row[RADAR_2_1_VX], vy=row[RADAR_2_1_VY], ax=row[RADAR_2_1_AX], ay=row[RADAR_2_1_AY], prob=row[RADAR_2_1_PROB]),
                CornerData(dx=row[RADAR_2_2_DX], dy=row[RADAR_2_2_DY], vx=row[RADAR_2_2_VX], vy=row[RADAR_2_2_VY], ax=row[RADAR_2_2_AX], ay=row[RADAR_2_2_AY], prob=row[RADAR_2_2_PROB]),
                CornerData(dx=row[RADAR_2_3_DX], dy=row[RADAR_2_3_DY], vx=row[RADAR_2_3_VX], vy=row[RADAR_2_3_VY], ax=row[RADAR_2_3_AX], ay=row[RADAR_2_3_AY], prob=row[RADAR_2_3_PROB]),
                CornerData(dx=row[RADAR_2_4_DX], dy=row[RADAR_2_4_DY], vx=row[RADAR_2_4_VX], vy=row[RADAR_2_4_VY], ax=row[RADAR_2_4_AX], ay=row[RADAR_2_4_AY], prob=row[RADAR_2_4_PROB]),
                CornerData(dx=row[RADAR_2_5_DX], dy=row[RADAR_2_5_DY], vx=row[RADAR_2_5_VX], vy=row[RADAR_2_5_VY], ax=row[RADAR_2_5_AX], ay=row[RADAR_2_5_AY], prob=row[RADAR_2_5_PROB]),
                CornerData(dx=row[RADAR_2_6_DX], dy=row[RADAR_2_6_DY], vx=row[RADAR_2_6_VX], vy=row[RADAR_2_6_VY], ax=row[RADAR_2_6_AX], ay=row[RADAR_2_6_AY], prob=row[RADAR_2_6_PROB]),
                CornerData(dx=row[RADAR_2_7_DX], dy=row[RADAR_2_7_DY], vx=row[RADAR_2_7_VX], vy=row[RADAR_2_7_VY], ax=row[RADAR_2_7_AX], ay=row[RADAR_2_7_AY], prob=row[RADAR_2_7_PROB]),
                CornerData(dx=row[RADAR_2_8_DX], dy=row[RADAR_2_8_DY], vx=row[RADAR_2_8_VX], vy=row[RADAR_2_8_VY], ax=row[RADAR_2_8_AX], ay=row[RADAR_2_8_AY], prob=row[RADAR_2_8_PROB]),
                CornerData(dx=row[RADAR_2_9_DX], dy=row[RADAR_2_9_DY], vx=row[RADAR_2_9_VX], vy=row[RADAR_2_9_VY], ax=row[RADAR_2_9_AX], ay=row[RADAR_2_9_AY], prob=row[RADAR_2_9_PROB])
            ],
            [
                CornerData(dx=row[RADAR_3_0_DX], dy=row[RADAR_3_0_DY], vx=row[RADAR_3_0_VX], vy=row[RADAR_3_0_VY], ax=row[RADAR_3_0_AX], ay=row[RADAR_3_0_AY], prob=row[RADAR_3_0_PROB]),
                CornerData(dx=row[RADAR_3_1_DX], dy=row[RADAR_3_1_DY], vx=row[RADAR_3_1_VX], vy=row[RADAR_3_1_VY], ax=row[RADAR_3_1_AX], ay=row[RADAR_3_1_AY], prob=row[RADAR_3_1_PROB]),
                CornerData(dx=row[RADAR_3_2_DX], dy=row[RADAR_3_2_DY], vx=row[RADAR_3_2_VX], vy=row[RADAR_3_2_VY], ax=row[RADAR_3_2_AX], ay=row[RADAR_3_2_AY], prob=row[RADAR_3_2_PROB]),
                CornerData(dx=row[RADAR_3_3_DX], dy=row[RADAR_3_3_DY], vx=row[RADAR_3_3_VX], vy=row[RADAR_3_3_VY], ax=row[RADAR_3_3_AX], ay=row[RADAR_3_3_AY], prob=row[RADAR_3_3_PROB]),
                CornerData(dx=row[RADAR_3_4_DX], dy=row[RADAR_3_4_DY], vx=row[RADAR_3_4_VX], vy=row[RADAR_3_4_VY], ax=row[RADAR_3_4_AX], ay=row[RADAR_3_4_AY], prob=row[RADAR_3_4_PROB]),
                CornerData(dx=row[RADAR_3_5_DX], dy=row[RADAR_3_5_DY], vx=row[RADAR_3_5_VX], vy=row[RADAR_3_5_VY], ax=row[RADAR_3_5_AX], ay=row[RADAR_3_5_AY], prob=row[RADAR_3_5_PROB]),
                CornerData(dx=row[RADAR_3_6_DX], dy=row[RADAR_3_6_DY], vx=row[RADAR_3_6_VX], vy=row[RADAR_3_6_VY], ax=row[RADAR_3_6_AX], ay=row[RADAR_3_6_AY], prob=row[RADAR_3_6_PROB]),
                CornerData(dx=row[RADAR_3_7_DX], dy=row[RADAR_3_7_DY], vx=row[RADAR_3_7_VX], vy=row[RADAR_3_7_VY], ax=row[RADAR_3_7_AX], ay=row[RADAR_3_7_AY], prob=row[RADAR_3_7_PROB]),
                CornerData(dx=row[RADAR_3_8_DX], dy=row[RADAR_3_8_DY], vx=row[RADAR_3_8_VX], vy=row[RADAR_3_8_VY], ax=row[RADAR_3_8_AX], ay=row[RADAR_3_8_AY], prob=row[RADAR_3_8_PROB]),
                CornerData(dx=row[RADAR_3_9_DX], dy=row[RADAR_3_9_DY], vx=row[RADAR_3_9_VX], vy=row[RADAR_3_9_VY], ax=row[RADAR_3_9_AX], ay=row[RADAR_3_9_AY], prob=row[RADAR_3_9_PROB])
            ]    
        ]

        #TODO:: Filter null objects

        sensor_dataset.append(SensorData(row[SENSOR_TS],camera_data=camera_dataset, corner_data=corner_dataset))        

    return sensor_dataset



# Reads and converts given path .CSV for VehicleData class list
def host_vehicle_model_dataset_from_csv(path):
    
    # Read .CSV to pandas dataframe
    df = pd.read_csv(path)

    host_vehicle_dataset = []

    # Iterate throw the rows of the dataframe
    for index, row in df.iterrows():
        host_vehicle_dataset.append(VehicleData(t=row[HOST_TS], vx=row[HOST_VX], vy=row[HOST_VY], ax=row[HOST_AX], ay=row[HOST_AY], yaw_rate=row[HOST_YAW]))
        #print(VehicleData(t=row[HOST_TS], vx=row[HOST_VX], vy=row[HOST_VY], ax=row[HOST_AX], ay=row[HOST_AY], yaw_rate=row[HOST_YAW]))

    return host_vehicle_dataset


"""
#test
sd = sensor_model_dataset_from_csv("dataset/PSA_ADAS_W3_FC_2022-09-01_14-49_0054.MF4/Group_349.csv")
sd[-1].print()

#host_vehicle_model_dataset_from_csv("dataset/PSA_ADAS_W3_FC_2022-09-01_15-17_0060.MF4/Group_416.csv")
"""