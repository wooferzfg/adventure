import string

from manim import *

from adventure import AdventureGame
from fonts import MAIN_FONT, TERMINAL_FONT
from keyboard import (
    DUNGEON_COLOR,
    DUNGEON_LETTERS,
    INDEX_FOR_QWERTY_LETTER,
    QWERTY_COLOR,
    animate_blackboard_arrow_move,
    animate_keyboard_create,
    animate_keyboard_outlines,
    animate_keyboard_texts,
    draw_blackboard_arrow,
    draw_blackboard_text,
    draw_blackboard_with_letter,
    draw_dungeon_keyboard,
    draw_key_outline,
    draw_qwerty_keyboard,
    init_keyboard_status,
    position_for_index,
    process_events,
    split_text,
)
from text_animations import animate_text_add_letters, animate_text_remove_letters

STEP_1_TEXT = "awrwwnwpepseapnwwawwwpneppepseeeneneeapswwwwwaseepnwnwwwwpppppepseewwwwwwapseeaseepnwnwwwwwppeepseewapseeeaseepnwnwwwwwpppeepseewapseeeeaseepnwnwwwwwppppeepseeswapeeeeanwwwwppppeepseeeapeeeanwwwwpppeepseeeee"
STEP_2_TEXT = "wwwwrnwwwwrnwwrnwwwwrnwwwwrseernwwwwrneeeeernwwwrneeeeerwwwrnwwwrwwwwrneeeeerseernwwwwrnwwwwrwwwwrnwwwwrnwwwwrnwwwwrneeeeerseernwwwrneeeeerneeeeernwwwrneeeeerwwwrnwwwrnwwwrnwwwrseernwwwrseernwwwrnwwwrwwwwrneeeeerwwwrnwwwwrnwwwwrnwwwwrnwwwwrnwwwwrwwwwrwwwrnwwwrnwwwrneeeeerseernwwwwrseernwwwwrnwwwwrnwwwwrnwwwwrneeeeerneeeeerneeeeerneeeeerneeeeernwwwrneeeeerwwwrnwwwrnwwwrnwwwwrnwwwwrnwwwwrnwwwwrnwwwwrnwwwwrwwwwrneeeeerwwwrnwwwrnwwwrwwwwrwwwrnwwwrnwwwrneeeeerseernwwwwrseernwwwwrnwwwwrnwwwwrnwwwwrnwwwwrneeeeerneeeeernwwwrnwwwrneeeeerwwwrnwwwrnwwwrnwwwwrwwwwrneeeeerwwwrnwwwrnwwwrnwwwrwwwwrwwwrnwwwrnwwwrneeeeerseernwwwwrseernwwwwrnwwwwrnwwwwrnwwwwrnwwwwrneeeeerneeeeerneeeeernwwwrnwwwrneeeeerwwwrnwwwrnwwwrnwwwwrwwwwrneeeeerwwwrnwwwrnwwwrnwwwrnwwwrwwwwrwwwrnwwwrnwwwrneeeeerseernwwwwrseernwwwwrnwwwwrnwwwwrnwwwwrnwwwwrneeeeerneeeeerneeeeerneeeeernwwwrnwwwrneeeeerwwwrnwwwrnwwwrwwwrnwwwwrwwwwrneeeeernwwwrnwwwrnwwwrnwwwrwwwwrseernwwwwrnwwwwrnwwwwrnwwwwrneeeeerneeeeerneeeeerneeeeernwwwrnwwwrneeeeerwwwrnwwwrnwwwrnwwwrwwwwrneeeeernwwwrnwwwrnwwwrwwwwrseernwwwwrnwwwwrnwwwwrnwwwwrneeeeerneeeeerneeeeernwwwrnwwwrneeeeerwwwrnwwwrnwwwrnwwwrnwwwrnwwwr"
STEP_3_GAME_TEXT = STEP_2_TEXT.upper()
G_BLACKBOARD_TEXT = "nw w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e w w w p ne p p e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w p p p p p e p se e nw w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e nw w w w p p p p e e p se e se e p nw nw w w w p p p p p e p se e w w w p ne p p e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e nw w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w p p p p p e p se e w w w p ne p p e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w p p p p p e p se e nw w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e w w w p ne p p e p se e se e p nw nw w w w w p p p e e p se e w w w p ne p p e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e nw w w w p p p p e e p se e se e p nw nw w w w p p p p p e p se e nw w w w p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e nw w w w p p p p e e p se e nw w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w p p p p p e p se e w w w p ne p p e p se e se e p nw nw w w w w p p p p e e p se e w w w p ne p p e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w p p p p p e p se e nw w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e nw w w w p p p p e e p se e se e p nw nw w w w p p p p p e p se e nw w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e nw w w w p p p p e e p se e nw w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w p p p p p e p se e w w w p ne p p e p se e se e p nw nw w w w w p p p p e e p se e w w w p ne p p e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w p p p p p e p se e nw w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p p e e p se e nw w w w p p p p e e p se e se e p nw nw w w w p p p p p e p se e nw w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e nw w w w p p p p e e p se e nw w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w p p p p p e p se e w w w p ne p p e p se e se e p nw nw w w w w p p p p e e p se e w w w p ne p p e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w p p p p p e p se e nw w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p p e e p se e nw w w w p p p p e e p se e se e p nw nw w w w p p p p p e p se e nw w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e nw w w w p p p p e e p se e nw w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w p p p p p e p se e w w w p ne p p e p se e se e p nw nw w w w w p p p p e e p se e w w w p ne p p e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w p p p p p e p se e nw w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e nw w w w p p p e e p se e se e p nw nw w w w w p p p p e e p se e nw w w w p p p p e e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e nw w w w p p p p e e p se e w w w p ne p p e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w p p p p p e p se e nw w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e nw w w w p p p p e e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e nw w w w p p p p e e p se e w w w p ne p p e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w w p p p p e e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w p p p p p e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w p p p p p e p se e nw w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e se e p nw nw w w w w p p p e e p se e"


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
        self.play(FadeOut(title_element, subtitle_element, run_time=1))


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
        self.play(FadeOut(second_room_text_element, input_element, run_time=1))
        self.pause(1)


class DungeonRoom(AdventureScene):
    def draw_scene(self):
        letter_element = Text(
            "G", color=DUNGEON_COLOR, font_size=200, weight=BOLD, font=MAIN_FONT
        ).move_to(DOWN * 2.25)
        self.play(FadeIn(letter_element, run_time=1))
        self.pause(0.5)

        button = ImageMobject("images/button_not_pressed.png").move_to(UP * 1.75 + RIGHT * 2.5)
        self.play(FadeIn(button, run_time=1))
        self.pause(0.5)

        blackboard = ImageMobject("images/blackboard.png").move_to(UP * 1.75 + LEFT * 2.5)
        self.play(FadeIn(blackboard, run_time=1))
        self.pause(0.5)

        monkey = ImageMobject("images/monkey.png").move_to(RIGHT * 5 + UP * 5.2)
        monkey.generate_target()
        monkey.target.align_on_border(UP, buff=-0.1)
        self.add(monkey)
        self.play(MoveToTarget(monkey, run_time=1))

        pivot = 4 * UP + RIGHT * 5.5
        self.play(
            Rotate(
                monkey,
                PI / 12,
                about_point=pivot,
                run_time=0.75,
                rate_func=rate_functions.ease_in_out_sine,
            )
        )
        self.play(
            Rotate(
                monkey,
                -PI / 6,
                about_point=pivot,
                run_time=1.5,
                rate_func=rate_functions.ease_in_out_sine,
            )
        )
        self.play(
            Rotate(
                monkey,
                PI / 12,
                about_point=pivot,
                run_time=0.75,
                rate_func=rate_functions.ease_in_out_sine,
            )
        )

        self.play(
            FadeOut(letter_element, button, blackboard, monkey, run_time=1),
        )
        self.pause(1)


