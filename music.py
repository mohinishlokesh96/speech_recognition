import speech as s
import playsound
def music_list():
    s.speak("Here is a list of music you would like:")
    print("1. Star Trek")
    print("2. Star wars")

def playing_music():
    s.speak("Which music do you want me to play?. You can just say the number")
    number=s.wording()
    if number == '1':
        playsound.playsound("Voice packages\Star Wars\John Williams - Finale.mp3")



