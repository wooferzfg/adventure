from manim import *


KEY_FONT = 'Century Gothic'
KEY_FILL = '#fafafa'


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


def draw_key_outline(position_x, position_y):
    return RoundedRectangle(width=0.85, height=0.85, corner_radius=0.1, color=BLACK) \
        .set_fill(KEY_FILL, opacity=1) \
        .move_to(RIGHT * position_x + DOWN * position_y)


def draw_key_text(position_x, position_y, letter, color):
    return Text(text=letter, color=color, font=KEY_FONT, weight=BOLD) \
        .move_to(RIGHT * position_x + DOWN * position_y)


def draw_key(position_x, position_y, letter, color):
    return (
        draw_key_outline(position_x, position_y),
        draw_key_text(position_x, position_y, letter, color),
    )


def draw_keyboard(letters, letter_color):
    outlines = []
    texts = []

    for i in range(len(letters)):
        row = letters[i]

        for j in range(len(row)):
            position_x = -4.5 + i * 0.5 + j
            position_y = -1 + i
            letter = row[j]

            outline, text = draw_key(position_x, position_y, letter, letter_color)

            outlines.append(outline)
            texts.append(text)

    return outlines, texts


def draw_qwerty_keyboard():
    return draw_keyboard(QWERTY_LETTERS, QWERTY_COLOR)


def draw_dungeon_keyboard():
    return draw_keyboard(DUNGEON_LETTERS, DUNGEON_COLOR)


def draw_keyboard_create(scene, outlines, texts):
    outline_creates = map(lambda outline: Create(outline), outlines)
    text_creates = map(lambda text: FadeIn(text), texts)
    scene.play(*outline_creates, *text_creates)