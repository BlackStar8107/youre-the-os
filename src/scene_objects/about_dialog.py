from engine.modal import Modal
from scene_objects.button import Button
from scene_objects.views.about_dialog_view import AboutDialogView


class AboutDialog(Modal):

    def __init__(self, localisation_manager):
        super().__init__(AboutDialogView(self, localisation_manager))

        self.close_button = Button(localisation_manager.get_string("close_button"), self.close)
        self.children.append(self.close_button)