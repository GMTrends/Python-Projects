#robot_move_avoid.py
# This script will set our robot in motion and avoid object collision (see function 'turn_robot')
# This script requires importing Simon Monk's rrb3 script from MIT 

from rrb3 import *
from time import sleep

def turn_robot(rr):
    rr.reverse(1,0.3)  # run motor for 1 second
    rr.right(0.5,0.3)  # 0.3 = speed

def main():
    BATTERY_VOLTS = 8.1
    MOTOR_VOLTS = 4

    rr = RRB3(BATTERY_VOLTS,MOTOR_VOLTS)
    running = False

    try:
        while True:
            if not rr.sw2_closed():
                print("switch open")
                running = True
            else:
                print("switch closed")
                running = False
            distance = rr.get_distance()
            print(distance)
            if running:
                rr.forward(1,0.5)
            if distance < 20 and running:
                turn_robot(rr)
                print("avoiding")
            sleep(0.1)
            
    except KeyboardInterrupt:
        print("Exiting")
        
    finally:
        print("Clean up")
        rr.cleanup()

main()
