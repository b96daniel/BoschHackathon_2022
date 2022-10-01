class GUIConstants:
    """Window constants"""
    WINDOW_TITLE = "Object tracking"

    """Button constants"""
    BUTTON_PADDING = 5
    BUTTON_MARGIN = 10
    BUTTON_HEIGHT = 60
    BUTTON_WIDTH = 180
    BUTTON_FONT_SIZE = 30

    """Table constants"""
    TABLE_ROWS = 5
    TABLE_COLS = 3
    TABLE_FONT_SIZE = 25
    TABLE_CELL_WIDTH = 140
    TABLE_CELL_HEIGHT = 40

    """Car constants"""
    X_POSITION_CORNER_RADAR_LEFT_FRONT = 3.4738
    X_POSITION_CORNER_RADAR_LEFT_REAR = -0.7664
    X_POSITION_CORNER_RADAR_RIGHT_FRONT = 3.4738
    X_POSITION_CORNER_RADAR_RIGHT_REAR = -0.7664
    Y_POSITION_CORNER_RADAR_LEFT_FRONT = 0.6286
    Y_POSITION_CORNER_RADAR_LEFT_REAR = 0.738
    Y_POSITION_CORNER_RADAR_RIGHT_FRONT = -0.6286
    Y_POSITION_CORNER_RADAR_RIGHT_REAR = -0.738
    CAR_LENGTH_M = X_POSITION_CORNER_RADAR_RIGHT_FRONT - X_POSITION_CORNER_RADAR_RIGHT_REAR
    CAR_WIDTH_M = Y_POSITION_CORNER_RADAR_LEFT_REAR - Y_POSITION_CORNER_RADAR_RIGHT_REAR
    BLIND_SPOT_WIDTH = 2.3
    BLIND_SPOT_HEIGHT = 1.5
    LEFT_BLIND_SPOT_X = -0.3
    LEFT_BLIND_SPOT_Y = 2.3
    RIGHT_BLIND_SPOT_X = -0.3
    RIGHT_BLIND_SPOT_Y = -0.8