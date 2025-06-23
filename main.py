import requests
import speech_recognition as sr
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO

# ElevenLabs API details
API_KEY = "sk_b491c10c3efd6c4200b203c238d14b6160086a1a03a10aae"
API_URL = "https://api.elevenlabs.io/v1/text-to-speech"
VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Replace with a valid voice ID

# Prompt template for the chatbot
template = """
You are a helpful support chatbot for a food delivery app. 
Your job is to assist users with their queries, such as 
order status, menu items, cancellations, and delivery timings.

Here is the conversation history: {history}

User's Question: {question}

Support Answer:
"""

# Initialize the AI model
model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# Function to synthesize speech using ElevenLabs
def say_with_elevenlabs(text):
    headers = {
        "accept": "audio/mpeg",
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }
    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.75
        }
    }
    response = requests.post(f"{API_URL}/{VOICE_ID}", json=payload, headers=headers)

    if response.status_code == 200:
        audio = AudioSegment.from_file(BytesIO(response.content), format="mp3")
        play(audio)
    else:
        print(f"Error: {response.status_code} - {response.text}")

# Function to capture user input via speech
def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            user_input = recognizer.recognize_google(audio)
            return user_input
        except sr.UnknownValueError:
            print("Bot: Sorry, I didn't catch that. Please try again.")
            say_with_elevenlabs("Sorry, I didn't catch that. Please try again.")
            return None
        except sr.RequestError:
            print("Bot: There seems to be an issue with the speech recognition service.")
            say_with_elevenlabs("There seems to be an issue with the speech recognition service.")
            return None

# Main function to handle the chatbot logic
def handle_food_delivery_support():
    history = ""
    print("Welcome to Swiggato Support! Say 'exit' to quit.")
    say_with_elevenlabs("Welcome to Swiggato Support! Say 'exit' to quit.")

    while True:
        print("You (speak now):")
        user_input = get_voice_input()
        if not user_input:
            continue

        print(f"You: {user_input}")
        if user_input.lower() == 'exit':
            print("Bot: Thank you for using Swiggato Support. Have a great day!")
            say_with_elevenlabs("Thank you for using Swiggato Support. Have a great day!")
            break

        # Generate response using the AI model
        result = chain.invoke({"history": history, "question": user_input}).strip()
        print("Bot:", result)

        # Speak the response using ElevenLabs
        say_with_elevenlabs(result)

        # Update conversation history
        history += f"\nUser: {user_input}\nAI: {result}"

if __name__ == "__main__":
    handle_food_delivery_support()