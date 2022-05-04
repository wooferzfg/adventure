import string

from manim import *

from adventure import AdventureGame
from keyboard import (
    DUNGEON_LETTERS,
    coordinate_for_index,
    draw_dungeon_keyboard,
    draw_key_outline,
    draw_keyboard_create,
    draw_qwerty_keyboard,
    index_for_qwerty_letter,
)
from text_animations import animate_text_update

MAIN_FONT = "Century Gothic"
TERMINAL_FONT = "Consolas"


class AdventureScene(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        self.draw_scene()


class Intro(AdventureScene):
    def draw_scene(self):
        title_element = Text("Adventure", color=BLACK, font_size=160, font=MAIN_FONT).move_to(
            UP * 0.8
        )
        self.play(Write(title_element, run_time=8))
        subtitle_element = Text(
            "Galactic Puzzle Hunt 2018", color=BLACK, font_size=60, font=MAIN_FONT
        ).move_to(DOWN * 1.2)
        self.play(FadeIn(subtitle_element, run_time=2))
        self.pause(2)
        self.play(FadeOut(title_element, run_time=1), FadeOut(subtitle_element, run_time=1))


class GameIntro(AdventureScene):
    def draw_scene(self):
        game = AdventureGame()
        intro_text = game.get_current_output()
        intro_text_element = MarkupText(
            intro_text, color=BLACK, width=12, font_size=48, line_spacing=2, font=TERMINAL_FONT
        ).move_to(UP * 1)
        self.play(Write(intro_text_element, run_time=3))
        self.pause(3)

        input_element = (
            Text("> ne", color=BLACK, font_size=36, font=TERMINAL_FONT)
            .move_to(DOWN * 2.5)
            .align_to(intro_text_element, LEFT)
        )
        self.play(FadeIn(input_element, run_time=1, lag_ratio=0.4))
        game.run_command("ne")

        input_element.generate_target()
        input_element.target.shift(UP * 4.5)
        self.play(MoveToTarget(input_element, run_time=2), FadeOut(intro_text_element))

        second_room_text = game.get_current_output()
        second_room_text_element = MarkupText(
            second_room_text,
            color=BLACK,
            width=12,
            font_size=48,
            line_spacing=2,
            font=TERMINAL_FONT,
        ).move_to(DOWN * 0.5)
        self.play(Write(second_room_text_element, run_time=2))
        self.pause(1)
        self.play(FadeOut(second_room_text_element, run_time=1), FadeOut(input_element, run_time=1))
        self.pause(1)


class DungeonRoom(AdventureScene):
    def draw_scene(self):
        letter_element = Text("G", color=RED, font_size=200, weight=BOLD, font=MAIN_FONT).move_to(
            DOWN * 2.25
        )
        self.play(FadeIn(letter_element, run_time=1))
        self.pause(0.5)

        button = ImageMobject("images/button_not_pressed.png").move_to(UP * 1.75 + RIGHT * 2.5)
        self.play(FadeIn(button, run_time=1))
        self.pause(0.5)

        blackboard = ImageMobject("images/blackboard.png").move_to(UP * 1.75 + LEFT * 2.5)
        self.play(FadeIn(blackboard, run_time=1))
        self.pause(0.5)

        monkey = ImageMobject("images/monkey.png").move_to(RIGHT * 5).align_on_border(UP, buff=0)
        self.play(FadeIn(monkey, run_time=1))
        self.pause(3)

        self.play(
            FadeOut(letter_element, run_time=1),
            FadeOut(button, run_time=1),
            FadeOut(blackboard, run_time=1),
            FadeOut(monkey, run_time=1),
        )
        self.pause(1)


class TypeSameThing(AdventureScene):
    def draw_scene(self):
        dungeon_outlines, dungeon_texts = draw_dungeon_keyboard(0, 0)
        draw_keyboard_create(self, dungeon_outlines, dungeon_texts, run_time=4)
        self.pause(2)

        keyboard_move_anims = []
        for element in dungeon_outlines + dungeon_texts:
            element.generate_target()
            element.target.shift(UP * 1.25)
            keyboard_move_anims.append(MoveToTarget(element, run_time=1.5))
        self.play(*keyboard_move_anims)

        qwerty_outlines, qwerty_texts = draw_qwerty_keyboard(0, 2.25)
        draw_keyboard_create(self, qwerty_outlines, qwerty_texts, run_time=4)
        self.pause(3)

        total_dungeon_letters = ""
        previous_top_text = None
        previous_keys = []
        time_per_letter = 0.3

        for letter in string.ascii_uppercase:
            row_index, column_index = index_for_qwerty_letter(letter)
            top_position_x, top_position_y = coordinate_for_index(row_index, column_index, 0, -1.25)
            bottom_position_x, bottom_position_y = coordinate_for_index(
                row_index, column_index, 0, 2.25
            )

            top_key = draw_key_outline(
                top_position_x, top_position_y, color=YELLOW, fill_opacity=0, stroke_width=6
            )
            bottom_key = draw_key_outline(
                bottom_position_x, bottom_position_y, color=YELLOW, fill_opacity=0, stroke_width=6
            )

            total_dungeon_letters += DUNGEON_LETTERS[row_index][column_index]
            current_top_text = (
                Text(total_dungeon_letters, color=BLACK, font_size=48, font=MAIN_FONT)
                .move_to(UP * 3.5)
                .align_on_border(LEFT, buff=1.7)
            )
            top_text_animations = animate_text_update(
                current_top_text, previous_top_text, run_time=time_per_letter
            )

            self.play(
                FadeIn(top_key, run_time=time_per_letter),
                FadeIn(bottom_key, run_time=time_per_letter),
                *map(lambda key: FadeOut(key, run_time=time_per_letter), previous_keys),
                *top_text_animations,
            )

            previous_top_text = current_top_text
            previous_keys = [top_key, bottom_key]

        self.play(*map(lambda key: FadeOut(key, run_time=time_per_letter), previous_keys))
        self.pause(1)
        self.play(
            *map(
                lambda element: FadeOut(element, run_time=1),
                dungeon_outlines
                + dungeon_texts
                + qwerty_outlines
                + qwerty_texts
                + [previous_top_text],
            ),
        )
        self.pause(1)


class AllScenes(AdventureScene):
    ALL_SCENES = [Intro, GameIntro, DungeonRoom, TypeSameThing]

    def draw_scene(self):
        for scene in self.ALL_SCENES:
            scene.draw_scene(self)
