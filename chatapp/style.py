# style.py
import reflex as rx

# Common styles for questions and answers.
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    max_width="30em",
    display="inline-block",
)

# Set specific styles for questions and answers.
question_style = message_style | dict(
    margin_left=chat_margin,
    background_color=rx.color("gray", 4),
)
answer_style = message_style | dict(
    margin_right=chat_margin,
    background_color=rx.color("accent", 8),
)

# Styles for the action bar.
input_style = dict(
    border_width="1px", padding="1em"
)
button_style = dict(
    background_color=rx.color("accent", 10),
)
