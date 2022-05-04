from manim import *


KEY_FONT = 'Century Gothic'
KEY_FILL = '#f0f0f0'


QWERTY_LETTERS = [
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
]
QWERTY_COLOR = '#2929ff'

DUNGEON_LETTERS = [
    ['H', 'A', 'S', 'K', 'Y', 'D', 'B', 'T', 'O', 'T'],
    ['T', 'E', 'E', 'A', 'M', 'E', 'H', 'I', 'N'],
    ['S', 'R', 'P', 'O', 'Y', 'B', 'G']
]
DUNGEON_COLOR = '#ff2929'


def index_for_qwerty_letter(letter):
    for x, row in enumerate(QWERTY_LETTERS):
        for y, value in enumerate(row):
            if value == letter:
                return (x, y)


def draw_key_outline(position_x, position_y, color=BLACK, fill_opacity=1, stroke_width=4):
    return RoundedRectangle(width=0.85, height=0.85, corner_radius=0.1, color=color, stroke_width=stroke_width) \
        .set_fill(KEY_FILL, opacity=fill_opacity) \
        .move_to(RIGHT * position_x + DOWN * position_y)


def draw_key_text(position_x, position_y, letter, color):
    return Text(text=letter, color=color, font=KEY_FONT, weight=BOLD) \
        .move_to(RIGHT * position_x + DOWN * position_y)


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


def draw_keyboard_create(scene, outlines, texts, run_time):
    outline_creates = map(lambda outline: Write(outline), outlines)
    text_creates = map(lambda text: FadeIn(text), texts)
    scene.play(*outline_creates, *text_creates, run_time=run_time)
