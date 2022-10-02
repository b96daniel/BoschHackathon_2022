from gui import GUI
from update import *
import copy

DATASET_RELATIVE_PATH = "dataset/PSA_ADAS_W3_FC_2022-09-01_14-49_0054.MF4"

if __name__ == '__main__':
    # Load Data
    sensor_dataset, host_vehicle_dataset, adma_dataset = read_all_dataset_from_csv(DATASET_RELATIVE_PATH)

    # Initialize
    sensor_data = sensor_dataset[0]
    object_pool = ObjectPool(sensor_data.t)
    object_pool_list = []

    # Loop for estimation and prediction steps
    for i in range(len(sensor_dataset) - 1):
        update(sensor_dataset[i], object_pool)
        next_t = sensor_dataset[i + 1].t
        vehicle_data = synced_vehicle_data(i, host_vehicle_dataset)
        object_pool.predict(next_t, vehicle_data)
        object_pool.kill()
        object_pool_list.append(copy.deepcopy(object_pool))
        print(str(i) + "/" + str(len(sensor_dataset)) + " processed")

    # Initialize GUI
    try:
        gui = GUI(object_pool_list, adma_dataset, DATASET_RELATIVE_PATH)
        while True:
            gui.update()
    except KeyboardInterrupt:
        print("Script terminated")
