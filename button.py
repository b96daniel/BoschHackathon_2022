import pygame
from colors import Colors
from gui_constants import GUIConstants


class Button:
    """Button GUI element class"""
    def __init__(self, screen, text, gui_pos):
        self.screen = screen
        self.gui_pos = gui_pos
        self.font = pygame.font.SysFont("", GUIConstants.BUTTON_FONT_SIZE)
        self.text = self.font.render(text, True, Colors.WHITE)
        self.size = self.text.get_size()
        self.surface = pygame.Surface((GUIConstants.BUTTON_WIDTH, GUIConstants.BUTTON_HEIGHT))
        self.surface.fill(Colors.PRIMARY)
        self.surface.blit(self.text, (
            GUIConstants.BUTTON_WIDTH / 2 - self.size[0] / 2, GUIConstants.BUTTON_HEIGHT / 2 - self.size[1] / 2))
        self.rect = pygame.Rect(self.gui_pos[0], self.gui_pos[1], GUIConstants.BUTTON_WIDTH, GUIConstants.BUTTON_HEIGHT)

    def draw(self):

        self.screen.blit(self.surface, self.gui_pos)
        pygame.draw.rect(self.screen, Colors.LIGHTGREY, self.rect, 1)
