import speech_recognition as sr
import pyttsx3


def speak(text):
    engine =pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
def get_audio():
    r = sr.Recognizer()
    m = sr.Microphone()
    with m as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        word = r.recognize_google(audio)
        return word
    except Exception as e:
        print("None")

def wording():
    word = get_audio()
    if word == None:
        while word ==None:
            word=get_audio()
    if word != None:
        return word
