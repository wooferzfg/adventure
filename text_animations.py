from manim import *


def delayed_until_end(_):
    return 0


def animate_text_update(new_text, previous_text, run_time):
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
