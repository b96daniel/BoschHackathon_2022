import pandas as pd


def print_349_index_defines():
    print("TIMESTAMP = 0")
    print("CAM_TS = 1")
    index = 1
    for i in range(15):
        index = index + 1
        print("CAM_" + str(i) + "_DX = " + str(index))

    for i in range(15):
        index = index + 1
        print("CAM_" + str(i) + "_DY = " + str(index))

    for i in range(15):
        index = index + 1
        print("CAM_" + str(i) + "_OBJ = " + str(index))

    for i in range(15):
        index = index + 1
        print("CAM_" + str(i) + "_VX = " + str(index))

    for i in range(15):
        index = index + 1
        print("CAM_" + str(i) + "_VY = " + str(index))

    for i in range(4):
        index = index + 1
        print("RADAR_" + str(i) + "_TS = " + str(index))

    for i in range(4):
        for j in range(10):
            index = index + 1
            print("RADAR_" + str(i) + "_" + str(j) + "_AX = " + str(index))

    for i in range(10):
        for j in range(4):
            index = index + 1
            print("RADAR_" + str(j) + "_" + str(i) + "_AY = " + str(index))

    for i in range(10):
        for j in range(4):
            index = index + 1
            print("RADAR_" + str(j) + "_" + str(i) + "_DX = " + str(index))

    for i in range(10):
        for j in range(4):
            index = index + 1
            print("RADAR_" + str(j) + "_" + str(i) + "_DY = " + str(index))

    for i in range(10):
        for j in range(4):
            index = index + 1
            print("RADAR_" + str(j) + "_" + str(i) + "_DZ = " + str(index))

    for i in range(10):
        for j in range(4):
            index = index + 1
            print("RADAR_" + str(j) + "_" + str(i) + "_PROB = " + str(index))

    for i in range(10):
        for j in range(4):
            index = index + 1
            print("RADAR_" + str(j) + "_" + str(i) + "_VX = " + str(index))

    for i in range(10):
        for j in range(4):
            index = index + 1
            print("RADAR_" + str(j) + "_" + str(i) + "_VY = " + str(index))

    print("CAM_POSX = 401")
    print("CAM_POSY = 402")
    print("CAM_POSZ = 403")
    return


def print_416_index_defines():
    df = pd.read_csv("dataset/PSA_ADAS_W3_FC_2022-09-01_15-17_0060.MF4/Group_416.csv")

    for col in df.columns:
        print(col)
