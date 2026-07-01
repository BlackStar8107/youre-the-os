from engine.modal_view import ModalView
from ui.color import Color
from ui.fonts import FONT_PRIMARY_XXLARGE, FONT_SECONDARY_SMALL


class HotkeyDialogView(ModalView):
    def __init__(self, dialog, localisation_manager):
        self.dialog = dialog
        super().__init__()

        self.localisation_manager = localisation_manager

        self._title_text = FONT_PRIMARY_XXLARGE.render(
            self.localisation_manager.get_string("hotkey_button"), True, Color.WHITE)

        self._explanation_text = FONT_SECONDARY_SMALL.render(
            self.localisation_manager.get_string("hotkey_tip"), True, Color.WHITE)

        self._binding_keys = [
            FONT_SECONDARY_SMALL.render(self.localisation_manager.get_string("hotkey_space"), True, Color.WHITE),
            FONT_SECONDARY_SMALL.render(self.localisation_manager.get_string("hotkey_num"), True, Color.WHITE),
            FONT_SECONDARY_SMALL.render(self.localisation_manager.get_string("hotkey_zero"), True, Color.WHITE),
            FONT_SECONDARY_SMALL.render(self.localisation_manager.get_string("hotkey_shift_num"), True, Color.WHITE),
            FONT_SECONDARY_SMALL.render(self.localisation_manager.get_string("hotkey_shift_click"), True, Color.WHITE),
            FONT_SECONDARY_SMALL.render(self.localisation_manager.get_string("hotkey_s_key"), True, Color.WHITE),
        ]

        self._binding_explanations = [
            FONT_SECONDARY_SMALL.render(
                self.localisation_manager.get_string("hotkey_space_msg"),
                True,
                Color.WHITE),
            FONT_SECONDARY_SMALL.render(
                self.localisation_manager.get_string("hotkey_num_msg"),
                True,
                Color.WHITE),
            FONT_SECONDARY_SMALL.render(
                self.localisation_manager.get_string("hotkey_zero_msg"),
                True,
                Color.WHITE),
            FONT_SECONDARY_SMALL.render(
                self.localisation_manager.get_string("hotkey_shift_num_msg"),
                True,
                Color.WHITE),
            FONT_SECONDARY_SMALL.render(
                self.localisation_manager.get_string("hotkey_shift_click_msg"),
                True,
                Color.WHITE),
            FONT_SECONDARY_SMALL.render(
                self.localisation_manager.get_string("hotkey_s_key_msg"),
                True,
                Color.WHITE),
        ]

    @ModalView.x.setter
    def x(self, value):
        self._x = value
        self.dialog.close_button.view.x = self.x + (
            self.width - self.dialog.close_button.view.width) / 2

    @ModalView.y.setter
    def y(self, value):
        self._y = value
        self.dialog.close_button.view.y = (
            self.y + self.height - self.dialog.close_button.view.height - 40)

    @property
    def width(self):
        return 533

    @property
    def height(self):
        return 440

    def draw_content(self, surface):
        y = self.y + 40

        surface.blit(self._title_text, (self.x + (self.width -
                     self._title_text.get_width()) / 2, self.y + 30))

        y += self._title_text.get_height() + 20
        surface.blit(self._explanation_text, (self.x +
                     (self.width - self._explanation_text.get_width()) / 2, y))

        y += self._explanation_text.get_height() + 40
        first_key_y = y

        for binding_key in self._binding_keys:
            surface.blit(binding_key, (self.x + 20, y))
            y += binding_key.get_height() + 10

        y = first_key_y

        for binding_explanation in self._binding_explanations:
            surface.blit(binding_explanation, (self.x + 150, y))
            y += binding_explanation.get_height() + 10
