#pythoneight.py

from rrb3 import *
from time import sleep

#Step 1: Robot exercise
'''
rr = RRB3(9.0,6.0)

def main ():
try:
    while True:
	print("Starting the main block")
	rr.forward(0.5,0.5)
	distance = rr.get_distance()
	print("Distance in cm " + str(distance))
	if (distance < 15.0):
	    print("Distance is less than 15 cm!")
	    rr.stop
	    rr.reverse(0.3,0.3)
	    rr.stop
	    rr.set_motors(0.3,0,0.3,1)
	    sleep(1)
except KeyboardInterrupt:
    print("Completing...")
	sleep(1)
finally:
    print("Clean up")
    rr.cleanup()

main()
'''

#Step 2a
def main():
    filename = input("Enter the filename\n")        
    file_opened = False
    inventory_items = []
try:
	inventory_file = open(filename,"a")
	file_opened = True
    while True:
		item_name = input("Enter the item name or exit to quit: ")            
		if item_name == "exit":
			break   
		number_sold = int(input("Enter the number sold: "))
		price_item = float(input("Enter the price: "))
		cost_item = float(input("Enter the cost: "))
		inventory_items.append(item_name)
		inventory_items.append(number_sold)
		inventory_items.append(price_item)
		inventory_items.append(cost_item)
		print("{0},{1},{2},{3}".format(item_name,number_sold,price_item,cost_item))
		print("{0},{1},{2},{3}".format(item_name,number_sold,price_item,cost_item),file=inventory_file)
except KeyboardInterrupt:
    print("Exiting...")
except PermissionError: # if you do not have write permissions
    print("Permission Error")
except IsADirectoryError:
    print("Directory is specified and not a file")
except FileNotFoundError:
    print("File not found")
finally:
    if file_opened:
        inventory_file.close()


#Step 2b
file_opened = False
try:
    filename = input("Enter the filename\n")  
    inventory_file = open(filename,"r")
    file_opened = True
    profit = 0
    totalProfit = 0
    for line_str in inventory_file:
		line_str = line_str.strip()
		print(line_str)            
		data_line = line_str.split(',')
		profit = float((float(data_line[2]))-(float(data_line[3])))*(float(data_line[1]))
		totalProfit += profit
		print(data_line[0] + " profit = $" + (format(profit,'.2f')))
		print()
    print("Total profits = $" + (format(totalProfit,'.2f')))    
except KeyboardInterrupt:
    print("Exiting...")
except PermissionError: 
    print("Permission Error")
except IsADirectoryError:
    print("Directory is specified and not a file")
except FileNotFoundError:
    print("File not found")
finally:
    if file_opened:
        inventory_file.close()

main()