class TypeSameThing(AdventureScene):
    def draw_scene(self):
        dungeon_outlines, dungeon_texts = draw_dungeon_keyboard(0, 0)
        self.play(*animate_keyboard_create(dungeon_outlines, dungeon_texts, run_time=4))
        self.pause(2)

        keyboard_move_anims = []
        for element in dungeon_outlines + dungeon_texts:
            element.generate_target()
            element.target.shift(UP * 1.25)
            keyboard_move_anims.append(MoveToTarget(element, run_time=1.5))
        self.play(*keyboard_move_anims)

        qwerty_outlines, qwerty_texts = draw_qwerty_keyboard(0, 2.25)
        self.play(*animate_keyboard_create(qwerty_outlines, qwerty_texts, run_time=4))
        self.pause(3)

        total_dungeon_letters = ""
        previous_top_text = None
        previous_keys = []
        time_per_letter = 0.3

        for letter in string.ascii_uppercase:
            row_index, column_index = INDEX_FOR_QWERTY_LETTER[letter]
            top_position = position_for_index(row_index, column_index, 0, -1.25)
            bottom_position = position_for_index(row_index, column_index, 0, 2.25)

            top_key = draw_key_outline(top_position, color=YELLOW, fill_opacity=0, stroke_width=6)
            bottom_key = draw_key_outline(
                bottom_position, color=YELLOW, fill_opacity=0, stroke_width=6
            )

            total_dungeon_letters += DUNGEON_LETTERS[row_index][column_index]
            current_top_text = (
                Text(total_dungeon_letters, color=BLACK, font_size=48, font=MAIN_FONT)
                .move_to(UP * 3.5)
                .align_on_border(LEFT, buff=1.7)
            )
            top_text_animations = animate_text_add_letters(
                current_top_text, previous_top_text, run_time=time_per_letter
            )

            self.play(
                FadeIn(top_key, bottom_key, run_time=time_per_letter),
                *(FadeOut(key, run_time=time_per_letter) for key in previous_keys),
                *top_text_animations,
            )

            previous_top_text = current_top_text
            previous_keys = [top_key, bottom_key]

        self.play(FadeOut(*previous_keys, run_time=time_per_letter))
        self.pause(1)

        both_keyboards_text = (
            Text("BOTHKEYBOARDS", color=BLACK, font_size=48, font=MAIN_FONT)
            .move_to(UP * 3.5)
            .align_on_border(RIGHT, buff=1.694)
        )
        both_keyboards_animations = animate_text_remove_letters(
            both_keyboards_text, previous_top_text, run_time=2
        )

        self.play(
            FadeOut(
                *(dungeon_outlines + dungeon_texts + qwerty_outlines + qwerty_texts), run_time=2
            ),
            *both_keyboards_animations,
        )

        both_keyboards_text.generate_target()
        both_keyboards_text.target.move_to(UP * 3.5)
        self.play(MoveToTarget(both_keyboards_text, run_time=2))

        real_keyboard_example = Text(
            "> ne w w e se sw nw p e ne nw sw", color=BLACK, font_size=36, font=TERMINAL_FONT
        ).move_to(UP * 1.25)
        self.play(FadeIn(real_keyboard_example, run_time=5, lag_ratio=0.4))

        real_keyboard_text = Text(
            "Real Keyboard:", color=BLACK, font_size=48, font=MAIN_FONT
        ).move_to(UP * 2)
        self.play(Write(real_keyboard_text, run_time=1))
        self.pause(2)

        self.play(*animate_keyboard_outlines(qwerty_outlines, run_time=3))

        game_keyboard_text = Text(
            "Game Keyboard:", color=BLACK, font_size=48, font=MAIN_FONT
        ).move_to(DOWN * 0.25)
        self.play(Write(game_keyboard_text, run_time=1))

        self.play(*animate_keyboard_texts(qwerty_texts, run_time=6))
        self.pause(2)

        self.play(
            FadeOut(
                *(
                    qwerty_outlines
                    + qwerty_texts
                    + [
                        both_keyboards_text,
                        game_keyboard_text,
                        real_keyboard_example,
                        real_keyboard_text,
                    ]
                ),
                run_time=1,
            )
        )
        self.pause(1)


class GameKeyboardType(AdventureScene):
    def draw_scene(self):
        letter_element = Text(
            "S", color=QWERTY_COLOR, font_size=200, weight=BOLD, font=MAIN_FONT
        ).move_to(DOWN * 1.75)
        button_not_pressed = ImageMobject("images/button_not_pressed.png", z_index=1).move_to(
            UP * 1
        )
        self.play(FadeIn(letter_element, button_not_pressed, run_time=2))

        button_pressed = ImageMobject("images/button_pressed.png").move_to(UP * 1)
        self.add(button_pressed)

        self.pause(4)
        p_command = Text("> p", color=BLACK, font_size=36, font=TERMINAL_FONT).move_to(UP * 2.25)
        self.play(FadeIn(p_command, run_time=0.5, lag_ratio=0.4))

        self.play(FadeOut(button_not_pressed, run_time=1))
        self.pause(0.5)
        self.play(
            FadeOut(p_command, button_pressed, letter_element, run_time=1),
        )
        self.pause(1)


class GoalOfPuzzle(AdventureScene):
    def draw_scene(self):
        real_keyboard_header = (
            Text("Letters Typed on Real Keyboard:", color=BLACK, font_size=32, font=MAIN_FONT)
            .move_to(UP * 2)
            .align_on_border(LEFT, buff=3.4)
        )
        game_keyboard_header = (
            Text("Letters Typed on Game Keyboard:", color=BLACK, font_size=32, font=MAIN_FONT)
            .move_to(DOWN * 1)
            .align_on_border(LEFT, buff=3.4)
        )

        self.play(Write(real_keyboard_header, run_time=1), Write(game_keyboard_header, run_time=1))

        previous_real_text = None
        previous_game_text = None
        real_letters = ""
        game_letters = ""

        time_per_letter = 0.2
        events = [
            ("real", "e"),
            ("real", "w"),
            ("real", "s"),
            ("game", "E"),
            ("real", "w"),
            ("game", "W"),
            ("real", "p"),
            ("real", "n"),
            ("game", "S"),
            ("real", "e"),
            ("game", "W"),
            ("game", "P"),
            ("real", "e"),
            ("game", "N"),
            ("real", "n"),
            ("real", "w"),
            ("game", "E"),
            ("game", "E"),
            ("real", "a"),
            ("game", "N"),
            ("real", "p"),
            ("game", "W"),
            ("real", "r"),
            ("game", "A"),
            ("real", "e"),
            ("game", "P"),
            ("game", "R"),
            ("real", "r"),
            ("game", "E"),
            ("game", "R"),
        ]

        for keyboard_type, letter in events:
            if keyboard_type == "real":
                real_letters += letter
                new_real_text = (
                    Text(real_letters, color=BLACK, font_size=60, font=TERMINAL_FONT)
                    .align_to(real_keyboard_header, UP)
                    .shift(DOWN * 1)
                    .align_on_border(LEFT, buff=3.4)
                )
                self.play(
                    *animate_text_add_letters(
                        new_real_text, previous_real_text, run_time=time_per_letter
                    )
                )
                previous_real_text = new_real_text
            elif keyboard_type == "game":
                game_letters += letter
                new_game_text = (
                    Text(
                        game_letters, color=QWERTY_COLOR, font_size=50, font=MAIN_FONT, weight=BOLD
                    )
                    .move_to(DOWN * 1.95)
                    .align_on_border(LEFT, buff=3.4)
                )
                self.play(
                    *animate_text_add_letters(
                        new_game_text, previous_game_text, run_time=time_per_letter
                    )
                )
                previous_game_text = new_game_text

        self.pause(0.5)
        self.play(
            FadeOut(
                real_keyboard_header,
                game_keyboard_header,
                previous_real_text,
                previous_game_text,
                run_time=1,
            ),
        )
        self.pause(1)


