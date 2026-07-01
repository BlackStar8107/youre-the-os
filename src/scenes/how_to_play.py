from os import path

import pygame

from ui.color import Color
from engine.scene import Scene
from scene_objects.button import Button
from scene_objects.how_to_play_part import HowToPlayPart


_parts_text = [
    "how_to_play_0_0",
    "how_to_play_1_0",
    "how_to_play_2_0",
    "how_to_play_3_0",
    "how_to_play_4_0",
    "how_to_play_5_0",
    "how_to_play_6_0",
    "how_to_play_7_0",
    "how_to_play_8_0",
    "how_to_play_9_0",
    "how_to_play_10_0",
    "how_to_play_11_0",
    "how_to_play_12_0",
    "how_to_play_13_0",
    "how_to_play_14_0"
]

_parts_images = [
    [pygame.image.load(path.join('assets', 'how_to_play_0_0.png'))],
    [pygame.image.load(path.join('assets', 'how_to_play_1_0.png'))],
    [pygame.image.load(path.join('assets', 'how_to_play_2_0.png'))],
    [
        pygame.image.load(path.join('assets', 'how_to_play_3_0.png')),
        pygame.image.load(path.join('assets', 'how_to_play_3_1.png')),
    ],
    [
        pygame.image.load(path.join('assets', 'how_to_play_4_0.png')),
        pygame.image.load(path.join('assets', 'how_to_play_4_1.png'))
    ],
    [
        pygame.image.load(path.join('assets', 'how_to_play_5_0.png')),
        pygame.image.load(path.join('assets', 'how_to_play_5_1.png')),
        pygame.image.load(path.join('assets', 'how_to_play_5_2.png')),
        pygame.image.load(path.join('assets', 'how_to_play_5_3.png')),
        pygame.image.load(path.join('assets', 'how_to_play_5_4.png')),
        pygame.image.load(path.join('assets', 'how_to_play_5_5.png'))
    ],
    [
        pygame.image.load(path.join('assets', 'how_to_play_6_0.png')),
        pygame.image.load(path.join('assets', 'how_to_play_6_1.png')),
        pygame.image.load(path.join('assets', 'how_to_play_6_2.png')),
        pygame.image.load(path.join('assets', 'how_to_play_6_3.png')),
        pygame.image.load(path.join('assets', 'how_to_play_6_4.png')),
    ],
    [
        pygame.image.load(path.join('assets', 'how_to_play_7_0.png')),
        pygame.image.load(path.join('assets', 'how_to_play_7_1.png'))
    ],
    [pygame.image.load(path.join('assets', 'how_to_play_8_0.png'))],
    [pygame.image.load(path.join('assets', 'how_to_play_9_0.png'))],
    [
        pygame.image.load(path.join('assets', 'how_to_play_10_0.png')),
        pygame.image.load(path.join('assets', 'how_to_play_10_1.png'))
    ],
    [pygame.image.load(path.join('assets', 'how_to_play_11_0.png'))],
    [
        pygame.image.load(path.join('assets', 'how_to_play_12_0.png')),
        pygame.image.load(path.join('assets', 'how_to_play_12_1.png'))
    ],
    [
        pygame.image.load(path.join('assets', 'how_to_play_13_0.png')),
        pygame.image.load(path.join('assets', 'how_to_play_13_1.png'))
    ],
    [pygame.image.load(path.join('assets', 'how_to_play_14_0.png'))],
    [pygame.image.load(path.join('assets', 'how_to_play_15_0.png'))]
]

_parts_animation_intervals = {
    6: 600,
    13: 200,
    14: 200
}

class HowToPlay(Scene):
    def __init__(self, localisation_manager):
        super().__init__('how_to_play')

        self.background_color=Color.LIGHT_GREY

        self._parts = []
        self._current_part_id = 0
        self._previous_button = None
        self._next_button = None
        self._current_time = 0

        self.localisation_manager = localisation_manager

    def setup(self):
        self._scene_objects = []

        self.process_parts()

        self._current_part_id = 0
        self._scene_objects.append(self._parts[self._current_part_id])

        self._previous_button = Button('<', self._go_to_previous_part)
        self._previous_button.view.set_xy(
            52,
            self.screen.get_height() - 78
        )
        self._scene_objects.append(self._previous_button)

        self._next_button = Button('>', self._go_to_next_part)
        self._next_button.view.set_xy(
            self.screen.get_width() - self._next_button.view.width - 52,
            self.screen.get_height() - 78
        )
        self._scene_objects.append(self._next_button)

    def _go_to_previous_part(self):
        if self._current_part_id == 0:
            self._return_to_main_menu()
        else:
            self._scene_objects.remove(self._previous_button)
            self._scene_objects.remove(self._next_button)
            self._scene_objects.remove(self._parts[self._current_part_id])

            self._current_part_id -= 1
            self._parts[self._current_part_id].initial_time = self._current_time

            self._scene_objects.append(self._parts[self._current_part_id])
            self._scene_objects.append(self._previous_button)
            self._scene_objects.append(self._next_button)

    def _go_to_next_part(self):
        if self._current_part_id == len(self._parts) - 1:
            self._return_to_main_menu()
        else:
            self._scene_objects.remove(self._previous_button)
            self._scene_objects.remove(self._next_button)
            self._scene_objects.remove(self._parts[self._current_part_id])

            self._current_part_id += 1
            self._parts[self._current_part_id].initial_time = self._current_time

            self._scene_objects.append(self._parts[self._current_part_id])
            self._scene_objects.append(self._previous_button)
            self._scene_objects.append(self._next_button)

    def _return_to_main_menu(self):
        self.scene_manager.start_scene('main_menu')

    def update(self, current_time, events):
        self._current_time = current_time
        for scene_object in list(self._scene_objects):
            scene_object.update(current_time, events)

    def process_parts(self):
        
        self._parts = []

        for i in range(len(_parts_text)-1):

            part_text = self.localisation_manager.get_string(_parts_text[i])

            if i in _parts_animation_intervals:
                self._parts.append(HowToPlayPart(
                    part_text,
                    _parts_images[i],
                    animation_interval = _parts_animation_intervals[i]
                    )
                )
            else:
                self._parts.append(HowToPlayPart(
                    self.localisation_manager.get_string(_parts_text[i]),
                    _parts_images[i]
                    )
                )