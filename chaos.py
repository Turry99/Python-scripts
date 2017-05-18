import pyautogui as pa
import random

#set the speed of clicks
pa.PAUSE = float(input("What speed should the script click?\n>  "))

first = (377, 248)   #0
second = (1031, 275) #1
third = (675, 830)   #2
start = (638, 543)
####### CLICK THE ENDS
pa.click(first)
pa.click(second)
pa.click(third)

def getMiddle(current, endPos):
    """Get the middle coordinates of the 2 points"""
    return (int((current[0]+endPos[0])/2), int((current[1] + endPos[1])/2))

pa.click(start) # Set the mouse to the middle point

for x in range(2000):
    seed = random.randint(0,2)
    if seed == 0:
        pa.click(getMiddle(pa.position(), first))
    elif seed == 1:
        pa.click(getMiddle(pa.position(), second))
    else:
        pa.click(getMiddle(pa.position(), third))
