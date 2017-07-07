# read_sensehat_data_random.py

# sense_file.seek(0) <-- bytes of offset (location in the file)
# sense_file.tell() <-- location of the file pointer
# line_str = sense_file.readline() <-- reads one line at a time

from sense_hat import SenseHat
from time import sleep,time,ctime #ctime converts time to more readable format

def main():
    file_opened = False
    sense = SenseHat()

    try:
        filename = input("Enter the sensehat data filename\n")
        sense_file = open(filename,"r")
        file_opened = True
        line_number = int(input("Enter the line number"))
        while line_number >= 1:
            sense_file.seek(0) # go to the beginning of the file
            line_str = sense_file.readline()
            for line in range(1,line_number):
                line_str = sense_file.readline()
                if not line_str:
                    break
            if line_str:
                line_str = line_str.strip() # strip off the new lines
                data_line = line_str.split(',')
                print("x = " + data_line[0])
                print("y = " + data_line[1])
                print("z = " + data_line[2])
                print("time = " + data_line[3])
            else:
                print("Line at end of file: current location" + str(sense_file.tell()))
            line_number = int(input("Enter the line number"))
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
