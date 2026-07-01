from engine.drawable import Drawable
from ui.color import Color
from ui.fonts import FONT_SECONDARY_MEDIUM


class DifficultySelectionLabelView(Drawable):
    def __init__(self, difficulty_selection_label, localisation_manager):
        self._difficulty_selection_label = difficulty_selection_label
        super().__init__()

        self.localisation_manager = localisation_manager

        self._text = FONT_SECONDARY_MEDIUM.render(
            self.localisation_manager.get_string("select_difficulty"), True, Color.WHITE)

    @property
    def width(self):
        return self._text.get_width()

    @property
    def height(self):
        return self._text.get_height()

    def draw(self, surface):
        surface.blit(self._text, (self.x, self.y))
