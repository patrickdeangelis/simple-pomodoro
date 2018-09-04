'''
    CMD Pomodoro Timer
    Only suporting windows
    Developed by: Patrick
'''

import winsound as ws 
import os
import time

def getCurrentTimeInMinutes(): 
    return time.clock() / 60

def cleanScreen():
    #make it suport clear prompt on both windows and unix systems
    os.system("cls||clear")

def startTimeCounter(time):
    sessionStartTime = getCurrentTimeInMinutes()
    currentSessionTime, deltaTime = 0, 0
    while deltaTime < time:
        currentSessionTime = getCurrentTimeInMinutes()
        deltaTime = currentSessionTime - sessionStartTime
        #Using int() cause int don't round, and cut the decimal part, that's not relevant in this case
        print("      {:02d} m ".format(int(deltaTime)), end="\r", flush=True)
    print("{:02d} m ".format(int(deltaTime)))

def beep():
    for i in range(3):
        ws.Beep(2500, 100)

def startPomodoroSession():
    #time in minutes
    print("----------------")
    print("    WORKING!")
    print("----------------")
    startTimeCounter(20)
    beep()
    print("\nFINISH POMODORO SESSION")
    defineBreakTime()

def defineBreakTime():
    while (True):
        print("Case you wanna take a break type here(in minutes), if not type n:", end=" ")
        breakOption = input()
        cleanScreen()

        if(breakOption.isnumeric()):
            cleanScreen()
            breakOption = float(breakOption)
            startTimeCounter(breakOption)
            return
        else:
            if(breakOption.lower().strip() == "n"):
                return
            else:
                print("Error, try again")                
                time.sleep(0.5)

def menu():
    cleanScreen()
    while (True):
        print("=====================")
        print("POMODORO SIMPLE TIMER")
        print("=====================")
        print("1 -> Start Pomodoro Session")
        print("2 -> Exit")
        menuOption = int(input())

        if(menuOption == 1):
            cleanScreen()
            startPomodoroSession()
        elif(menuOption == 2):
            cleanScreen()
            exit()
        else:
            print("Invalid value, please try again")
    
if __name__== '__main__':
    menu()