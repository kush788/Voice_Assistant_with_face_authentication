import os
import eel
from authentication import recognize
from command import *
from features import play_sound

def start():
    eel.init("frontend")
    play_sound()

    @eel.expose
    def init():
        eel.hideLoader()
        speak("Ready for face authentication")
        flag = recognize.AuthenticateFace()

        if flag == 1:
            eel.hideFaceAuth()
            speak("Face authentication successful")
            eel.hideFaceAuthSuccess()
            speak("Welcome to the system")
            eel.hideStart()
        else:
            speak("Face authentication failed, please try again")

    # Start the eel app (this will block)
    eel.start("index.html", mode='edge', host='localhost', block=True)

# Run the app
if __name__ == "__main__":
    start()
