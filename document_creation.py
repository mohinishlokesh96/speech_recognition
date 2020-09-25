import speech as s
import subprocess
type_of_files = ["doc","Doc",'t x t',"txt","TXT"]


def get_type():
    s.speak("I can create a t x t file or a doc file")
    s.speak("Which one would you want?")
    value  = s.get_audio()
    if value not in type_of_files:
        get_type()
    elif value == "doc":
        s.speak("What do you want me to save in the file?")
        said = s.get_audio()
        f = open("note.doc","w+")
        f.write(said)
        f.close

