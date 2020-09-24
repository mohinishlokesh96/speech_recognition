import speech as s
from datetime import datetime
import pytz
import time

responses = ['No','no','nada','Nope','no boi']
def todays_time():
    s.speak(" Springfield time is :")
    now = time.localtime()
    time1 = time.strftime("%H:%M:%S",now)
    s.speak(time1)
    s.speak("Do you need anything else:")
    if value in responses:
        return

def time_zone():
    pass





