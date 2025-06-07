from assistant.speech_engine import listen, speak
from assistant.config import GEMINI_API_KEY  # Example


def run_assistant():
    speak("Hello, I'm your Gemini voice assistant. How can I help you?")
    while True:
        command = listen()
        if command.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye!")
            break
        if command:
            response = get_gemini_response(command)
            print(f"🤖 Gemini: {response}")
            speak(response)

if __name__ == "__main__":
    run_assistant()
