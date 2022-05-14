from itertools import chain

from manim import *

from fonts import KEY_FONT, MAIN_FONT, TERMINAL_FONT
from text_animations import animate_text_add_letters

QWERTY_LETTERS = [
    ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
    ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
    ["Z", "X", "C", "V", "B", "N", "M"],
]

DUNGEON_LETTERS = [
    ["H", "A", "S", "K", "Y", "D", "B", "T", "O", "T"],
    ["T", "E", "E", "A", "M", "E", "H", "I", "N"],
    ["S", "R", "P", "O", "Y", "B", "G"],
]

BLACKBOARD_ARROW_COLOR = "#2bffaa"
DUNGEON_COLOR = "#ff2929"
KEY_FILL = "#f0f0f0"
POSITION_CIRCLE_COLOR = "#ff8b26"
QWERTY_COLOR = "#2929ff"

INDEX_FOR_QWERTY_LETTER = {}

for x, row in enumerate(QWERTY_LETTERS):
    for y, letter in enumerate(row):
        INDEX_FOR_QWERTY_LETTER[letter] = (x, y)


def draw_key_outline(position, color=BLACK, fill_opacity=1, stroke_width=4):
    return (
        RoundedRectangle(
            width=0.85, height=0.85, corner_radius=0.1, color=color, stroke_width=stroke_width
        )
        .set_fill(KEY_FILL, opacity=fill_opacity)
        .move_to(position)
    )


def draw_key_text(position, letter, color):
    return Text(text=letter, color=color, font=KEY_FONT, weight=BOLD, z_index=1).move_to(position)


def draw_key(position, letter, color):
    return (
        draw_key_outline(position),
        draw_key_text(position, letter, color),
    )


def position_for_index(row, column, x_offset, y_offset):
    position_x = -4.5 + row * 0.5 + column + x_offset
    position_y = -1 + row + y_offset
    return RIGHT * position_x + DOWN * position_y


def position_for_letter(letter, x_offset, y_offset):
    row, column = INDEX_FOR_QWERTY_LETTER[letter]
    return position_for_index(row, column, x_offset, y_offset)


def draw_keyboard(letters, letter_color, x_offset, y_offset):
    outlines = []
    texts = []

    for i in range(len(letters)):
        row = letters[i]

        for j in range(len(row)):
            position = position_for_index(i, j, x_offset, y_offset)
            letter = row[j]

            outline, text = draw_key(position, letter, letter_color)

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
    position = position_for_letter(letter, x_offset, y_offset)

    return Circle(radius=0.365, color=POSITION_CIRCLE_COLOR, stroke_width=6).move_to(position)


def animate_position_circle_move(position_circle, letter, x_offset, y_offset, run_time):
    position = position_for_letter(letter, x_offset, y_offset)

    position_circle.generate_target()
    position_circle.target.move_to(position)

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
        .align_on_border(UP, buff=1.05)
        .align_on_border(LEFT, buff=0.5)
    )


def draw_game_letters_text(letters):
    return (
        Text(letters, color=QWERTY_COLOR, font_size=33, font=MAIN_FONT, weight=BOLD)
        .move_to(UP * 1.3)
        .align_on_border(LEFT, buff=0.5)
    )


def draw_button_and_tooltip(letter, x_offset, y_offset):
    position = position_for_letter(letter, x_offset, y_offset)

    button_not_pressed = ImageMobject("images/button_not_pressed.png", z_index=4).move_to(
        position + UP * 1.16
    )
    button_pressed = ImageMobject("images/button_pressed.png", z_index=3).move_to(
        position + UP * 1.16
    )
    tooltip = ImageMobject("images/button_tooltip.png", z_index=2).move_to(position + UP * 1.08)

    return (button_not_pressed, button_pressed, tooltip)


def draw_blackboard_arrow(position):
    return Arrow(
        start=position + DOWN * 0.75,
        end=position + DOWN * 0.15,
        buff=0,
        color=BLACKBOARD_ARROW_COLOR,
        max_tip_length_to_length_ratio=0.4,
        max_stroke_width_to_length_ratio=12,
    )


def animate_blackboard_arrow_move(arrow, position, run_time):
    arrow.generate_target()
    arrow.target.move_to(position + DOWN * 0.45)
    return MoveToTarget(arrow, run_time=run_time)


