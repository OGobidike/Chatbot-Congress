from chatbot import Chatbotz
from interactiones import chatbot_interaction



def load_prompt(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()

Plato = Chatbotz("Broad", load_prompt("promptz/Broad_shoulderz.txt"))
Cicero = Chatbotz("Cicero", load_prompt("promptz/Cicero.txt"))
Omnibus = Chatbotz("Omnibus", load_prompt("promptz/Omnibus.txt"))

chatbot_interaction(
    [Plato, Cicero, Omnibus],
    initial_message="Let's discuss the evolution of storytelling through history.")

