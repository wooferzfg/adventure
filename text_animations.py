from manim import *


def animate_text_update(new_text, previous_text, run_time):
    animations = [FadeIn(new_text, run_time=run_time)]

    if previous_text is None:
        return animations

    return animations + [FadeOut(
        previous_text,
        run_time=run_time,
        rate_func=rate_functions.ease_in_expo,
    )]
