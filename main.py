import speech as s
import music as m
import timing as t
import document_creation as d
import random
music_word_list = ['Music','MUSIC','music','MuSiC']
time_word_list = ['Time','time','TIME','TiMe']
random_greetings = ['Hello','Hi','Good Morning','Hi,Its good to see you again']
positive_notes = ['Yes','Ya Boi','yes','yo','hmmm']
document_check = [ 'document',"Document",'file','File']
if __name__=="__main__":


    value =random.randrange(0,len(random_greetings))
    s.speak(random_greetings[value])
    s.speak("My name is Jericho, I am your personal Assistant for this laptop.")
    s.speak("So what would you like me to do today?")
    while True:
        word = s.wording()
        value  = word.split(" ")
        music_check =any(items in value for items in music_word_list)
        time_check = any(items in value for items in time_word_list)
        document_creation = any(items in value for items in document_check)
        if music_check:
            m.music_list()
            m.playing_music()
        elif time_check:
            s.speak("do you want today's time")
            value = s.get_audio()
            if value in positive_notes:
                t.todays_time()
            else:
                s.speak("Okay then have nice day")
        elif document_creation:
            s.speak("Do you want to create a Document?")
            value =s.get_audio()
            if value in positive_notes:
                d.get_type()
        s.speak("I am sorry. But that command is still not in my library.")
        s.speak("Your command is :"+word)









