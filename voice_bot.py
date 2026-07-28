import speech_recognition as sr
import pyttsx3
import subprocess

engine = pyttsx3.init()
engine.setProperty("rate", 175)

def speak(text: str) -> None:
    engine.say(text)
    engine.runAndWait()

def listen() -> str:
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.6)
        print("Listening...")
        audio = recognizer.listen(source, phrase_time_limit=5)
    return recognizer.recognize_google(audio).lower()

COMMANDS = {
    "open notepad": ["notepad"],
    "open calculator": ["calc"],
    "open browser": ["cmd", "/c", "start", "chrome"],
}

def run():
    speak("Voice Command Robot is online. How can I help?")
    while True:
        try:
            command = listen()
            print(f"You said: {command}")
            if "stop" in command or "exit" in command:
                speak("Shutting down. Goodbye!")
                break
            for phrase, args in COMMANDS.items():
                if phrase in command:
                    speak(f"Running {phrase}")
                    subprocess.Popen(args, shell=True)
                    break
            else:
                speak("Sorry, I didn't recognise that command.")
        except sr.UnknownValueError:
            speak("Could you repeat that?")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    run()
