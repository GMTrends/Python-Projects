#button_press_example.py

import RPi.GPIO as GPIO
from time import sleep

def main():
    GPIO.setmode(GPIO.BCM)
    button_pin = 4
    GPIO.setup(button_pin, GPIO.IN,pull_up_down=GPIO.PUD_UP) #voltage is up
    try:
        while True:
            value = GPIO.input(button_pin)
            print("value" + str(value))
            if value == 0: #button press pulls down to ground
                print("Button pressed")
            sleep(0.05)
    except KeyboardInterrupt:
        print("exiting...")
    finally:
        GPIO.cleanup()

main()
