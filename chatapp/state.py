import reflex as rx
import asyncio

class State(rx.State):
  # The current being asked
  question: str

  # Keep track of the chat history as a list of (question, answer) tuples.
  chat_history: list[tuple[str, str]]

  async def answer(self):
    answer = "I don't know!"
    self.chat_history.append((self.question, answer))

    # Clear the question input
    self.question = ""

    # Yield here to clear the frontend input before continuing

    yield

    for i in range(len(answer)):
      # Pause to show the streaming effect
      await asynio.sleep(0.1)
      # Add one letter at a time to the output
      self.chat_history[-1] = (
        self.chat_history[-1][0],
        answer[: i + 1]
      )
      yield