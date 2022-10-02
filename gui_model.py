import pygame
from colors import Colors
from gui_constants import GUIConstants
from convert import convert_real2px
from model import ObjType


class CarObject:
    """Car object"""

    def __init__(self, screen, m2px):
        super().__init__()
        self.screen = screen
        self.width = m2px * GUIConstants.CAR_LENGTH_M
        self.height = m2px * GUIConstants.CAR_WIDTH_M
        self.image = pygame.transform.scale(pygame.image.load("res/car.png"), (self.width, self.height))

    def draw(self, m2px):
        """Draws the car on the screen"""
        self.width = m2px * GUIConstants.CAR_LENGTH_M
        self.height = m2px * GUIConstants.CAR_WIDTH_M
        self.image = pygame.transform.scale(pygame.image.load("res/car.png"), (self.width, self.height))

        """Car in the coordinate system"""
        temp_top_left = convert_real2px((GUIConstants.X_POSITION_CORNER_RADAR_LEFT_REAR,
                                         GUIConstants.Y_POSITION_CORNER_RADAR_LEFT_REAR), m2px)
        rect = pygame.Rect(temp_top_left[0], temp_top_left[1], self.width, self.height)

        """Left blind spot"""
        temp_top_left = convert_real2px((GUIConstants.LEFT_BLIND_SPOT_X,
                                         GUIConstants.LEFT_BLIND_SPOT_Y), m2px)
        left_bs_rect = pygame.Rect(
            temp_top_left[0],
            temp_top_left[1],
            GUIConstants.BLIND_SPOT_WIDTH * m2px,
            GUIConstants.BLIND_SPOT_HEIGHT * m2px
        )

        """Right blind spot"""
        temp_top_left = convert_real2px((GUIConstants.RIGHT_BLIND_SPOT_X,
                                         GUIConstants.RIGHT_BLIND_SPOT_Y), m2px)
        right_bs_rect = pygame.Rect(
            temp_top_left[0],
            temp_top_left[1],
            GUIConstants.BLIND_SPOT_WIDTH * m2px,
            GUIConstants.BLIND_SPOT_HEIGHT * m2px
        )

        pygame.draw.rect(self.screen, Colors.BS_BACKGROUND, left_bs_rect)
        pygame.draw.rect(self.screen, Colors.BS_BACKGROUND, right_bs_rect)
        pygame.draw.rect(self.screen, Colors.BS_BORDER, left_bs_rect, 1)
        pygame.draw.rect(self.screen, Colors.BS_BORDER, right_bs_rect, 1)
        self.screen.blit(self.image, rect)


class DashboardObject:
    """Dashboard object"""

    def __init__(self, screen, gui_pos, width, height):
        super().__init__()
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load("res/dashboard.png"), (width, height))
        self.width = width
        self.height = height
        self.gui_pos = gui_pos
        self.rect = pygame.Rect(gui_pos[0] - width, gui_pos[1], width, height)
        self.warn_right = False
        self.warn_left = False

    def calculate_rect(self):
        """Calculates the rectangle of the object"""
        self.rect = pygame.Rect(self.gui_pos[0] - self.width, self.gui_pos[1], self.width, self.height)

    def draw(self):
        """Draws the object on the screen"""
        if self.warn_right:
            pygame.draw.rect(self.screen, (255, 0, 0),
                             pygame.Rect(self.rect.left + int(self.rect.width / 2),
                                         self.rect.top,
                                         int(self.rect.width / 2),
                                         self.rect.height)
                             )
        if self.warn_left:
            pygame.draw.rect(self.screen, Colors.RED,
                             pygame.Rect(self.rect.left,
                                         self.rect.top,
                                         int(self.rect.width / 2),
                                         self.rect.height)
                             )
        self.screen.blit(self.image, self.rect)
        pygame.draw.rect(self.screen, Colors.LIGHTGREY, self.rect, 3)


class DetectedObject:
    """Detected object"""

    def __init__(self, screen, obj, m2px):
        self.screen = screen
        self.object = obj
        self.gui_pos = convert_real2px((obj.dx, obj.dy), m2px)
        self.real_pos = (obj.dx, obj.dy)

    def draw(self):
        """Draws the object on the screen"""
        color = Colors.RED
        if self.object.type == ObjType.CAR.value:
            color = Colors.CAR_COLOR
        elif self.object.type == ObjType.TRUCK.value:
            color = Colors.TRUCK_COLOR
        elif self.object.type == ObjType.CAR_OR_TRUCK.value:
            color = Colors.CAR_OR_TRUCK_COLOR
        elif self.object.type == ObjType.BICYCLE.value:
            color = Colors.BICYCLE_COLOR
        elif self.object.type == ObjType.MOTORBIKE.value:
            color = Colors.MOTORBIKE_COLOR
        elif self.object.type == ObjType.PEDESTRIAN.value:
            color = Colors.PEDESTRIAN_COLOR
        pygame.draw.circle(self.screen, color, self.gui_pos, radius=10)

    def draw_text(self, x, y, msg):
        """Draws a message into the cell"""
        font = pygame.font.SysFont("", 30)
        img = font.render(msg, True, Colors.BLACK)
        self.screen.blit(img, self.gui_pos)