class NavigatingPressingButtons(AdventureScene):
    def draw_scene(self):
        keyboard_status = init_keyboard_status(self)
        time_per_letter = 0.7

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "create_keyboard",
                    "run_time": 2,
                },
                {
                    "type": "create_letters_typed_headers",
                    "run_time": 2,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "create_position_circle",
                    "letter": "H",
                    "run_time": 1,
                }
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "move",
                    "letter": "Y",
                    "run_time": time_per_letter,
                },
                {
                    "type": "real_text",
                    "letters": "nw",
                    "run_time": time_per_letter,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "move",
                    "letter": "G",
                    "run_time": time_per_letter,
                },
                {
                    "type": "real_text",
                    "letters": "sw",
                    "run_time": time_per_letter,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "move",
                    "letter": "B",
                    "run_time": time_per_letter,
                },
                {
                    "type": "real_text",
                    "letters": "se",
                    "run_time": time_per_letter,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "move",
                    "letter": "N",
                    "run_time": time_per_letter,
                },
                {
                    "type": "real_text",
                    "letters": "e",
                    "run_time": time_per_letter,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "button_press",
                    "letter": "N",
                    "run_time": time_per_letter * 3,
                },
                {
                    "type": "real_text",
                    "letters": "p",
                    "run_time": time_per_letter,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "move",
                    "letter": "B",
                    "run_time": time_per_letter,
                },
                {
                    "type": "real_text",
                    "letters": "w",
                    "run_time": time_per_letter,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "move",
                    "letter": "V",
                    "run_time": time_per_letter,
                },
                {
                    "type": "real_text",
                    "letters": "w",
                    "run_time": time_per_letter,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "move",
                    "letter": "C",
                    "run_time": time_per_letter,
                },
                {
                    "type": "real_text",
                    "letters": "w",
                    "run_time": time_per_letter,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "move",
                    "letter": "X",
                    "run_time": time_per_letter,
                },
                {
                    "type": "real_text",
                    "letters": "w",
                    "run_time": time_per_letter,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "move",
                    "letter": "S",
                    "run_time": time_per_letter,
                },
                {
                    "type": "real_text",
                    "letters": "nw",
                    "run_time": time_per_letter,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "move",
                    "letter": "W",
                    "run_time": time_per_letter,
                },
                {
                    "type": "real_text",
                    "letters": "nw",
                    "run_time": time_per_letter,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "button_press",
                    "letter": "W",
                    "run_time": time_per_letter * 3,
                },
                {
                    "type": "real_text",
                    "letters": "p",
                    "run_time": time_per_letter,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "move",
                    "letter": "S",
                    "run_time": time_per_letter,
                },
                {
                    "type": "real_text",
                    "letters": "se",
                    "run_time": time_per_letter,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "button_press",
                    "letter": "S",
                    "run_time": time_per_letter * 3,
                },
                {
                    "type": "real_text",
                    "letters": "p",
                    "run_time": time_per_letter,
                },
            ],
        )

        self.pause(1)

        process_events(
            keyboard_status,
            [
                {
                    "type": "fade_out_keyboard",
                    "run_time": 1,
                },
                {
                    "type": "fade_out_logs",
                    "run_time": 1,
                },
            ],
        )

        self.pause(1)


class Blackboards(AdventureScene):
    def draw_scene(self):
        blackboard = ImageMobject("images/blackboard.png")
        self.play(FadeIn(blackboard, run_time=2))
        self.pause(3)

        a_command = Text("> a w nw sw e p", color=BLACK, font_size=36, font=TERMINAL_FONT).move_to(
            UP * 2.5
        )
        self.play(FadeIn(a_command, run_time=1.5, lag_ratio=0.4))
        self.pause(1)

        blackboard_text = Text("w nw sw e p", color=WHITE, font_size=36, font=TERMINAL_FONT)
        self.play(Write(blackboard_text, run_time=1.5))
        self.play(FadeOut(a_command, run_time=1))

        r_command = Text("> r", color=BLACK, font_size=36, font=TERMINAL_FONT).move_to(UP * 2.5)
        self.play(FadeIn(r_command, run_time=0.5, lag_ratio=0.4))
        self.pause(3)

        arrow = draw_blackboard_arrow(LEFT * 1.24)
        self.play(FadeIn(arrow, run_time=1.5))

        self.play(animate_blackboard_arrow_move(arrow, LEFT * 0.6, run_time=1))
        self.play(animate_blackboard_arrow_move(arrow, RIGHT * 0.15, run_time=1))
        self.play(animate_blackboard_arrow_move(arrow, RIGHT * 0.77, run_time=1))
        self.play(animate_blackboard_arrow_move(arrow, RIGHT * 1.25, run_time=1))

        self.play(FadeOut(r_command, arrow, run_time=1))
        self.play(FadeOut(blackboard, blackboard_text, run_time=1))
        self.pause(1)


class BlackboardExample(AdventureScene):
    def draw_scene(self):
        keyboard_status = init_keyboard_status(self)

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "create_keyboard",
                    "run_time": 2,
                },
                {
                    "type": "create_letters_typed_headers",
                    "run_time": 2,
                },
                {
                    "type": "create_position_circle",
                    "letter": "H",
                    "run_time": 2,
                },
            ],
        )
        self.pause(1)

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "real_text",
                    "letters": "a",
                    "run_time": 0.7,
                },
            ],
        )
        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "real_text",
                    "letters": "w",
                    "run_time": 0.7,
                },
            ],
        )
        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "real_text",
                    "letters": "p",
                    "run_time": 0.7,
                },
            ],
        )
        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "real_text",
                    "letters": "p",
                    "run_time": 0.7,
                },
            ],
        )
        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "real_text",
                    "letters": "p",
                    "run_time": 0.7,
                },
            ],
        )
        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "real_text",
                    "letters": "e",
                    "run_time": 0.7,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "create_blackboard",
                    "letter": "H",
                    "run_time": 2,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_text",
                    "text": "w p p p e",
                    "transition": "write",
                    "run_time": 1,
                },
            ],
        )

        self.pause(3)

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "real_text",
                    "letters": "r",
                    "run_time": 2,
                },
            ],
        )
        self.pause(3)

        keyboard_status = BlackboardExample.animate_blackboard_read(self, keyboard_status, 0.9)
        self.pause(3)

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "real_text",
                    "letters": "r",
                    "run_time": 0.3,
                },
            ],
        )
        keyboard_status = BlackboardExample.animate_blackboard_read(self, keyboard_status, 0.3)

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "real_text",
                    "letters": "r",
                    "run_time": 0.3,
                },
            ],
        )
        keyboard_status = BlackboardExample.animate_blackboard_read(self, keyboard_status, 0.3)
        self.pause(1)

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "fade_out_blackboard",
                    "run_time": 1,
                },
                {
                    "type": "fade_out_keyboard",
                    "run_time": 1,
                },
                {
                    "type": "fade_out_logs",
                    "run_time": 1,
                },
            ],
        )

        self.pause(1)

    def animate_blackboard_read(self, keyboard_status, time_per_step):
        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": LEFT * 0.99,
                    "run_time": time_per_step,
                },
                {
                    "type": "move",
                    "letter": "G",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": LEFT * 0.48,
                    "run_time": time_per_step,
                },
                {
                    "type": "button_press",
                    "letter": "G",
                    "run_time": time_per_step * 3,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": RIGHT * 0.02,
                    "run_time": time_per_step,
                },
                {
                    "type": "button_press",
                    "letter": "G",
                    "run_time": time_per_step * 3,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": RIGHT * 0.52,
                    "run_time": time_per_step,
                },
                {
                    "type": "button_press",
                    "letter": "G",
                    "run_time": time_per_step * 3,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": RIGHT * 1.02,
                    "run_time": time_per_step,
                },
                {
                    "type": "move",
                    "letter": "H",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "fade_out_blackboard_arrow",
                    "run_time": time_per_step,
                },
            ],
        )

        return keyboard_status


