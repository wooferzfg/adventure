from manim import *
from keyboard import draw_keyboard_create, draw_qwerty_keyboard, draw_dungeon_keyboard
from adventure import AdventureGame


MAIN_FONT = 'Century Gothic'
TERMINAL_FONT = 'Consolas'


class AdventureScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.draw_scene()


class Intro(AdventureScene):
    def draw_scene(self):
        text = AdventureGame().get_current_output()
        text_element = Paragraph(text, color=BLACK, width=12, font_size=96, line_spacing=3, font=TERMINAL_FONT)
        self.play(Write(text_element, run_time=6))
        self.pause(2)
        title_element = Text("Adventure", color=BLACK, font_size=160, font=MAIN_FONT).move_to(UP * 0.8)
        self.play(FadeOut(text_element, run_time=3), GrowFromCenter(title_element, run_time=3, lag_ratio=0.03))
        subtitle_element = Text("Galactic Puzzle Hunt 2018", color=BLACK, font_size=60, font=MAIN_FONT).move_to(DOWN * 1.2)
        self.play(FadeIn(subtitle_element, run_time=2))
        self.pause(5)
        self.play(FadeOut(title_element, run_time=1), FadeOut(subtitle_element, run_time=1))


class CreateQwertyKeyboard(AdventureScene):
    def draw_scene(self):
        outlines, texts = draw_qwerty_keyboard()
        draw_keyboard_create(self, outlines, texts)


class CreateDungeonKeyboard(AdventureScene):
    def draw_scene(self):
        outlines, texts = draw_dungeon_keyboard()
        draw_keyboard_create(self, outlines, texts)
