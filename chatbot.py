import openai  # Here i need to import the OpenAI library to interact with OpenAI's API.
import os  # import the os library for working w/ environment variables.
from dotenv import load_dotenv  # import load_dotenv so we can load environment variables
from typing import List  # just in case we need hints when typing
import backoff

# Load!
load_dotenv()

# Openai.API...SET!
openai.api_key = os.getenv("OPENAI_API_KEY")

# readddddy!!!


class Chatbotz:
    """
    A reusable chatbot class that allows you to create chatbots with unique personalities and system prompts.

    Att:
        name (str): The name of the chatbot.
        system_prompt (str): The initial system message that defines the chatbot's behavior and persona.
    """

    def __init__(self, name: str, system_prompt: str):
        """
        Initialize a new instance of the Chatbotz.

        Args:
            name (str): The name of the chatbot.
            system_prompt (str): The system message to guide the chatbot's behavior.
        """
        self.name = name  # Assign the chatbot's name to an instance variable.
        self.system_prompt = system_prompt  # Assign the system prompt to an instance variable.

    @backoff.on_exception(backoff.expo, (openai.error.RateLimitError, openai.error.ServiceUnavailableError))
    def generate_response(self, user_input: str, history: List[dict] = None) -> str:
        history = history or []
        messages = [{"role": "system", "content": self.system_prompt}] + history + [
            {"role": "user", "content": user_input}]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0.27,
        )
        return response.choices[0].message.content