class NineBlackboards(AdventureScene):
    def draw_scene(self):
        outlines, texts = draw_qwerty_keyboard(0, 0.6)
        self.play(*animate_keyboard_create(outlines, texts, run_time=2))

        blackboards_used_text = Text(
            "Blackboards Used in Solution", color=BLACK, font=MAIN_FONT, font_size=48
        ).move_to(UP * 1.8)
        blackboard_outlines = NineBlackboards.draw_outlines(
            ["A", "E", "N", "P", "R", "S", "W", "G", "H"]
        )
        self.play(
            Write(blackboards_used_text, run_time=2),
            FadeIn(*blackboard_outlines, run_time=2),
        )
        self.pause(1)
        self.play(FadeOut(blackboards_used_text, *blackboard_outlines, run_time=1))

        letters_text = Text(
            "A, E, N, P, R, S, W", color=BLACK, font=MAIN_FONT, font_size=48
        ).move_to(UP * 1.8)
        blackboard_outlines = NineBlackboards.draw_outlines(["A", "E", "N", "P", "R", "S", "W"])
        self.play(
            Write(letters_text, run_time=2),
            FadeIn(*blackboard_outlines, run_time=2),
        )
        self.pause(5)
        self.play(FadeOut(letters_text, *blackboard_outlines, run_time=1))

        main_blackboard_text = Text(
            "Main Blackboard", color=BLACK, font=MAIN_FONT, font_size=48
        ).move_to(UP * 1.8)
        blackboard_outlines = NineBlackboards.draw_outlines(["G"])
        self.play(
            Write(main_blackboard_text, run_time=2),
            FadeIn(*blackboard_outlines, run_time=2),
        )
        self.pause(6)
        self.play(FadeOut(main_blackboard_text, *blackboard_outlines, run_time=1))

        final_blackboard_text = Text(
            "Final Blackboard", color=BLACK, font=MAIN_FONT, font_size=48
        ).move_to(UP * 1.8)
        blackboard_outlines = NineBlackboards.draw_outlines(["H"])
        self.play(
            Write(final_blackboard_text, run_time=2),
            FadeIn(*blackboard_outlines, run_time=2),
        )
        self.pause(5)
        self.play(FadeOut(final_blackboard_text, *blackboard_outlines, run_time=1))

        self.play(FadeOut(*outlines, *texts, run_time=1))
        self.pause(1)

    def draw_outlines(letters):
        outlines = []

        for letter in letters:
            row_index, column_index = INDEX_FOR_QWERTY_LETTER[letter]
            position = position_for_index(row_index, column_index, 0, 0.6)
            outlines.append(
                draw_key_outline(position, color=YELLOW, fill_opacity=0, stroke_width=6)
            )

        return outlines


class StepOne(AdventureScene):
    def draw_scene(self):
        step_1_text = Text("Step 1", font_size=72, color=BLACK, font=MAIN_FONT)
        self.play(Write(step_1_text, run_time=1))
        self.play(FadeOut(step_1_text, run_time=1))

        keyboard_status = init_keyboard_status(self)

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "create_keyboard",
                    "run_time": 2,
                },
                {
                    "type": "create_position_circle",
                    "letter": "H",
                    "run_time": 2,
                },
            ],
        )

        time_per_step = 0.45

        StepOne.write_on_blackboard(keyboard_status, "H", "w r w w nw p e p", time_per_step)
        StepOne.move(keyboard_status, "N", "se", time_per_step)
        StepOne.write_on_blackboard(
            keyboard_status, "N", "p nw w a w w w p ne p p e p se e", time_per_step
        )
        StepOne.move(keyboard_status, "M", "e", time_per_step)
        StepOne.move(keyboard_status, "K", "ne", time_per_step)
        StepOne.move(keyboard_status, "O", "ne", time_per_step)
        StepOne.move(keyboard_status, "P", "e", time_per_step)
        StepOne.write_on_blackboard(
            keyboard_status,
            "P",
            "p sw w w w w a se e p nw nw w w w p p p p p e p se e",
            time_per_step,
        )
        StepOne.move(keyboard_status, "O", "w", time_per_step)
        StepOne.move(keyboard_status, "I", "w", time_per_step)
        StepOne.move(keyboard_status, "U", "w", time_per_step)
        StepOne.move(keyboard_status, "Y", "w", time_per_step)
        StepOne.move(keyboard_status, "T", "w", time_per_step)
        StepOne.move(keyboard_status, "R", "w", time_per_step)
        StepOne.write_on_blackboard(
            keyboard_status, "R", "p se e a se e p nw nw w w w w p p e e p se e", time_per_step
        )
        StepOne.move(keyboard_status, "E", "w", time_per_step)
        StepOne.write_on_blackboard(
            keyboard_status,
            "E",
            "p se e e a se e p nw nw w w w w p p p e e p se e",
            time_per_step,
        )
        StepOne.move(keyboard_status, "W", "w", time_per_step)
        StepOne.write_on_blackboard(
            keyboard_status,
            "W",
            "p se e e e a se e p nw nw w w w w p p p p e e p se e",
            time_per_step,
        )
        StepOne.move(keyboard_status, "A", "sw", time_per_step)
        StepOne.write_on_blackboard(
            keyboard_status, "A", "p e e e e a nw w w w p p p p e e p se e", time_per_step
        )
        StepOne.move(keyboard_status, "S", "e", time_per_step)
        StepOne.write_on_blackboard(
            keyboard_status, "S", "p e e e a nw w w w p p p e e p se e", time_per_step
        )
        StepOne.move(keyboard_status, "D", "e", time_per_step)
        StepOne.move(keyboard_status, "F", "e", time_per_step)
        StepOne.move(keyboard_status, "G", "e", time_per_step)

        process_events(
            keyboard_status,
            [
                {
                    "type": "fade_out_keyboard",
                    "run_time": 1,
                },
                {
                    "type": "fade_out_commands",
                    "run_time": 1,
                },
            ],
        )
        self.pause(1)

    def write_on_blackboard(keyboard_status, letter, commands, time_per_step):
        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "create_blackboard",
                    "letter": letter,
                    "run_time": time_per_step,
                },
                {
                    "type": "add_command",
                    "command": f"a {commands}",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_text",
                    "text": commands,
                    "transition": "write",
                    "run_time": time_per_step,
                }
            ],
        )
        keyboard_status["scene"].pause(time_per_step / 2)

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "fade_out_blackboard",
                    "run_time": time_per_step / 2,
                }
            ],
        )

        return keyboard_status

    def move(keyboard_status, letter, command, time_per_step):
        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "move",
                    "letter": letter,
                    "run_time": time_per_step,
                },
                {
                    "type": "add_command",
                    "command": command,
                    "run_time": time_per_step / 2,
                },
            ],
        )

        return keyboard_status


