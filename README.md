# Chatbot Congress!: Conversational AI with Personality

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

1. **Mr.Broad Shoulders (Plato, if yk,yk)**  
   The philosophical thinker who dives deep into abstract concepts and big-picture ideas.  
   
2. **Cicero**  
   The orator and statesman, known for persuasive arguments and logical reasoning.  
   
3. **Omnibus**  
   The polymathic guide, offering diverse insights across multiple domains.  

---

## 📜 **How It Works**

### 1. **Chatbot Class**
Each chatbot is created using the `Chatbotz` class, which allows you to:
- Define a name for the bot.
- Provide a system prompt to shape its responses.

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

- **OpenAI API**: GPT-3.5 Turbo for conversational intelligence and... speeed!
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

## 🤝 **Contributing**

Contributions are welcome! Feel free to fork the repo, create a branch, and submit a pull request. Let’s make Chatbotz even better together!

---

## 📜 **License**

This project is licensed under the MIT License, so no funny business!


