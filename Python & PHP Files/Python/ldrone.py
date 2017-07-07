#ldrone.py
from gpiozero import LightSensor
from time import sleep
ldr = LightSensor(4)
try:
    while True:
        sleep(0.2)
        print("ldr.value " + str(ldr.value))
        if ldr.value < 0.95: # make the sensitivity different
            print("Light Blocked")
        else:
            print("Light On")
except KeyboardInterrupt:
    print("Exiting ...")
finally:
    ldr.close()