class StepTwo(AdventureScene):
    def draw_scene(self):
        step_1_header = Text(
            "Letters Typed on Real Keyboard in Step 1:",
            color=BLACK,
            font_size=40,
            font=MAIN_FONT,
        ).move_to(UP * 2.5)

        step_1_commands = Text(
            "\n".join(split_text(STEP_1_TEXT, 35, False)),
            color=BLACK,
            width=12,
            font_size=24,
            font=TERMINAL_FONT,
            line_spacing=0.5,
        ).move_to(DOWN * 0.75)

        self.play(
            Write(step_1_header, run_time=1), FadeIn(step_1_commands, lag_ratio=0.4, run_time=3)
        )
        self.pause(3)

        a_text = (
            Text("a", color=BLACK, font_size=40, font=TERMINAL_FONT)
            .move_to(UP * 0.92)
            .align_on_border(LEFT, buff=1.142)
        )
        step_2_text = Text("Step 2", font_size=72, color=BLACK, font=MAIN_FONT)
        self.play(
            FadeOut(step_1_header, run_time=2),
            *animate_text_remove_letters(a_text, step_1_commands, run_time=2),
        )
        self.play(Write(step_2_text, run_time=1))
        self.pause(1)

        a_text.generate_target()
        a_text.target.align_on_border(UP, buff=1.05).align_on_border(LEFT, buff=0.5)
        self.play(MoveToTarget(a_text, run_time=1), FadeOut(step_2_text, run_time=1))

        keyboard_status = init_keyboard_status(self)
        keyboard_status["previous_real_text"] = a_text

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "create_keyboard",
                    "run_time": 2,
                },
                {
                    "type": "create_letters_typed_headers",
                    "run_time": 2,
                },
                {
                    "type": "real_text",
                    "letters": "a ... ",
                    "run_time": 2,
                },
                {
                    "type": "create_position_circle",
                    "letter": "G",
                    "run_time": 2,
                },
            ],
        )
        self.pause(1)

        time_per_step = 1

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "move",
                    "letter": "F",
                    "run_time": time_per_step,
                },
                {
                    "type": "real_text",
                    "letters": "w",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "move",
                    "letter": "D",
                    "run_time": time_per_step,
                },
                {
                    "type": "real_text",
                    "letters": "w",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "move",
                    "letter": "S",
                    "run_time": time_per_step,
                },
                {
                    "type": "real_text",
                    "letters": "w",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "move",
                    "letter": "A",
                    "run_time": time_per_step,
                },
                {
                    "type": "real_text",
                    "letters": "w",
                    "run_time": time_per_step,
                },
            ],
        )

        self.pause(2)

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "create_blackboard",
                    "letter": "A",
                    "run_time": time_per_step,
                },
                {
                    "type": "real_text",
                    "letters": "r",
                    "run_time": time_per_step,
                },
                {
                    "type": "blackboard_text",
                    "text": "p e e e e a nw w w w p p p p e e p se e",
                    "transition": "fade",
                    "run_time": time_per_step,
                },
            ],
        )

        self.pause(6)

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": LEFT * 2.4 + UP * 0.56,
                    "run_time": 1.5,
                },
                {
                    "type": "button_press",
                    "letter": "A",
                    "run_time": 4.5,
                },
            ],
        )

        self.pause(7)

        time_per_step = 1

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": LEFT * 1.89 + UP * 0.56,
                    "run_time": time_per_step,
                },
                {
                    "type": "move",
                    "letter": "S",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": LEFT * 1.39 + UP * 0.56,
                    "run_time": time_per_step,
                },
                {
                    "type": "move",
                    "letter": "D",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": LEFT * 0.89 + UP * 0.56,
                    "run_time": time_per_step,
                },
                {
                    "type": "move",
                    "letter": "F",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": LEFT * 0.38 + UP * 0.56,
                    "run_time": time_per_step,
                },
                {
                    "type": "move",
                    "letter": "G",
                    "run_time": time_per_step,
                },
            ],
        )

        self.pause(7)

        wwwwr_highlight = Rectangle(color="#f2db05", width=1.8, height=0.6, stroke_width=6).move_to(
            UP * 2.81 + LEFT * 4.1
        )
        self.play(FadeIn(wwwwr_highlight, run_time=2))
        self.pause(5)
        self.play(FadeOut(wwwwr_highlight, run_time=1))
        self.pause(1)

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": RIGHT * 0.12 + UP * 0.56,
                    "run_time": 1,
                },
            ],
        )
        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "fade_out_keyboard",
                    "run_time": 1,
                },
                {
                    "type": "fade_out_logs",
                    "run_time": 1,
                },
            ],
        )

        shift_animations = []
        for element in [
            keyboard_status["blackboard"],
            keyboard_status["blackboard_letter"],
            keyboard_status["blackboard_text"],
            keyboard_status["blackboard_arrow"],
        ]:
            element.generate_target()
            element.target.shift(LEFT * 3.5)
            shift_animations.append(MoveToTarget(element, run_time=1))

        g_blackboard_position = DOWN * 1.95
        g_blackboard, g_letter = draw_blackboard_with_letter(g_blackboard_position, "G")

        self.play(*shift_animations, FadeIn(g_blackboard, g_letter, run_time=2))

        arrow = keyboard_status["blackboard_arrow"]
        arrow.generate_target()
        arrow.target.shift(RIGHT * 2.25)
        self.play(MoveToTarget(arrow, run_time=0.5, rate_func=rate_functions.linear))

        arrow.generate_target()
        arrow.target.shift(LEFT * 4.75 + DOWN * 1.125)
        self.play(MoveToTarget(arrow, run_time=0.8, rate_func=rate_functions.ease_in_out_cubic))

        arrow.generate_target()
        arrow.target.shift(RIGHT * 4.25)
        self.play(MoveToTarget(arrow, run_time=0.8, rate_func=rate_functions.linear))

        g_blackboard_text = draw_blackboard_text(
            g_blackboard_position, "nw w w w p p p p e e p se e"
        )
        self.play(Write(g_blackboard_text, run_time=1), FadeOut(arrow, run_time=1))
        self.pause(1)

        shift_animations = []
        for element in [
            g_blackboard,
            g_letter,
            g_blackboard_text,
        ]:
            element.generate_target()
            element.target.shift(RIGHT * 3.5 + UP * 3.9)
            shift_animations.append(MoveToTarget(element, run_time=1.5))

        self.play(
            FadeOut(
                keyboard_status["blackboard"],
                keyboard_status["blackboard_letter"],
                keyboard_status["blackboard_text"],
                run_time=1,
            ),
        )
        self.play(*shift_animations)

        keyboard_status = init_keyboard_status(self)
        keyboard_status["blackboard"] = g_blackboard
        keyboard_status["blackboard_letter"] = g_letter
        keyboard_status["blackboard_text"] = g_blackboard_text

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "create_keyboard",
                    "run_time": 2,
                },
                {
                    "type": "create_position_circle",
                    "letter": "G",
                    "run_time": 2,
                },
                {
                    "type": "create_letters_typed_headers",
                    "run_time": 2,
                },
                {
                    "type": "real_text",
                    "letters": "a ... wwwwr ... ",
                    "run_time": 2,
                },
                {
                    "type": "game_text",
                    "letters": "A ... ",
                    "run_time": 2,
                },
                {
                    "type": "blackboard_text",
                    "text": "nw w w w p p p p e e p se e ...",
                    "transition": "fade",
                    "run_time": 2,
                },
            ],
        )
        self.pause(1)

        time_per_step = 0.7

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": LEFT * 2.26 + UP * 0.56,
                    "run_time": time_per_step,
                },
                {
                    "type": "move",
                    "letter": "T",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": LEFT * 1.645 + UP * 0.56,
                    "run_time": time_per_step,
                },
                {
                    "type": "move",
                    "letter": "R",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": LEFT * 1.14 + UP * 0.56,
                    "run_time": time_per_step,
                },
                {
                    "type": "move",
                    "letter": "E",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": LEFT * 0.635 + UP * 0.56,
                    "run_time": time_per_step,
                },
                {
                    "type": "move",
                    "letter": "W",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": LEFT * 0.12 + UP * 0.56,
                    "run_time": time_per_step,
                },
                {
                    "type": "button_press",
                    "letter": "W",
                    "run_time": time_per_step * 3,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": RIGHT * 0.385 + UP * 0.56,
                    "run_time": time_per_step,
                },
                {
                    "type": "button_press",
                    "letter": "W",
                    "run_time": time_per_step * 3,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": RIGHT * 0.89 + UP * 0.56,
                    "run_time": time_per_step,
                },
                {
                    "type": "button_press",
                    "letter": "W",
                    "run_time": time_per_step * 3,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": RIGHT * 1.4 + UP * 0.56,
                    "run_time": time_per_step,
                },
                {
                    "type": "button_press",
                    "letter": "W",
                    "run_time": time_per_step * 3,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": RIGHT * 1.89 + UP * 0.56,
                    "run_time": time_per_step,
                },
                {
                    "type": "move",
                    "letter": "E",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": RIGHT * 2.405 + UP * 0.56,
                    "run_time": time_per_step,
                },
                {
                    "type": "move",
                    "letter": "R",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": LEFT * 2.39 + DOWN * 0.565,
                    "run_time": time_per_step,
                },
                {
                    "type": "button_press",
                    "letter": "R",
                    "run_time": time_per_step * 3,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": LEFT * 1.78 + DOWN * 0.565,
                    "run_time": time_per_step,
                },
                {
                    "type": "move",
                    "letter": "F",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": LEFT * 1.135 + DOWN * 0.565,
                    "run_time": time_per_step,
                },
                {
                    "type": "move",
                    "letter": "G",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "fade_out_blackboard_arrow",
                    "run_time": time_per_step,
                },
            ],
        )
        self.pause(1)

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "fade_out_keyboard",
                    "run_time": 1,
                },
                {
                    "type": "fade_out_logs",
                    "run_time": 1,
                },
                {
                    "type": "fade_out_blackboard",
                    "run_time": 1,
                },
            ],
        )

        self.pause(1)


