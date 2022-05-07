from itertools import chain

from manim import *

from fonts import KEY_FONT, MAIN_FONT, TERMINAL_FONT
from text_animations import animate_text_add_letters

KEY_FILL = "#f0f0f0"

QWERTY_LETTERS = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
    ["Z", "X", "C", "V", "B", "N", "M"],
]
QWERTY_COLOR = "#2929ff"

DUNGEON_LETTERS = [
    ["H", "A", "S", "K", "Y", "D", "B", "T", "O", "T"],
    ["T", "E", "E", "A", "M", "E", "H", "I", "N"],
    ["S", "R", "P", "O", "Y", "B", "G"],
]
DUNGEON_COLOR = "#ff2929"

POSITION_CIRCLE_COLOR = "#ffa200"

INDEX_FOR_QWERTY_LETTER = {}

for x, row in enumerate(QWERTY_LETTERS):
    for y, letter in enumerate(row):
        INDEX_FOR_QWERTY_LETTER[letter] = (x, y)


def vector_for_position(position_x, position_y):
    return RIGHT * position_x + DOWN * position_y


def draw_key_outline(position_x, position_y, color=BLACK, fill_opacity=1, stroke_width=4):
    return (
        RoundedRectangle(
            width=0.85, height=0.85, corner_radius=0.1, color=color, stroke_width=stroke_width
        )
        .set_fill(KEY_FILL, opacity=fill_opacity)
        .move_to(vector_for_position(position_x, position_y))
    )


def draw_key_text(position_x, position_y, letter, color):
    return Text(text=letter, color=color, font=KEY_FONT, weight=BOLD, z_index=1).move_to(
        vector_for_position(position_x, position_y)
    )


def draw_key(position_x, position_y, letter, color):
    return (
        draw_key_outline(position_x, position_y),
        draw_key_text(position_x, position_y, letter, color),
    )


def coordinate_for_index(row, column, x_offset, y_offset):
    return (
        -4.5 + row * 0.5 + column + x_offset,
        -1 + row + y_offset,
    )


def coordinate_for_letter(letter, x_offset, y_offset):
    row, column = INDEX_FOR_QWERTY_LETTER[letter]
    return coordinate_for_index(row, column, x_offset, y_offset)


def draw_keyboard(letters, letter_color, x_offset, y_offset):
    outlines = []
    texts = []

    for i in range(len(letters)):
        row = letters[i]

        for j in range(len(row)):
            position_x, position_y = coordinate_for_index(i, j, x_offset, y_offset)
            letter = row[j]

            outline, text = draw_key(position_x, position_y, letter, letter_color)

            outlines.append(outline)
            texts.append(text)

    return outlines, texts


def draw_qwerty_keyboard(x_offset, y_offset):
    return draw_keyboard(QWERTY_LETTERS, QWERTY_COLOR, x_offset, y_offset)


def draw_dungeon_keyboard(x_offset, y_offset):
    return draw_keyboard(DUNGEON_LETTERS, DUNGEON_COLOR, x_offset, y_offset)


def animate_keyboard_outlines(outlines, run_time):
    return (Write(outline, run_time=run_time) for outline in outlines)


def animate_keyboard_texts(texts, run_time):
    return (FadeIn(text, run_time=run_time) for text in texts)


def animate_keyboard_create(outlines, texts, run_time):
    return chain(
        animate_keyboard_outlines(outlines, run_time), animate_keyboard_texts(texts, run_time)
    )


def draw_position_circle(letter, x_offset, y_offset):
    position_x, position_y = coordinate_for_letter(letter, x_offset, y_offset)

    return Circle(radius=0.365, color=POSITION_CIRCLE_COLOR, stroke_width=6).move_to(
        vector_for_position(position_x, position_y)
    )


def animate_position_circle_move(position_circle, letter, x_offset, y_offset, run_time):
    position_x, position_y = coordinate_for_letter(letter, x_offset, y_offset)

    position_circle.generate_target()
    position_circle.target.move_to(vector_for_position(position_x, position_y))

    return MoveToTarget(position_circle, run_time=run_time)


