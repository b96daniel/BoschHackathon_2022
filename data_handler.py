"""

data_handler.py



"""


import pandas as pd
from model import *
from column_index_macros import *

CAMERA_OBJ_MAX_SIZE = 15
RADAR_SIZE = 4
RADAR_OBJ_MAX_SIZE = 10
RADAR_PROB_OBSTACLE_THRESHOLD = 0.05


def filter_camera_data(row, obj_id, camera_dataset):
    if row[CAM_0_OBJ + obj_id] != ObjType.NONE.value:
        camera_dataset.append(CameraData(dx=row[CAM_0_DX + obj_id], dy=row[CAM_0_DY + obj_id],
                                         vx=row[CAM_0_VX + obj_id], vy=row[CAM_0_VY + obj_id], type=row[CAM_0_OBJ + obj_id]))
    return camera_dataset


def filter_radar_data(row, radar_id, obj_id, radar_dataset):
    if row[RADAR_0_0_PROB + radar_id + obj_id * RADAR_SIZE] > RADAR_PROB_OBSTACLE_THRESHOLD:
        radar_dataset.append(CornerData(
            dx=row[RADAR_0_0_DX + radar_id + obj_id * RADAR_SIZE],
            dy=row[RADAR_0_0_DY + radar_id + obj_id * RADAR_SIZE],
            vx=row[RADAR_0_0_VX + radar_id + obj_id * RADAR_SIZE],
            vy=row[RADAR_0_0_VY + radar_id + obj_id * RADAR_SIZE],
            ax=row[RADAR_0_0_AX + radar_id + obj_id * RADAR_SIZE],
            ay=row[RADAR_0_0_AY + radar_id + obj_id * RADAR_SIZE],
            prob=row[RADAR_0_0_PROB + radar_id + obj_id * RADAR_SIZE]))

    return radar_dataset



# Reads and converts given path .CSV for SensorData class list
def sensor_model_dataset_from_csv(path):

    # Read .CSV to pandas dataframe
    df = pd.read_csv(path)

    sensor_dataset = []

    # Iterate throw the rows of the dataframe
    for index, row in df.iterrows():
        # Create CameraData[max(15)] list
        camera_dataset = []

        # Filter unreal objects, only the real object's data stored
        for cam_obj_index in range(CAMERA_OBJ_MAX_SIZE):
            camera_dataset = filter_camera_data(
                row=row,
                obj_id=cam_obj_index,
                camera_dataset=camera_dataset
            )

        """
        print(str(row[HOST_TS]))
        print(len(camera_dataset))
        for camera_data in camera_dataset:
            print(camera_data)
        """

        # Create CornerData[max(4)][max(10)] 2D list
        corner_dataset = []

        # Filter for obstacles objects, only the higher probability obstace's data stored
        for radar_index in range(RADAR_SIZE):
            radar_dataset = []
            for radar_obj_index in range(RADAR_OBJ_MAX_SIZE):
                radar_dataset = filter_radar_data(
                    row=row,
                    radar_id=radar_index,
                    obj_id=radar_obj_index,
                    radar_dataset=radar_dataset
                )
            corner_dataset.append(radar_dataset)

        """
        print(str(row[HOST_TS]))
        print(len(corner_dataset))
        for radar_data in corner_dataset:
            print(len(radar_data))
            for object_data in radar_data:
                print(object_data)
        """

        sensor_dataset.append(
            SensorData(
                t=row[SENSOR_TS],
                camera_data=camera_dataset,
                corner_data=corner_dataset
            )
        )

    print("Sensor dataset finished!")
    return sensor_dataset



