#move_robot.py
# This script will run the robot in a loop

from rrb3 import *
from time import sleep

def main():
    BATTERY_VOLTS = 8.1
    MOTOR_VOLTS = 4

    rr = RRB3(BATTERY_VOLTS, MOTOR_VOLTS)

    motor_speed = 0.5  # Motor speed (bigger number is faster up to 1.9)
    try:
        while True:
            rr.forward(4,motor_speed) # run engines for four seconds
            rr.right(4,motor_speed) # run engines for four seconds
            rr.left(4,motor_speed) # run engines for four seconds
            rr.reverse(4,motor_speed) # run engines for four seconds
    except KeyboardInterrupt:
        print("Exiting")
    finally:
        print("Cleaning up")
        rr.cleanup()
        sleep(1)
        
main()
