'''
To render all scenes:

manim -pql scene.py -q h AllScenes
'''

from manim import *
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


class GameIntro(AdventureScene):
    def draw_scene(self):
        game = AdventureGame()
        intro_text = game.get_current_output()
        intro_text_element = MarkupText(intro_text, color=BLACK, width=12, font_size=48, line_spacing=2, font=TERMINAL_FONT).move_to(UP * 1)
        self.play(Write(intro_text_element, run_time=3))
        self.pause(3)

        input_element = Text("> ne", color=BLACK, font_size = 36, font=TERMINAL_FONT).move_to(DOWN * 2.5).align_to(intro_text_element, LEFT)
        self.play(FadeIn(input_element, run_time=1, lag_ratio=0.4))
        game.run_command("ne")

        input_element.generate_target()
        input_element.target.shift(UP * 4.5)
        self.play(MoveToTarget(input_element, run_time=2), FadeOut(intro_text_element))

        second_room_text = game.get_current_output()
        second_room_text_element = MarkupText(second_room_text, color=BLACK, width=12, font_size=48, line_spacing=2, font=TERMINAL_FONT).move_to(DOWN * 0.5)
        self.play(Write(second_room_text_element, run_time=2))
        self.pause(1)
        self.play(FadeOut(second_room_text_element, run_time=1), FadeOut(input_element, run_time=1))
        self.pause(1)


class AllScenes(AdventureScene):
    ALL_SCENES = [Intro, GameIntro]

    def draw_scene(self):
        for scene in self.ALL_SCENES:
            scene.draw_scene(self)