def draw_letters_typed_headers():
    real_keyboard_header = (
        Text("Letters Typed on Real Keyboard:", color=BLACK, font_size=24, font=MAIN_FONT)
        .align_on_border(UP, buff=0.5)
        .align_on_border(LEFT, buff=0.5)
    )
    game_keyboard_header = (
        Text("Letters Typed on Game Keyboard:", color=BLACK, font_size=24, font=MAIN_FONT)
        .align_on_border(UP, buff=2)
        .align_on_border(LEFT, buff=0.5)
    )

    return (real_keyboard_header, game_keyboard_header)


def draw_real_letters_text(letters):
    return (
        Text(letters, color=BLACK, font_size=40, font=TERMINAL_FONT)
        .align_on_border(UP, buff=1.25)
        .align_on_border(LEFT, buff=0.5)
    )


def draw_game_letters_text(letters):
    return (
        Text(letters, color=QWERTY_COLOR, font_size=33, font=MAIN_FONT, weight=BOLD)
        .move_to(UP * 2)
        .align_on_border(LEFT, buff=0.5)
    )


def init_keyboard_status(scene):
    return {
        "scene": scene,
        "previous_real_text": None,
        "previous_game_text": None,
        "real_letters": "",
        "game_letters": "",
        "outlines": None,
        "texts": None,
        "real_keyboard_header": None,
        "game_keyboard_header": None,
        "position_circle": None,
    }


def process_events(keyboard_status, events):
    """
    type: create_keyboard
    - run_time

    type: create_position_circle
    - letter
    - run_time

    type: create_letters_typed_headers
    - run_time

    type: move
    - letter
    - run_time

    type: real_text
    - letters
    - run_time

    type: button_press
    - letter
    - run_time
    """

    scene = keyboard_status["scene"]
    previous_real_text = keyboard_status["previous_real_text"]
    previous_game_text = keyboard_status["previous_game_text"]
    real_letters = keyboard_status["real_letters"]
    game_letters = keyboard_status["game_letters"]
    outlines = keyboard_status["outlines"]
    texts = keyboard_status["texts"]
    real_keyboard_header = keyboard_status["real_keyboard_header"]
    game_keyboard_header = keyboard_status["game_keyboard_header"]
    position_circle = keyboard_status["position_circle"]

    x_offset = 0
    y_offset = 2.25

    animations = []

    for event in events:
        event_type = event["type"]
        run_time = event["run_time"]

        if event_type == "create_keyboard":
            outlines, texts = draw_qwerty_keyboard(x_offset, y_offset)
            animations.extend(animate_keyboard_create(outlines, texts, run_time=run_time))
        elif event_type == "create_position_circle":
            letter = event["letter"]

            position_circle = draw_position_circle(letter, x_offset, y_offset)
            animations.append(FadeIn(position_circle, run_time=1))
        elif event_type == "create_letters_typed_headers":
            real_keyboard_header, game_keyboard_header = draw_letters_typed_headers()
            animations.extend(
                [
                    Write(real_keyboard_header, run_time=1),
                    Write(game_keyboard_header, run_time=1),
                ]
            )
        elif event_type == "move":
            letter = event["letter"]

            animations.append(
                animate_position_circle_move(
                    position_circle, letter, x_offset, y_offset, run_time=run_time
                )
            )
        elif event_type == "real_text":
            real_letters += event["letters"]

            real_text = draw_real_letters_text(real_letters)
            animations.extend(
                animate_text_add_letters(real_text, previous_real_text, run_time=run_time)
            )
            previous_real_text = real_text

    keyboard_status["previous_real_text"] = previous_real_text
    keyboard_status["previous_game_text"] = previous_game_text
    keyboard_status["real_letters"] = real_letters
    keyboard_status["game_letters"] = game_letters
    keyboard_status["outlines"] = outlines
    keyboard_status["texts"] = texts
    keyboard_status["real_keyboard_header"] = real_keyboard_header
    keyboard_status["game_keyboard_header"] = game_keyboard_header
    keyboard_status["position_circle"] = position_circle

    scene.play(*animations)

    return keyboard_status
