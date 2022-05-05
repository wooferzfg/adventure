from manim import *


def delayed_until_end(_):
    return 0


def instant_start(_):
    return 1


def animate_text_add_letters(new_text, previous_text, run_time):
    animations = [FadeIn(new_text, run_time=run_time)]

    if previous_text is None:
        return animations

    return animations + [
        FadeOut(
            previous_text,
            run_time=run_time,
            rate_func=delayed_until_end,
        )
    ]


def animate_text_remove_letters(new_text, previous_text, run_time):
    animations = [FadeIn(new_text, run_time=run_time, rate_func=instant_start)]

    return animations + [FadeOut(previous_text, run_time=run_time)]
