from features import findContact, whatsApp

import time
import pyttsx3
import speech_recognition as sr
import eel
from features import *
from util import speak




def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        eel.DisplayMessage("Listening...")
        
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)
    try:
        print('recognizing...')
        eel.DisplayMessage("Recognizing...")
        
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.DisplayMessage(query)
        time.sleep(2)

       
    except Exception as e:
        return ""
    
    return query.lower()

@eel.expose
def allCommands(message =1):
    if message == 1:
        query = takecommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)
    
    try:
        # query = takecommand()
        # print(query)
        

        if "open" in query:
            openCommand(query)
        elif "on youtube" in query:
            PlayYoutube(query)
        elif "track my location" in query or "location tracking" in query:
            speak("Tracking location.")
            Tracklocation()
        elif 'weather forecast' in query or 'what the weather' in query:
            speak("Sure, which city's weather forecast do you want to know?")
            city = takecommand().lower()
            weather(city)



        elif "send message" in query or "phone call" in query or "video call" in query:
            contact_no, name = findContact(query)
        if contact_no != 0:
            message = ""

                
            if "send message" in query:
                message = 'message'
                speak("what message to send")
                query = takecommand()
                                        
            elif "phone call" in query:
                message = 'call'
            else:
                message = 'video call'
                                        
            whatsApp(contact_no, query, message, name)
        else:
            print("not run")
    except:
        print("Error in command execution")
        

    eel.ShowHood()