def draw_blackboard_with_letter(position, letter):
    blackboard = ImageMobject("images/blackboard.png").move_to(position)
    blackboard_letter = (
        Text(letter, color=QWERTY_COLOR, font_size=48, font=MAIN_FONT, weight=BOLD)
        .align_to(blackboard, UP + RIGHT)
        .shift(LEFT * 6.3)
    )
    return blackboard, blackboard_letter


def draw_blackboard_text(position, text):
    updated_text = "\n".join(split_text(text, 20))

    width = 5 if ("\n" in updated_text) else None

    return Text(
        updated_text, color=WHITE, font_size=36, font=TERMINAL_FONT, width=width, line_spacing=2
    ).move_to(position)


def draw_command(command):
    updated_command = "\n  ".join(split_text(command, 26))

    width = 6 if ("\n" in updated_command) else None
    scale = 1 if ("\n" in updated_command) else 1.05

    return (
        Text(f"> {updated_command}", font_size=28, font=TERMINAL_FONT, color=BLACK, width=width)
        .scale(scale)
        .align_on_border(LEFT, buff=0.5)
        .shift(UP * 0.3)
    )


def split_text(text, line_length):
    result = []
    current_line = ""

    for letters in text.split():
        if len(current_line) >= line_length:
            result.append(current_line)
            current_line = ""

        current_line += f" {letters}" if current_line else letters

    if current_line:
        result.append(current_line)

    return result


