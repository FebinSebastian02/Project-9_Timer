#imports are done
import time
from playsound import playsound #playsound is a function in playsound module

CLEAR_CONSOLE = "\033[2J"   #ANSI escape character that clears the entire terminal screen
CLEAR_AND_RETURN = "\033[H" #ANSI escape character that overwrites on the same line in terminal

print("\n!!!TIMER!!!")
hours = int(input("\nEnter the hours after which the alarm should go off..."))
minutes = int(input("Enter the minutes after which the alarm should go off..."))
seconds = int(input("Enter the seconds after which the alarm should go off..."))

totalSeconds = (hours * 3600) + (minutes * 60) + seconds
timeElapsed = 0

print(CLEAR_CONSOLE)
while timeElapsed < totalSeconds:
    time.sleep(1)   #Freezes this line of code for 1 second so that the alarm doesn't goes off very fast.
    timeLeft = totalSeconds - timeElapsed
    hoursLeft = timeLeft // 3600    #Gives hours in the time left
    secondsLeftInHours = timeLeft % 3600    #Gives remainder of hoursLeft
    minutesLeft = secondsLeftInHours // 60    #Gives minutes in the time left
    secondsLeft = secondsLeftInHours % 60 #Gives seconds in the time left

    print(f"{CLEAR_AND_RETURN}The Countdown begins: {hoursLeft:02d} : {minutesLeft:02d} : {secondsLeft:02d}")
    #:02d is used to format time into 2 digits.
    timeElapsed += 1
playsound("Alarm.mp3")