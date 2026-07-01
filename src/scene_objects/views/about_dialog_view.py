from game_info import TITLE, VERSION, COPYRIGHT_YEAR
from engine.modal_view import ModalView
from ui.color import Color
from ui.fonts import FONT_PRIMARY_XXLARGE, FONT_SECONDARY_SMALL, FONT_SECONDARY_XSMALL


class AboutDialogView(ModalView):
    def __init__(self, about_dialog, localisation_manager):
        self.about_dialog = about_dialog
        self.localisation_manager = localisation_manager
        super().__init__()

    @ModalView.x.setter
    def x(self, value):
        self._x = value
        self.about_dialog.close_button.view.x = self.x + (
            self.width - self.about_dialog.close_button.view.width) / 2

    @ModalView.y.setter
    def y(self, value):
        self._y = value
        self.about_dialog.close_button.view.y = (
            self.y + self.height - self.about_dialog.close_button.view.height - 40)

        self._title_text = FONT_PRIMARY_XXLARGE.render(
            self.localisation_manager.get_string("title"), True, Color.WHITE)
        self._version_text = FONT_SECONDARY_SMALL.render(
            self.localisation_manager.get_string("version_word") + VERSION, True, Color.WHITE)
        self._copyright_text = FONT_SECONDARY_SMALL.render(
            '© ' + COPYRIGHT_YEAR + ' Pier-Luc Brault', True, Color.WHITE)
        self._license_text = FONT_SECONDARY_XSMALL.render(
            self.localisation_manager.get_string("license"),
            True,
            Color.WHITE)
        self._license_url_text = FONT_SECONDARY_XSMALL.render(
            '<https://www.gnu.org/licenses/gpl-3.0.html>', True, Color.WHITE)
        self._asset_credits_title = FONT_SECONDARY_XSMALL.render(
            self.localisation_manager.get_string("credits_and_license"), True, Color.WHITE)
        self._asset_credits = [
            FONT_SECONDARY_XSMALL.render(
                self.localisation_manager.get_string("credit_game_icon"),
                True,
                Color.WHITE),
            FONT_SECONDARY_XSMALL.render(
                self.localisation_manager.get_string("credit_primary_font"),
                True,
                Color.WHITE),
            FONT_SECONDARY_XSMALL.render(
                self.localisation_manager.get_string("credit_secondary_font"),
                True,
                Color.WHITE),
            FONT_SECONDARY_XSMALL.render(
                self.localisation_manager.get_string("credit_emojis"),
                True,
                Color.WHITE),
            FONT_SECONDARY_XSMALL.render(
                self.localisation_manager.get_string("credit_image"),
                True,
                Color.WHITE),
        ]

    @property
    def width(self):
        return 540

    @property
    def height(self):
        return 540

    def draw_content(self, surface):
        y = self.y + 40

        surface.blit(self._title_text, (self.x + (self.width -
                     self._title_text.get_width()) / 2, self.y + 30))

        y += self._title_text.get_height() + 20
        surface.blit(self._version_text, (
            self.x + (self.width - self._version_text.get_width()) / 2,
            y
        ))

        y += self._version_text.get_height() + 20
        surface.blit(self._copyright_text, (
            self.x + (self.width - self._copyright_text.get_width()) / 2,
            y
        ))

        y += self._copyright_text.get_height() + 40
        surface.blit(self._license_text, (
            self.x + (self.width - self._license_text.get_width()) / 2,
            y
        ))

        y += self._license_text.get_height() + 10
        surface.blit(self._license_url_text, (
            self.x + (self.width - self._license_url_text.get_width()) / 2,
            y
        ))

        y += self._license_url_text.get_height() + 40
        surface.blit(self._asset_credits_title, (
            self.x + (self.width - self._asset_credits_title.get_width()) / 2,
            y
        ))

        y += self._asset_credits_title.get_height() + 10
        for text in self._asset_credits:
            surface.blit(text, (
                self.x + (self.width - text.get_width()) / 2,
                y
            ))
            y += text.get_height() + 5