# Reads and converts given path .CSV for VehicleData class list
def host_vehicle_model_dataset_from_csv(path):

    # Read .CSV to pandas dataframe
    df = pd.read_csv(path)

    host_vehicle_dataset = []

    # Iterate throw the rows of the dataframe
    for index, row in df.iterrows():
        host_vehicle_dataset.append(VehicleData(
            t=row[HOST_TS], vx=row[HOST_VX], vy=row[HOST_VY], ax=row[HOST_AX], ay=row[HOST_AY], yaw_rate=row[HOST_YAW]))
        #print(VehicleData(t=row[HOST_TS], vx=row[HOST_VX], vy=row[HOST_VY], ax=row[HOST_AX], ay=row[HOST_AY], yaw_rate=row[HOST_YAW]))

    print("Host vehicle dataset finished!")
    return host_vehicle_dataset



# Reads and converts given path .CSV for GpsData class list
def gps_model_dataset_from_csv(path_340_mode, path_342_lat, path_343_long):

    # Read gps mode .CSV to pandas dataframe
    df_mode = pd.read_csv(path_340_mode)
    df_mode = df_mode.rename(columns={"t": "t_mode"})

    # Read gps long .CSV to pandas dataframe
    df_long = pd.read_csv(path_343_long)
    df_long = df_long.rename(columns={"t": "t_long"})

    # Read gps lat .CSV to pandas dataframe
    df_lat = pd.read_csv(path_342_lat)
    df_lat = df_lat.rename(columns={"t": "t_lat"})

    # Merge datasets
    df_merged = pd.concat([df_mode, df_long, df_lat], axis=1)

    gps_dataset = []


    # Iterate throw the rows of the dataframe
    for index, row in df_merged.iterrows():
        if ((row['Hunter_GPS_Mode'] == 8) or (row['Hunter_GPS_Mode'] == 9)):
            gps_dataset.append(
                GpsData(
                    t=row['t_lat'],
                    dx=row['Lat_Delta_Distance'],
                    dy=row['Long_Delta_Distance'],
                    vx=row['Lat_Delta_Velocity'],
                    vy=row['Long_Delta_Velocity']
                )
            )
    """
    for gps_data in gps_dataset:
        print(gps_data)
    
    """
    
    print("Gps dataset finished!")
    return gps_dataset



# Read all .CSV file
# The given folder has to contain the following 5 files:
# Group_340.csv, Group_342.csv, Group_343.csv, Group_349.csv, Group_416.csv
def read_all_dataset_from_csv(data_folder_path):
    # Read sensor data
    sd = sensor_model_dataset_from_csv(data_folder_path+"/Group_349.csv")
    # Read vehicle data
    vd = host_vehicle_model_dataset_from_csv(data_folder_path+"/Group_416.csv")
    # Read GPS data
    gd = gps_model_dataset_from_csv(data_folder_path+"/Group_340.csv",
                                    data_folder_path+"/Group_342.csv",
                                    data_folder_path+"/Group_343.csv")
    return sd, vd, gd



# Splits the dataset and write it out .CSV for testing
def split_dataset(data_folder_path, output_folder_path, begin_index, end_index):
    df = pd.read_csv(data_folder_path+"/Group_349.csv")
    df.iloc[begin_index:end_index].to_csv(output_folder_path+"/Group_349.csv", sep=',', index=False)
    
    df = pd.read_csv(data_folder_path+"/Group_416.csv")
    df.iloc[begin_index:end_index].to_csv(output_folder_path+"/Group_416.csv", sep=',', index=False)
    
    df = pd.read_csv(data_folder_path+"/Group_340.csv")
    df.iloc[begin_index:end_index].to_csv(output_folder_path+"/Group_340.csv", sep=',', index=False)
    
    df = pd.read_csv(data_folder_path+"/Group_342.csv")
    df.iloc[begin_index:end_index].to_csv(output_folder_path+"/Group_342.csv", sep=',', index=False)
    
    df = pd.read_csv(data_folder_path+"/Group_343.csv")
    df.iloc[begin_index:end_index].to_csv(output_folder_path+"/Group_343.csv", sep=',', index=False)
    

#read_all_dataset_from_csv("dataset/test")
#split_dataset("dataset/PSA_ADAS_W3_FC_2022-09-01_14-49_0054.MF4", "dataset/test",0, 3000)