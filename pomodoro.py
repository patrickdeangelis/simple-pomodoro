'''
    CMD Pomodoro Timer
    Develop by: Patrick
'''

import winsound as ws 
import time

def getCurrentTimeInMinutes(): 
    return time.clock() / 60

def beep():
    ws.Beep(2500, 1000)

def startTimeCounter(time):
    sessionStartTime = getCurrentTimeInMinutes()
    currentSessionTime = 0
    while(currentSessionTime - sessionStartTime < time):
        currentSessionTime = getCurrentTimeInMinutes()
        print("{:01.1f} m".format(currentSessionTime), end="", flush=True)

def startPomodoroSession():
    #time in minutes
    startTimeCounter(20)
    beep()
    print("\nFINISH POMODORO SESSION")
    defineBreakTime()

def defineBreakTime():
    print("Case you wanna take a break type here(in minutes), if not type n:" end=" ")
    breakOption = input()

    if(breakOption.isnumeric()):
        breakOption = float(breakOption)
        startTimeCounter(breakOption)
        return
    
    
    

def menu():
    while (True):
        print("1 -> Start Pomodoro Session")
        print("2 -> Exit")
        menuOption = int(input())

        if(menuOption == 1):
            startPomodoroSession()
        elif(menuOption == 2):
            exit()
        else:
            print("Invalid value, please try again")
    
if __name__== '__main__':
    menu()