class RepeatStepTwo(AdventureScene):
    def draw_scene(self):
        step_1_real_header = Text(
            "Letters Typed on Real Keyboard in Step 1:",
            color=BLACK,
            font_size=32,
            font=MAIN_FONT,
        ).move_to(UP * 3.3)

        step_1_real_commands = (
            Text(
                "\n".join(split_text(STEP_1_TEXT, 69, False)),
                color=BLACK,
                width=12,
                font_size=14,
                font=TERMINAL_FONT,
                line_spacing=0.5,
            )
            .align_to(step_1_real_header, UP)
            .shift(DOWN * 0.75)
        )

        self.play(
            Write(step_1_real_header, run_time=1),
            FadeIn(step_1_real_commands, lag_ratio=0.4, run_time=3),
        )
        self.pause(5)

        step_2_game_header = Text(
            "Letters Typed on Game Keyboard in Step 2:",
            color=BLACK,
            font_size=32,
            font=MAIN_FONT,
        ).move_to(UP * 1.1)

        step_2_game_commands = (
            Text(
                "AWRWWNWPEPSEAPNWWAWWWPNEPPEPSEEENENEEAPSWWWWWASEEPNWNWW\nWWPPPPPEPSEEWWWWWWAPSEEASEEPNWNWWWWWPPEEPSEEWAPSEEEASEEPN\nWNWWWWWPPPEEPSEEWAPSEEEEASEEPNWNWWWWWPPPPEEPSEESWAPEEEEAN\nWWWWPPPPEEPSEEEAPEEEANWWWWPPPEEPSEEEEE",
                color=QWERTY_COLOR,
                width=12,
                font_size=24,
                font=MAIN_FONT,
                line_spacing=0.5,
            )
            .align_to(step_2_game_header, UP)
            .shift(DOWN * 0.75)
        )

        self.play(
            Write(step_2_game_header, run_time=1),
            FadeIn(step_2_game_commands, lag_ratio=0.4, run_time=3),
        )
        self.pause(3)

        step_2_real_header = Text(
            "Letters Typed on Real Keyboard in Step 2:",
            color=BLACK,
            font_size=32,
            font=MAIN_FONT,
        ).move_to(DOWN * 1.45)

        step_2_real_commands = (
            Text(
                "\n".join(split_text(STEP_2_TEXT, 120, False)),
                color=BLACK,
                width=12,
                font_size=24,
                font=TERMINAL_FONT,
                line_spacing=0.25,
            )
            .align_to(step_2_real_header, UP)
            .shift(DOWN * 0.75)
        )

        self.play(
            Write(step_2_real_header, run_time=1),
            FadeIn(step_2_real_commands, lag_ratio=0.4, run_time=5),
        )
        self.pause(1)

        self.play(
            FadeOut(
                step_1_real_header,
                step_1_real_commands,
                step_2_game_header,
                step_2_game_commands,
                step_2_real_header,
                run_time=1,
            )
        )

        g_blackboard, g_letter = draw_blackboard_with_letter(DOWN * 1.25, "G")
        step_2_real_commands.generate_target()
        step_2_real_commands.target.move_to(UP * 2.25)
        self.play(
            MoveToTarget(step_2_real_commands, run_time=1.5),
            FadeIn(g_blackboard, g_letter, run_time=3),
        )

        blackboard_text = Text(
            "\n".join(split_text(G_BLACKBOARD_TEXT, 140)),
            color=WHITE,
            font=TERMINAL_FONT,
            width=5.8,
            line_spacing=0.1,
        ).move_to(DOWN * 1.25)
        self.play(Write(blackboard_text, run_time=4))

        self.pause(1)

        self.play(
            FadeOut(step_2_real_commands, g_blackboard, g_letter, blackboard_text, run_time=1)
        )
        self.pause(1)


