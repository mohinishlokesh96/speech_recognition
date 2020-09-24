import speech as s
import music as m
import timing as t
import random
music_word_list = ['Music','MUSIC','music','MuSiC']
time_word_list = ['Time','time','TIME','TiMe']
random_greetings = ["Yooo! Wassup",'Hello','Hi','Good Morning','Hi,Its good to see you again']
positive_notes = ['Yes','Ya Boi','yes','yo','hmmm']
if __name__=="__main__":


    value =random.randrange(0,len(random_greetings))
    s.speak(random_greetings[value])
    s.speak("My name is Jericho, I am your personal Assistant for this laptop.")
    while True:
        s.speak("So what would you like me to do today?")
        word = s.wording()
        value  = word.split(" ")
        music_check =any(items in value for items in music_word_list)
        time_check = any(items in value for items in time_word_list)
        if music_check:
            m.music_list()
            m.playing_music()
        elif time_check:
            s.speak("do you want today's time")
            value = s.get_audio()
            if value in positive_notes:
                t.todays_time()









