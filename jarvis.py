import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        print("Processing...")
        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, could not understand audio.")
            return None

if __name__ == "__main__":
    text = listen()
    if text:
        print("You said:", text)


# Modify the Python script to send recognized text to the extension
import requests

def send_text_to_extension(text):
    url = "http://localhost:5000/update"
    data = {"text": text}
    requests.post(url, data=data)
