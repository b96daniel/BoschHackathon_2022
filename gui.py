import pygame
import sys
import time
from colors import Colors
from gui_constants import GUIConstants
from button import Button
from table import Table
from gui_model import CarObject, DashboardObject, DetectedObject

import cv2

M2PX = 20

class GUI:
    def __init__(self, object_pool_list, adma_dataset):
        """Initializes the window of the application and the class variables"""
        pygame.init()
        self.obj_pools = object_pool_list
        self.m2px = M2PX

        self.front_video = cv2.VideoCapture("dataset/PSA_ADAS_W3_FC_2022-09-01_14-49_0054.avi")
        self.back_video = cv2.VideoCapture("dataset/PSA_ADAS_W3_FC_2022-09-01_14-49_0054_Rear.avi")

        """Animation variables"""
        self.current_index = 0
        self.start_time = time.time()
        self.current_timestamp = 0
        self.is_playing = True

        """ADMA variable"""
        self.adma_index = 0
        self.adma_dataset = adma_dataset

        self.screen = pygame.display.set_mode((1280, 720))
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()
        pygame.display.set_caption(GUIConstants.WINDOW_TITLE)

        # TODO: Coordinate system
        # TODO: Sensor ranges
        # TODO: Indicate the type of the object
        # TODO: Window icon
        # game_icon = pygame.image.load('res/logo.png')
        # pygame.display.set_icon(game_icon)

        """Init gui objects"""
        """Buttons"""
        self.play_btn = Button(self.screen, "Start",
                               (0 + GUIConstants.BUTTON_MARGIN, 500 + GUIConstants.BUTTON_MARGIN))
        button_height = self.play_btn.rect.height
        self.pause_btn = Button(self.screen, "Pause",
                                (0 + GUIConstants.BUTTON_MARGIN, 500 + 2 * GUIConstants.BUTTON_MARGIN + button_height))
        self.reset_btn = Button(self.screen, "Reset",
                                (0 + GUIConstants.BUTTON_MARGIN, 500 + 3 * GUIConstants.BUTTON_MARGIN
                                 + 2 * button_height))

        """Table"""
        self.data_table = Table(self.screen, (self.play_btn.rect.width + 2 * GUIConstants.BUTTON_MARGIN,
                                              500 + GUIConstants.BUTTON_MARGIN))

        """Dashboard"""
        self.dashboard = DashboardObject(self.screen,
                                         (1280 - GUIConstants.BUTTON_MARGIN,
                                          self.height - 220 + GUIConstants.BUTTON_MARGIN),
                                         1280 - 4 * GUIConstants.BUTTON_MARGIN - self.play_btn.rect.width - self.data_table.width,
                                         220 - 2 * GUIConstants.BUTTON_MARGIN)

        """Car"""
        self.car = CarObject(self.screen, M2PX)

        self.detected_objects = []
        self.adma_data = None

        self.clock = pygame.time.Clock()

    def update(self):
        """Updates the content of the window"""
        self.screen.fill(Colors.WHITE)

        """Handle the occurred events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                """Button clicks"""

                mouse_pos = pygame.mouse.get_pos()
                if self.play_btn.rect.collidepoint(mouse_pos):
                    """Start animation"""
                    if not self.is_playing:
                        self.is_playing = True
                        self.start_time = time.time() - self.current_timestamp

                if self.pause_btn.rect.collidepoint(mouse_pos):
                    """Pause animation"""
                    if self.is_playing:
                        self.is_playing = False

                if self.reset_btn.rect.collidepoint(mouse_pos):
                    """Reset the animation"""
                    self.start_time = time.time()
                    self.current_timestamp = 0
                    self.current_index = 0

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button in [4, 5]:
                """Zoom in and out of the display"""
                if event.button == 4:
                    self.m2px += 5
                    self.m2px = min(self.m2px, 100)
                elif event.button == 5:
                    self.m2px -= 5
                    self.m2px = max(self.m2px, 5)

        current_time = time.time() - self.start_time

        """Update display data"""
        if (self.current_index < len(self.obj_pools)) and current_time >= self.obj_pools[self.current_index].t \
                and self.is_playing:
            while self.current_index < len(self.obj_pools) - 1:
                if current_time < self.obj_pools[self.current_index + 1].t:
                    break
                else:
                    self.current_index += 1
            self.dashboard.warn_left = False
            self.dashboard.warn_right = False
            self.detected_objects = []
            for obj in self.obj_pools[self.current_index].list:
                self.detected_objects.append(DetectedObject(self.screen, obj, self.m2px))
                if GUIConstants.LEFT_BLIND_SPOT_X <= obj.dx <= GUIConstants.LEFT_BLIND_SPOT_X + GUIConstants.BLIND_SPOT_WIDTH:
                    if GUIConstants.LEFT_BLIND_SPOT_Y >= obj.dy >= GUIConstants.LEFT_BLIND_SPOT_Y - GUIConstants.BLIND_SPOT_HEIGHT:
                        self.dashboard.warn_left = True
                    if GUIConstants.RIGHT_BLIND_SPOT_Y >= obj.dy >= GUIConstants.RIGHT_BLIND_SPOT_Y - GUIConstants.BLIND_SPOT_HEIGHT:
                        self.dashboard.warn_right = True

            self.current_timestamp = self.obj_pools[self.current_index].t
            self.current_index += 1

        """Update adma data"""
        if (self.adma_index < len(self.adma_dataset)) and self.current_timestamp >= self.adma_dataset[self.adma_index].t \
                and self.is_playing:
            while self.adma_index < len(self.adma_dataset) - 1:
                if self.current_timestamp < self.adma_dataset[self.adma_index + 1].t:
                    break
                else:
                    self.adma_index += 1
            self.adma_data = self.adma_dataset[self.adma_index]

        self.car.draw(self.m2px)
        for detected_obj in self.detected_objects:
            detected_obj.draw()

        pygame.draw.rect(self.screen, Colors.WHITE, pygame.Rect(0, 500, 1280, 220))
        self.play_btn.draw()
        self.pause_btn.draw()
        self.reset_btn.draw()
        self.data_table.draw()
        # TODO format timestamp
        # TODO Boundaries
        self.data_table.draw_value(0, 0, self.current_timestamp)
        if self.adma_data is not None:
            self.data_table.draw_value(1, 1, self.adma_data.dx)
            self.data_table.draw_value(1, 2, self.adma_data.dy)
            self.data_table.draw_value(1, 3, self.adma_data.vx)
            self.data_table.draw_value(1, 4, self.adma_data.vy)
        self.dashboard.draw()

        self.front_video.set(cv2.CAP_PROP_POS_MSEC, self.current_timestamp * 1000)
        success, img = self.front_video.read()
        if success:
            img = img[0:250, 340:640]
            shape = img.shape[1::-1]
            self.screen.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (980, 0))

        self.back_video.set(cv2.CAP_PROP_POS_MSEC, self.current_timestamp * 1000)
        success, img = self.back_video.read()
        if success:
            img = img[0:250, 0:300]
            shape = img.shape[1::-1]
            self.screen.blit(pygame.image.frombuffer(img.tobytes(), shape, "BGR"), (980, 250 + GUIConstants.BUTTON_MARGIN // 2))

        self.clock.tick(120)
        pygame.display.update()
