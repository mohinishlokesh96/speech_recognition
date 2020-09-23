import speech as s
import music as m


music_word_list = ['Music','MUSIC','music','MuSiC']
random_greetings = ["Yo! Wassup",'Hello','Hi','Namasate','Good Morning','Good Evening','How can i help you?']

if __name__=="__main__":

    s.speak("Hi, My name is Jericho, I am your personal Assistant for this laptop.")
    while True:
        s.speak("So what would you like me to do today?")
        word = s.wording()
        value  = word.split(" ")
        check =any(items in value for items in music_word_list)
        if check:
            m.music_list()
            m.playing_music()





