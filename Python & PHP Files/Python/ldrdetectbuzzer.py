#ldrone.py
# Program that will print alert to console and activate the buzzer if light sensor is blocked.

from gpiozero import LightSensor,Buzzer
from time import sleep
ldr = LightSensor(4)
buzzer = Buzzer(17)
buzzer.on()
sleep(0.5)
buzzer.off()

try:
    while True:
        sleep(0.1)
        if ldr.value < 0.95: # make the sensitivity different
            print("Light Blocked" + str(ldr.value))
            buzzer.on()
            sleep(1)
        else:
            print("Light On" + str(ldr.value))
            buzzer.off()
except KeyboardInterrupt:
    print("Exiting ...")
finally:
    ldr.close()
    buzzer.close()