class StepThree(AdventureScene):
    def draw_scene(self):
        step_3_text = Text("Step 3", font_size=72, color=BLACK, font=MAIN_FONT)
        self.play(Write(step_3_text, run_time=1))
        self.pause(1)
        self.play(FadeOut(step_3_text, run_time=1))

        keyboard_status = init_keyboard_status(self)

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "create_keyboard",
                    "run_time": 2,
                },
                {
                    "type": "create_position_circle",
                    "letter": "G",
                    "run_time": 2,
                },
                {
                    "type": "create_letters_typed_headers",
                    "run_time": 2,
                },
                {
                    "type": "real_text",
                    "letters": "a ... wwwwr ... ",
                    "run_time": 2,
                },
                {
                    "type": "game_text",
                    "letters": "A ... ",
                    "run_time": 2,
                },
            ],
        )
        self.pause(1)

        time_per_step = 1

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "move",
                    "letter": "H",
                    "run_time": time_per_step,
                },
                {
                    "type": "real_text",
                    "letters": "e",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "create_blackboard",
                    "letter": "H",
                    "run_time": time_per_step,
                },
                {
                    "type": "real_text",
                    "letters": "r",
                    "run_time": time_per_step,
                },
                {
                    "type": "blackboard_text",
                    "text": "w r w w nw p e p",
                    "transition": "fade",
                    "run_time": time_per_step,
                },
            ],
        )
        self.pause(2)

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": LEFT * 1.86,
                    "run_time": time_per_step,
                },
                {
                    "type": "move",
                    "letter": "G",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": LEFT * 1.35,
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "fade_out_keyboard",
                    "run_time": 1,
                },
                {
                    "type": "fade_out_logs",
                    "run_time": 1,
                },
            ],
        )

        g_blackboard_position = DOWN * 1.95 + RIGHT * 3.5
        g_blackboard, g_letter = draw_blackboard_with_letter(g_blackboard_position, "G")

        g_blackboard_text = Text(
            "\n".join(split_text(G_BLACKBOARD_TEXT, 140)),
            color=WHITE,
            font=TERMINAL_FONT,
            width=5.8,
            line_spacing=0.1,
        ).move_to(g_blackboard_position)

        g_blackboard_arrow = draw_blackboard_arrow(UP * 1.75 + LEFT * 2.85 + g_blackboard_position)

        step_3_game_header = (
            Text(
                "Letters Typed on Game\nKeyboard in Step 3:",
                color=BLACK,
                font_size=32,
                font=MAIN_FONT,
            )
            .move_to(UP * 3)
            .align_on_border(LEFT, buff=0.5)
        )

        self.play(
            FadeIn(g_blackboard, g_letter, g_blackboard_text, run_time=2),
            Write(step_3_game_header, run_time=2),
        )
        self.play(FadeIn(g_blackboard_arrow, run_time=1))

        self.pause(1)

        letters = ""
        previous_game_text = None
        time_per_letter_group = 0.4
        arrow_moving_right = True

        letter_groups = split_text(
            "\n".join(split_text(STEP_3_GAME_TEXT, 40, False)),
            116,
            False,
        )

        for letter_group in letter_groups:
            letters += letter_group

            g_blackboard_arrow.generate_target()
            if arrow_moving_right:
                g_blackboard_arrow.target.shift(RIGHT * 5.7)
                arrow_animation = MoveToTarget(
                    g_blackboard_arrow,
                    run_time=time_per_letter_group,
                    rate_func=rate_functions.linear,
                )
            else:
                g_blackboard_arrow.target.shift(DOWN * 0.644 + LEFT * 5.7)
                arrow_animation = MoveToTarget(
                    g_blackboard_arrow,
                    run_time=time_per_letter_group,
                    rate_func=rate_functions.ease_in_out_cubic,
                )
            arrow_moving_right = not arrow_moving_right

            game_text = (
                Text(
                    letters + "\n" * 60 + "W" * 38,
                    color=QWERTY_COLOR,
                    width=6,
                    font_size=24,
                    font=MAIN_FONT,
                    line_spacing=0.5,
                )
                .align_to(step_3_game_header, UP)
                .shift(DOWN * 1.25)
                .align_on_border(LEFT, buff=0.5)
            )

            self.play(
                *animate_text_add_letters(
                    game_text, previous_game_text, run_time=time_per_letter_group
                ),
                arrow_animation,
            )

            previous_game_text = game_text

        self.play(FadeOut(g_blackboard_arrow, run_time=1))
        self.pause(1)

        self.play(
            FadeOut(
                g_blackboard,
                g_letter,
                g_blackboard_text,
                step_3_game_header,
                previous_game_text,
                run_time=1,
            ),
        )

        previous_keyboard_status = keyboard_status
        keyboard_status = init_keyboard_status(self)
        keyboard_status["blackboard"] = previous_keyboard_status["blackboard"]
        keyboard_status["blackboard_letter"] = previous_keyboard_status["blackboard_letter"]
        keyboard_status["blackboard_text"] = previous_keyboard_status["blackboard_text"]
        keyboard_status["blackboard_arrow"] = previous_keyboard_status["blackboard_arrow"]

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "create_keyboard",
                    "run_time": 2,
                },
                {
                    "type": "create_position_circle",
                    "letter": "G",
                    "run_time": 2,
                },
                {
                    "type": "create_letters_typed_headers",
                    "run_time": 2,
                },
                {
                    "type": "real_text",
                    "letters": "a ... wwwwr ... er",
                    "run_time": 2,
                },
                {
                    "type": "game_text",
                    "letters": "A ... WWWWR ... ",
                    "run_time": 2,
                },
            ],
        )
        self.pause(7)

        time_per_step = 0.8

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": LEFT * 0.87,
                    "run_time": time_per_step,
                },
                {
                    "type": "move",
                    "letter": "F",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": LEFT * 0.37,
                    "run_time": time_per_step,
                },
                {
                    "type": "move",
                    "letter": "D",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": RIGHT * 0.26,
                    "run_time": time_per_step,
                },
                {
                    "type": "move",
                    "letter": "E",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": RIGHT * 0.89,
                    "run_time": time_per_step,
                },
                {
                    "type": "button_press",
                    "letter": "E",
                    "run_time": time_per_step * 3,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": RIGHT * 1.39,
                    "run_time": time_per_step,
                },
                {
                    "type": "move",
                    "letter": "R",
                    "run_time": time_per_step,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "blackboard_arrow",
                    "position": RIGHT * 1.89,
                    "run_time": time_per_step,
                },
                {
                    "type": "button_press",
                    "letter": "R",
                    "run_time": time_per_step * 3,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "fade_out_blackboard_arrow",
                    "run_time": 1,
                },
            ],
        )

        keyboard_status = process_events(
            keyboard_status,
            [
                {
                    "type": "fade_out_blackboard",
                    "run_time": 1,
                },
                {
                    "type": "fade_out_keyboard",
                    "run_time": 1,
                },
                {
                    "type": "fade_out_logs",
                    "run_time": 1,
                },
            ],
        )

        self.pause(1)


