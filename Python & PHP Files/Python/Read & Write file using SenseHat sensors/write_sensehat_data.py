# write_sensehat_data.py
# This script will write Raspberry Pi's acceleration sensor data to a file.

# data_line = line_str.split(',')

# Dictionary --> acceleration
#       ^ +x
#       |
#-y <-usbport-> +y
#       |
#       ^ -x

from sense_hat import SenseHat
from time import sleep,time,ctime #ctime converts time to more readable format

def main():
    file_opened = False
    sense = SenseHat()

    try:
        filename = input("Enter the filename\n")
        sense_file = open(filename,"a")
        file_opened = True
        print("Move the pi around")
        while True:
            acceleration = sense.get_accelerometer_raw()
            x = acceleration['x']
            y = acceleration['y']
            z = acceleration['z']
            t1 = ctime(time())
            print("{0},{1},{2},{3}".format(x,y,z,t1))
            print("{0},{1},{2},{3}".format(x,y,z,t1), file = sense_file)
            sleep(0.5)
    except KeyboardInterrupt:
        print("Exiting...")
    except PermissionError: #do not have write permissions
        print("Permission Error")
    except IsADirectoryError:
        print("Directory is specified and not a file")
    except FileNotFoundError:
        print("File not found")
    finally:
        if file_opened:
            sense_file.close()

main()
