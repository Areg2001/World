import myWorld
import time
import os


def start():
    print("The day is start.")
    while myWorld.start != myWorld.hours:
        time.sleep(1)
        myWorld.start += 1
        os.system("clear")
        print(myWorld.world)

    myWorld.start = 0
    start()

