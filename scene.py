from manim import *
from keyboard import draw_keyboard_create, draw_qwerty_keyboard, draw_dungeon_keyboard


class CreateQwertyKeyboard(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        outlines, texts = draw_qwerty_keyboard()
        draw_keyboard_create(self, outlines, texts)


class CreateDungeonKeyboard(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        outlines, texts = draw_dungeon_keyboard()
        draw_keyboard_create(self, outlines, texts)
