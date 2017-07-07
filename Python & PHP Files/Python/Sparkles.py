# This program will randomly turn on LED lights randomly on the Raspberry Pi's Sense Hat

from sense_hat import SenseHat
from random import randint
from time import sleep

while True:
    choice = input("Do you want to continue? ")
    choice = choice.lower()
    if (choice != "y"):
        break       #Exit out of the loop if "n"

sense = SenseHat()
try:
    while True:
        x = randint(0,7)    #Generate a random number between 0 and 7
        y = randint(0,7)
        r = randint(0,255)  #Generate a random number between 0 and 255
        g = randint(0,255)
        b = randint(0,255)
        sense.set_pixel(x,y,r,g,b)
        sleep(0.1)
except KeyboardInterrupt:
        print("Exiting")
        sense.clear()
finally:
        print("Clean up")

# Ctrl + C = Manual Keyboard Interrupt to exit program

