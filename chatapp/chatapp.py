import reflex as rx

from chatapp import style

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right"
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left"
        ),
        margin_y="1em"
    )

def chat() -> rx.Component:
    qa_pairs = [
        (
            "What is Reflex?",
            "A way to build web apps in pure Python!",
        ),
        (
            "What can I make with it?",
            "Anything from a simple website to a complex web app!",
        ),
    ]
    return rx.box(
        *[
            qa(question, answer)
            for question, answer in qa_pairs
        ]
    )

def action_bar() -> rx.Component:
    return rx.form.root(
        rx.hstack(
            rx.form.field(
                rx.form.label("Message"),
                rx.form.control(
                    rx.input(
                        style=style.input_style
                    ),
                    as_child=True,
                ),
                margin_bottom="0",
                flex_grow="1"
            ),
            rx.button("Send", style=style.button_style),
            align="end"
        )
    )

def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            chat(),
            action_bar(),
            align="center"
        )  
    )

app = rx.App()
app.add_page(index)