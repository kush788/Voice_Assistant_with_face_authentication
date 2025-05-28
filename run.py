import multiprocessing
from features import hotword
from main import start



def startJarvis():
    print("Starting Jarvis...")
    start()

def listenHotword():
    print("hotword function running...")
    hotword()

if __name__ == '__main__':
        p1 = multiprocessing.Process(target=startJarvis)
        p2 = multiprocessing.Process(target=listenHotword)
        p1.start()
        p2.start() 
        p1.join()

        if p2.is_alive():
            p2.terminate()
            p2.join()

        print("system stop")