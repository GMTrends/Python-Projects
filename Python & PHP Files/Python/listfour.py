#listfour.py - This can be used to measure the orientation of drones
from sense_hat import SenseHat
from time import sleep

def main():
    sense = SenseHat()
    data = [[0]*3,[0]*3,[0]*3]
    count = 0
    or_name = ['pitch','roll','yaw']
    while count < 3:
        orientation = sense.get_orientation()
        data[0][count] = orientation['pitch']
        data[1][count] = orientation['roll']
        data[2][count] = orientation['yaw']
        sleep(1)
        count = count + 1

    for i in range(0,3):
        print(or_name[i])
        for j in range(0,3):
            print(str(data[i][j]))

main()
