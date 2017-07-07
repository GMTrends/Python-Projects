#functionsone.py

from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

# we can return multiple values from 1 function...
def find_cost(number, tax):  # no need to specify a variable return type
    cost = number * 2.5
    total_tax = cost * tax
    cost = cost + cost * tax
    return cost, total_tax

def space_heroes(name, sense):  # "name" is the parameter
    sense.show_message(name + " is in their Star Fighter", 0.05)

def main():
    sense = SenseHat()
#   global sense   # making a global variable in main is poor programming practice
    space_heroes("Your name", sense)  
    items = int(input("Input the number of items "))
    tax_rate = float(input("Input the tax rate "))
    total, tax_found = find_cost(items, tax_rate)
    sense.show_message("The total is " + str(round(total,2)),0.05)
    print("Buck Rogers is on the way")
    space_heroes("Buck Rogers", sense) # adding sense is good practice
    space_heroes("Col. Wilma Deering", sense)
#   print("name = " + name)
    sense.clear()

main() # call the function

