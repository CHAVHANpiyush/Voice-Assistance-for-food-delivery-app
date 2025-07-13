import gradio as gr
from main import get_chat_response, say_with_elevenlabs, get_voice_input

history = ""

# Play welcome message once when app starts
welcome_audio = say_with_elevenlabs("Welcome to Swiggato Support! Say 'exit' to quit.")

def voice_chat():
    global history

    user_input = get_voice_input()
    if not user_input or user_input.lower() == "exit":
        goodbye = "Thank you for using Swiggato Support. Have a great day!"
        audio_path = say_with_elevenlabs(goodbye)
        return "exit", goodbye, audio_path

    response = get_chat_response(user_input, history)
    history += f"\nUser: {user_input}\nAI: {response}"
    audio_path = say_with_elevenlabs(response)
    return user_input, response, audio_path

# Gradio Interface
iface = gr.Interface(
    fn=voice_chat,
    inputs=[],
    outputs=[
        gr.Textbox(label="You said"),
        gr.Textbox(label="Bot Response"),
        gr.Audio(label="Bot Voice", type="filepath")
    ],
    title="🎤 Swiggato Voice Support Bot",
    description="The bot will greet you, listen via mic, and respond via voice. Just say your question!"
)

if __name__ == "__main__":
    print("Playing welcome message...")
    from pydub import AudioSegment
    from pydub.playback import play
    audio = AudioSegment.from_file(welcome_audio, format="mp3")
    play(audio)

    iface.launch()