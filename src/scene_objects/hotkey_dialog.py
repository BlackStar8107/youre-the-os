from engine.modal import Modal
from scene_objects.button import Button
from scene_objects.views.hotkey_dialog_view import HotkeyDialogView


class HotkeyDialog(Modal):

    def __init__(self, localisation_manager):
        super().__init__(HotkeyDialogView(self, localisation_manager))

        self.close_button = Button(localisation_manager.get_string("close_button"), self.close)
        self.children.append(self.close_button)