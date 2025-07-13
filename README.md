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

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt

3. **Set up environment variables**
Create a .env file in the project root with your ElevenLabs API key:
   ```bash
   pip install -r requirements.txt
4. **(macOS only) Install FFmpeg for audio support**
   ```bash
   brew install ffmpeg
5. **Run the app on CLI**
   ```bash
   python main.py
6. **Run the app on Gradio**
   ```bash
   python app.py