class CommandsTable(AdventureScene):
    def draw_scene(self):
        table_height = 7
        table_width = 13.2
        table_top = UP * (table_height / 2)
        table_bottom = DOWN * (table_height / 2)
        table_left = LEFT * (table_width / 2)
        table_right = RIGHT * (table_width / 2)

        vertical_lines = []
        for ratio in [0.2, 0.6]:
            line_x = table_left + RIGHT * table_width * ratio
            line = Line(table_top + line_x, table_bottom + line_x).set_color(BLACK)
            vertical_lines.append(line)

        horizontal_lines = []
        for ratio in [0.1, 0.4, 0.7]:
            line_y = table_top + DOWN * table_height * ratio
            line = Line(table_left + line_y, table_right + line_y).set_color(BLACK)
            horizontal_lines.append(line)

        top_labels = []
        for ratio, text in [(0.4, "Real Keyboard"), (0.8, "Game Keyboard")]:
            text_x = table_left + RIGHT * table_width * ratio
            text_element = Text(text, color=BLACK, font=MAIN_FONT, font_size=28).move_to(
                table_top + DOWN * table_height * 0.05 + text_x
            )
            top_labels.append(text_element)

        left_labels = []
        for ratio, text in [(0.255, "Step 1"), (0.555, "Step 2"), (0.855, "Step 3")]:
            text_y = table_top + DOWN * table_height * ratio
            text_element = Text(text, color=BLACK, font=MAIN_FONT, font_size=40).move_to(
                table_left + RIGHT * table_width * 0.097 + text_y
            )
            left_labels.append(text_element)

        self.play(
            *[
                Write(item, run_time=3)
                for item in vertical_lines + horizontal_lines + top_labels + left_labels
            ]
        )
        self.pause(3)

        box_1_outline = "#d98f8f"
        box_1_fill = "#ffd9d9"
        box_2_outline = "#d9d98f"
        box_2_fill = "#ffffd9"
        box_3_outline = "#8fc4d9"
        box_3_fill = "#d9f4ff"

        box_1_real_text = CommandsTable.draw_box(
            "Set Up Blackboards",
            "207 Letters",
            box_1_fill,
            box_1_outline,
            table_top + DOWN * table_height * 0.25 + table_left + RIGHT * table_width * 0.4,
        )
        self.play(*[Write(item, run_time=3) for item in box_1_real_text])
        self.pause(10)

        box_1_game_text = CommandsTable.draw_box(
            "Read Blackboard for Each Step 1 Letter",
            "207 Letters",
            box_1_fill,
            box_1_outline,
            table_top + DOWN * table_height * 0.55 + table_left + RIGHT * table_width * 0.8,
        )
        self.play(*[Write(item, run_time=3) for item in box_1_game_text])
        self.pause(4)

        box_2_real_text = CommandsTable.draw_box(
            "Navigate to Blackboard for Each Step 1 Letter",
            "1144 Letters",
            box_2_fill,
            box_2_outline,
            table_top + DOWN * table_height * 0.55 + table_left + RIGHT * table_width * 0.4,
        )
        self.play(*[Write(item, run_time=3) for item in box_2_real_text])
        self.pause(2)

        box_3_real_text = CommandsTable.draw_box(
            "Navigate to Final Blackboard",
            "2 Letters",
            box_3_fill,
            box_3_outline,
            table_top + DOWN * table_height * 0.85 + table_left + RIGHT * table_width * 0.4,
        )
        self.play(*[Write(item, run_time=3) for item in box_3_real_text])
        self.pause(5)

        box_2_game_text = CommandsTable.draw_box(
            "Read Main Blackboard",
            "1144 Letters",
            box_2_fill,
            box_2_outline,
            table_top + DOWN * table_height * 0.778 + table_left + RIGHT * table_width * 0.8,
        )
        self.play(*[Write(item, run_time=3) for item in box_2_game_text])
        self.pause(3)

        box_3_game_text = CommandsTable.draw_box(
            "Read Final Blackboard",
            "2 Letters",
            box_3_fill,
            box_3_outline,
            table_top + DOWN * table_height * 0.922 + table_left + RIGHT * table_width * 0.8,
        )
        self.play(*[Write(item, run_time=3) for item in box_3_game_text])
        self.pause(7)

        self.play(
            FadeOut(
                *horizontal_lines,
                *vertical_lines,
                *top_labels,
                *left_labels,
                *box_1_real_text,
                *box_1_game_text,
                *box_2_real_text,
                *box_2_game_text,
                *box_3_real_text,
                *box_3_game_text,
                run_time=1,
            )
        )
        self.pause(1)

    def draw_box(top_text, bottom_text, fill_color, outline_color, position):
        rectangle = (
            RoundedRectangle(
                width=5.1,
                height=0.9,
                corner_radius=0.05,
                color=outline_color,
            )
            .set_fill(fill_color, opacity=1)
            .move_to(position)
        )
        top_text_element = Text(top_text, color=BLACK, font=MAIN_FONT, font_size=16).move_to(
            position + UP * 0.18
        )
        bottom_text_element = Text(
            bottom_text, color=BLACK, font=MAIN_FONT, weight=BOLD, font_size=20
        ).move_to(position + DOWN * 0.18)
        return [rectangle, top_text_element, bottom_text_element]


class AllCommands(AdventureScene):
    def draw_scene(self):
        # 997 total commands
        all_commands = [
            "a w r w w nw p e p",
            "se",
            "a p nw w a w w w p ne p p e p se e",
            "e",
            "ne",
            "ne",
            "e",
            "a p sw w w w w a se e p nw nw w w w p p p p p e p se e",
            "w",
            "w",
            "w",
            "w",
            "w",
            "w",
            "a p se e a se e p nw nw w w w w p p e e p se e",
            "w",
            "a p se e e a se e p nw nw w w w w p p p e e p se e",
            "w",
            "a p se e e e a se e p nw nw w w w w p p p p e e p se e",
            "sw",
            "a p e e e e a nw w w w p p p p e e p se e",
            "e",
            "a p e e e a nw w w w p p p e e p se e",
            "e",
            "e",
            "e",
            "w",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "se",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "w",
            "w",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "se",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "w",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "se",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "se",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "se",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "w",
            "w",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "w",
            "w",
            "w",
            "w",
            "r",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "se",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "se",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "w",
            "w",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "w",
            "w",
            "w",
            "w",
            "r",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "se",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "se",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "w",
            "w",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "w",
            "w",
            "w",
            "w",
            "r",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "se",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "se",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "w",
            "w",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "w",
            "w",
            "w",
            "w",
            "r",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "se",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "se",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "w",
            "w",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "w",
            "w",
            "w",
            "w",
            "r",
            "se",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "w",
            "w",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "w",
            "w",
            "w",
            "w",
            "r",
            "se",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "ne",
            "e",
            "e",
            "e",
            "e",
            "r",
            "w",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "nw",
            "w",
            "w",
            "r",
            "e",
            "r",
        ]

        game = AdventureGame()
        for command in all_commands:
            game.run_command(command)

        final_line = game.get_current_output().split("\n")[-2]

        updated_commands = []
        for command in all_commands:
            updated_command = "\n  ".join(split_text(command, 18))
            updated_commands.append(f"> {updated_command}")

        chunk_size = 50
        command_chunks = [
            updated_commands[i : i + chunk_size]
            for i in range(0, len(updated_commands), chunk_size)
        ]

        previous_text = None
        animations = []
        border_buffer = 5.1

        for commands_in_chunk in command_chunks:
            chunk_text = "\n".join(commands_in_chunk)

            commands_text = Text(
                chunk_text,
                font=TERMINAL_FONT,
                color=BLACK,
                font_size=18,
            )

            commands_text.generate_target()

            if previous_text is not None:
                commands_text.next_to(previous_text, DOWN)
                commands_text.target.next_to(previous_text.target, DOWN).align_on_border(
                    LEFT, buff=border_buffer
                )
            else:
                commands_text.align_on_border(UP, buff=8)
                commands_text.target.align_on_border(DOWN, buff=242)

            commands_text.align_on_border(LEFT, buff=border_buffer)

            animations.append(
                MoveToTarget(commands_text, run_time=15, rate_func=rate_functions.ease_in_out_sine)
            )
            previous_text = commands_text

        self.play(*animations)
        self.pause(1)

        final_game_text = MarkupText(
            final_line,
            color=BLACK,
            width=12,
            font_size=48,
            font=TERMINAL_FONT,
        )
        self.play(Write(final_game_text, run_time=2))
        self.pause(1)

        self.play(FadeOut(final_game_text, run_time=1))
        self.pause(1)


class AllScenes(AdventureScene):
    ALL_SCENES = [
        Intro,
        GameIntro,
        DungeonRoom,
        TypeSameThing,
        GameKeyboardType,
        GoalOfPuzzle,
        NavigatingPressingButtons,
        Blackboards,
        BlackboardExample,
        NineBlackboards,
        StepOne,
        StepTwo,
        RepeatStepTwo,
        StepThree,
        CommandsTable,
        AllCommands,
    ]

    def draw_scene(self):
        for scene in self.ALL_SCENES:
            scene.draw_scene(self)
