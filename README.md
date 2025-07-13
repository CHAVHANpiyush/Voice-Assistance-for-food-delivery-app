# Voice-Assistance-for-food-delivery-app
A conversational AI voice assistant for a food delivery app, built with:
- 🧠 LLM (LLaMA via LangChain)
- 🗣️ Speech recognition (microphone input)
- 🔊 Voice output using ElevenLabs
- ⚙️ Deployed via Gradio

---

## 📌 Features

- Ask about food orders, menus, delivery times, or cancellations
- Voice-based interaction — just speak to it!
- Real-time voice responses using ElevenLabs
- Context-aware replies with conversation memory
- Cross-platform support (Mac and Windows)

---

## 🧪 Tech Stack

- Python
- [LangChain](https://www.langchain.com/)
- [Ollama (LLaMA)](https://ollama.com/)
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
- [ElevenLabs API](https://www.elevenlabs.io/)
- [Gradio](https://www.gradio.app/)
- [Pydub](https://pydub.com/) (for audio playback)

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/CHAVHANpiyush/Voice-Assistance-for-food-delivery-app.git
cd Voice-Assistance-for-food-delivery-app
python -m venv .venv
source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
pip install -r requirements.txt
API_KEY=your_elevenlabs_api_key
python main.py       # for CLI
python app.py        # for Gradio UI
