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
        title_element = Text("Adventure", color=BLACK, font_size=160, font=MAIN_FONT).move_to(UP * 0.8)
        self.play(Write(title_element, run_time=8))
        subtitle_element = Text("Galactic Puzzle Hunt 2018", color=BLACK, font_size=60, font=MAIN_FONT).move_to(DOWN * 1.2)
        self.play(FadeIn(subtitle_element, run_time=2))
        self.pause(2)
        self.play(FadeOut(title_element, run_time=1), FadeOut(subtitle_element, run_time=1))

        game = AdventureGame()
        intro_text = game.get_current_output()
        intro_text_element = Paragraph(intro_text, color=BLACK, width=12, font_size=96, line_spacing=2, font=TERMINAL_FONT).move_to(UP * 1)
        self.play(Write(intro_text_element, run_time=3))
        self.pause(3)

        input_element = Text("> ne", color=BLACK, font_size = 36, font=TERMINAL_FONT).move_to(DOWN * 2).align_to(intro_text_element, LEFT)
        self.play(FadeIn(input_element, run_time=1, lag_ratio=0.4))
        game.run_command("ne")

        input_element.generate_target()
        input_element.target.shift(UP * 4)
        self.play(MoveToTarget(input_element, run_time=2), FadeOut(intro_text_element))

        second_room_text = game.get_current_output()
        second_room_text_element = Paragraph(second_room_text, color=BLACK, width=12, font_size=96, line_spacing=2, font=TERMINAL_FONT).move_to(DOWN * 0.5)
        self.play(Write(second_room_text_element, run_time=3))
        self.pause(1)
        self.play(FadeOut(second_room_text_element, run_time=1), FadeOut(input_element, run_time=1))
        self.pause(1)

class CreateQwertyKeyboard(AdventureScene):
    def draw_scene(self):
        outlines, texts = draw_qwerty_keyboard()
        draw_keyboard_create(self, outlines, texts)


class CreateDungeonKeyboard(AdventureScene):
    def draw_scene(self):
        outlines, texts = draw_dungeon_keyboard()
        draw_keyboard_create(self, outlines, texts)
