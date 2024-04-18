import time
alarmname=input("Alarm Name: ")
description=input("Add a decription: ")
alarmtime=input("Time(HH:MM):")
#get current time
currenttime=time.strftime("%H:%M")
if alarmtime==currenttime:
    print(alarmname.upper())
    print(description.lower())