def shift_previous_commands(commands, run_time):
    animations = []

    for command in commands:
        command.generate_target()
        command.target.shift(UP * 1.05)
        animations.append(MoveToTarget(command, run_time=run_time))

    return animations


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
        "blackboard": None,
        "blackboard_letter": None,
        "blackboard_text": None,
        "blackboard_arrow": None,
        "commands": [],
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

    type: create_blackboard
    - letter
    - run_time

    type: move
    - letter
    - run_time

    type: real_text
    - letters
    - run_time

    type: game_text
    - letters
    - run_time

    type: button_press
    - letter
    - run_time

    type: blackboard_text
    - text
    - transition
    - run_time

    type: blackboard_arrow
    - position
    - run_time

    type: add_command
    - command
    - run_time

    type: fade_out_keyboard
    - run_time

    type: fade_out_logs
    - run_time

    type: fade_out_blackboard
    - run_time

    type: fade_out_blackboard_arrow
    - run_time

    type: fade_out_commands
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
    blackboard = keyboard_status["blackboard"]
    blackboard_letter = keyboard_status["blackboard_letter"]
    blackboard_text = keyboard_status["blackboard_text"]
    blackboard_arrow = keyboard_status["blackboard_arrow"]
    commands = keyboard_status["commands"]

    x_offset = 0
    y_offset = 2.25
    blackboard_position = 3.5 * RIGHT + 1.83 * UP
    animation_layers = 3

    animations = {i: [] for i in range(animation_layers)}

    for event in events:
        event_type = event["type"]
        run_time = event["run_time"]

        if event_type == "create_keyboard":
            outlines, texts = draw_qwerty_keyboard(x_offset, y_offset)
            animations[0].extend(animate_keyboard_create(outlines, texts, run_time=run_time))
        elif event_type == "create_position_circle":
            letter = event["letter"]

            position_circle = draw_position_circle(letter, x_offset, y_offset)
            animations[0].append(FadeIn(position_circle, run_time=run_time))
        elif event_type == "create_letters_typed_headers":
            real_keyboard_header, game_keyboard_header = draw_letters_typed_headers()
            animations[0].extend(
                [
                    Write(real_keyboard_header, run_time=run_time),
                    Write(game_keyboard_header, run_time=run_time),
                ]
            )
        elif event_type == "create_blackboard":
            letter = event["letter"]

            blackboard, blackboard_letter = draw_blackboard_with_letter(blackboard_position, letter)
            animations[0].append(FadeIn(blackboard, blackboard_letter, run_time=run_time))
        elif event_type == "move":
            letter = event["letter"]

            animations[0].append(
                animate_position_circle_move(
                    position_circle, letter, x_offset, y_offset, run_time=run_time
                )
            )
        elif event_type == "real_text":
            real_letters += event["letters"]

            real_text = draw_real_letters_text(real_letters)
            animations[0].extend(
                animate_text_add_letters(real_text, previous_real_text, run_time=run_time)
            )
            previous_real_text = real_text
        elif event_type == "game_text":
            game_letters += event["letters"]

            game_text = draw_game_letters_text(game_letters)
            animations[0].extend(
                animate_text_add_letters(game_text, previous_game_text, run_time=run_time)
            )
            previous_game_text = game_text
        elif event_type == "button_press":
            letter = event["letter"]

            game_letters += letter
            game_text = draw_game_letters_text(game_letters)

            button_not_pressed, button_pressed, tooltip = draw_button_and_tooltip(
                letter, x_offset, y_offset
            )
            run_time_per_step = run_time / 5

            animations[0].append(
                FadeIn(button_not_pressed, button_pressed, tooltip, run_time=run_time_per_step)
            )

            animations[1].append(FadeOut(button_not_pressed, run_time=run_time_per_step))
            animations[1].extend(
                animate_text_add_letters(game_text, previous_game_text, run_time=run_time_per_step)
            )
            previous_game_text = game_text

            animations[2].append(FadeOut(button_pressed, tooltip, run_time=run_time_per_step))
        elif event_type == "blackboard_text":
            text = event["text"]
            transition = event["transition"]

            blackboard_text = draw_blackboard_text(blackboard_position, text)
            if transition == "fade":
                animations[0].append(FadeIn(blackboard_text, run_time=run_time))
            elif transition == "write":
                animations[0].append(Write(blackboard_text, run_time=run_time))
        elif event_type == "blackboard_arrow":
            position = event["position"]

            arrow_position = blackboard_position + position
            if blackboard_arrow is None:
                blackboard_arrow = draw_blackboard_arrow(arrow_position)
                animations[0].append(FadeIn(blackboard_arrow, run_time=run_time))
            else:
                animations[0].append(
                    animate_blackboard_arrow_move(
                        blackboard_arrow, arrow_position, run_time=run_time
                    )
                )
        elif event_type == "add_command":
            command = event["command"]

            command_element = draw_command(command)
            animations[0].extend(
                [
                    FadeIn(command_element, lag_ratio=0.4, run_time=run_time),
                    *shift_previous_commands(commands, run_time=run_time * 0.7),
                ]
            )
            commands.append(command_element)
        elif event_type == "fade_out_keyboard":
            animations[0].append(
                FadeOut(
                    *outlines,
                    *texts,
                    position_circle,
                    run_time=run_time,
                )
            )
        elif event_type == "fade_out_logs":
            animations[0].append(
                FadeOut(
                    previous_real_text,
                    previous_game_text,
                    real_keyboard_header,
                    game_keyboard_header,
                    run_time=run_time,
                )
            )
        elif event_type == "fade_out_blackboard":
            animations[0].append(
                FadeOut(
                    blackboard,
                    blackboard_letter,
                    blackboard_text,
                    run_time=run_time,
                )
            )
        elif event_type == "fade_out_blackboard_arrow":
            animations[0].append(FadeOut(blackboard_arrow, run_time=run_time))
            blackboard_arrow = None
        elif event_type == "fade_out_commands":
            animations[0].append(FadeOut(*commands, run_time=run_time))

    keyboard_status["previous_real_text"] = previous_real_text
    keyboard_status["previous_game_text"] = previous_game_text
    keyboard_status["real_letters"] = real_letters
    keyboard_status["game_letters"] = game_letters
    keyboard_status["outlines"] = outlines
    keyboard_status["texts"] = texts
    keyboard_status["real_keyboard_header"] = real_keyboard_header
    keyboard_status["game_keyboard_header"] = game_keyboard_header
    keyboard_status["position_circle"] = position_circle
    keyboard_status["blackboard"] = blackboard
    keyboard_status["blackboard_letter"] = blackboard_letter
    keyboard_status["blackboard_text"] = blackboard_text
    keyboard_status["blackboard_arrow"] = blackboard_arrow
    keyboard_status["commands"] = commands

    for i in range(animation_layers):
        animations_in_layer = animations[i]
        if animations_in_layer:
            scene.play(*animations_in_layer)

    return keyboard_status
