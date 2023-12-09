import pyttsx3
import speech_recognition as sr


def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    print("")
    print(f"==> Lucy: {text}")
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            text = r.recognize_google(audio)
            return text
        except:
            return "Sorry, I did not get that"


def Main_Execution(query):
    command = query.lower()
    print(f"==> You: {command}")
    if "hello" in command:
        speak("Hello, how are you?")
    elif "how are you" in command:
        speak("I am fine, thank you")
    elif "what is your name" in command:
        speak("My name is Lucy")
    elif "what can you do" in command:
        speak(
            "I can do many things, for example, I can tell you the weather, I can search for something on the internet, I can tell you the time, and I can also tell you a joke"
        )
    elif "what is the weather" in command:
        speak("The weather is nice today")
    elif "what time is it" in command:
        speak("It is 2:30 PM")
    elif "tell me a joke" in command:
        speak("What do you call a fake noodle? An impasta")
    elif "goodbye" in command:
        speak("Goodbye, have a nice day")
    else:
        speak("Sorry, I did not get that")


while True:
    print()
    text = listen()
    Main_Execution(text)
    if "goodbye" in text:
        speak("Goodbye, have a nice day")
        break
