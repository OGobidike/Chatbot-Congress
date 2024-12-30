# Chatbotz: Conversational AI with Personality

![Chatbotz Banner] 
*Where cutting-edge AI meets the art of human interaction.*

---

## 🚀 **Project Overview**

**Chatbotz** is a Python-based framework for creating chatbots with unique personalities and customizable system prompts. Inspired by historical and philosophical figures, Chatbotz allows you to build AI-powered conversational agents tailored to specific personas, topics, or styles of communication. This project demonstrates the flexibility and power of OpenAI’s GPT-3.5 Turbo API to simulate compelling and meaningful conversations.

---

## 🌟 **Features**

- **Reusable Chatbot Class**: Easily create new chatbot instances with distinct personalities and behaviors.
- **Dynamic Interactions**: Chatbots can interact with users and each other for multi-agent conversations.
- **Personality-Driven Conversations**: Each chatbot is driven by a system prompt, allowing for rich, contextual dialogue.
- **Error Handling**: Built-in backoff strategy to gracefully handle rate limits and API errors.
- **Scalable Design**: Modular structure for extending functionality or integrating with other APIs.

---

## 🤖 **Chatbot Personalities**

### Meet the Stars:

1. **Broad Shoulders (Plato)**  
   The philosophical thinker who dives deep into abstract concepts and big-picture ideas.  
   ![Plato Avatar](https://via.placeholder.com/200x200.png?text=Plato)

2. **Cicero**  
   The orator and statesman, known for persuasive arguments and logical reasoning.  
   ![Cicero Avatar](https://via.placeholder.com/200x200.png?text=Cicero)

3. **Omnibus**  
   The polymathic guide, offering diverse insights across multiple domains.  
   ![Omnibus Avatar](https://via.placeholder.com/200x200.png?text=Omnibus)

---

## 📜 **How It Works**

### 1. **Chatbot Class**
Each chatbot is created using the `Chatbotz` class, which allows you to:
- Define a name for the bot.
- Provide a system prompt to shape its responses.

```python
Plato = Chatbotz("Plato", "A philosopher who explores the nature of reality and ideas.")
```

### 2. **Chatbot Interactions**
The `chatbot_interaction` function facilitates conversations between multiple chatbots or a chatbot and a user. Specify the number of turns and watch the dialogue unfold!

```python
chatbot_interaction(
    [Plato, Cicero, Omnibus],
    initial_message="Let's discuss the evolution of storytelling through history."
)
```

### 3. **Custom Prompts**
System prompts are loaded from external files, allowing easy customization of chatbot behavior.

```python
def load_prompt(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()
```

---

## 🛠️ **Getting Started**

### Prerequisites

- Python 3.8+
- OpenAI API Key
- Required libraries: `openai`, `dotenv`, `backoff`

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/chatbotz.git
   cd chatbotz
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key:
   - Create a `.env` file in the root directory:
     ```env
     OPENAI_API_KEY=your_openai_api_key
     ```

4. Run the program:
   ```bash
   python main.py
   ```

---

## 📂 **Project Structure**

```
chatbotz/
├── chatbot.py          # Chatbot class implementation
├── interactions.py     # Multi-chatbot interaction logic
├── main.py             # Entry point for the application
├── promptz/            # Directory for storing system prompts
│   ├── Broad_shoulderz.txt
│   ├── Cicero.txt
│   └── Omnibus.txt
├── .env                # Environment variables (OpenAI API Key)
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 💡 **Key Technologies**

- **OpenAI API**: GPT-3.5 Turbo for conversational intelligence.
- **Python**: Primary programming language.
- **Backoff**: For handling API rate limits gracefully.
- **Dotenv**: Secure management of API keys and environment variables.

---

## 📈 **Future Enhancements**

- **User Interface**: Add a web-based UI using Flask or Streamlit.
- **Memory**: Enable long-term memory for more context-aware conversations.
- **Multilingual Support**: Expand chatbot capabilities to support multiple languages.
- **Voice Integration**: Add TTS and ASR for voice-based interactions.

---

## 📷 **Screenshots**

![Chatbots in Action](https://via.placeholder.com/800x400.png?text=Chatbot+Interaction+Screenshot)
*Dynamic and engaging interactions between chatbots.*

---

## 🤝 **Contributing**

Contributions are welcome! Feel free to fork the repo, create a branch, and submit a pull request. Let’s make Chatbotz even better together!

---

## 📜 **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 **Acknowledgments**

- **OpenAI** for providing state-of-the-art APIs.
- **Inspiration** from historical figures who shaped human thought.
- **Community** support for bringing this project to life.

---

![Footer Image](https://via.placeholder.com/1200x100.png?text=Thank+you+for+exploring+Chatbotz!)

