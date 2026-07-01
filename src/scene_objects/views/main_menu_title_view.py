from os import path
import pygame

from game_info import TITLE
from engine.drawable import Drawable
from ui.fonts import FONT_PRIMARY_XXLARGE
from window_size import WINDOW_WIDTH

_icon_image = pygame.image.load(path.join('assets', 'icon.png'))


class MainMenuTitleView(Drawable):
    def __init__(self, main_menu_title, localisation_manager):
        self._main_menu_title = main_menu_title
        super().__init__()

        self.localisation_manager = localisation_manager
        
        self._icon = _icon_image

        self._text = FONT_PRIMARY_XXLARGE.render(self.localisation_manager.get_string("title"), True, (61, 154, 226))

    @property
    def width(self):
        return WINDOW_WIDTH

    @property
    def height(self):
        return self._icon.get_height() + self._text.get_height() + 20

    def draw(self, surface):
        surface.blit(self._icon, (self.x + (self.width -
                     self._icon.get_width()) / 2, self.y))
        surface.blit(self._text,
                     (self.x + (self.width - self._text.get_width()) / 2,
                      self.y + self._icon.get_height() + 20))
