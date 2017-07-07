# pythontwo.py

from sense_hat import SenseHat

# Step 1 - Calculate the area of a right triangle
height = input("Enter the height ")
height = float(height)

base = input("Enter the base ")
base = float(base)

if (height < 0) or (base < 0):
    print("Invalid data")
else:
    area = (base * height) / 2
    print("The area of the right triangle is " + format(area, '0.2f') + " = " + "{:.1e}".format(area) + "\n")

# Step 2 - Choose an option for the conditional code block
print("a The Muay Thai Kitchen")
print("b The Spaghetti Palace")
print("c The Taco Guru")

choice = input("Where do you want to have dinner? Enter a, b, or c. \n")

if (choice == 'a') or (choice == 'A'):
    print("Thai food is delicious \n")
elif (choice == 'b') or ((choice == 'B'):
    print("Italian food is delicious \n")
elif (choice == 'c') or (choice == 'C'):
    print("Mexican food is delicious \n")
else:
    print("But we'll starve. \n")

# Step 3 - Display conditional results in Sense Hat with try-catch exeption handling
sense = SenseHat()
try:
    number = int(input("Enter a number between 1 and 100 \n"))
    if (number > 0) and (number <= 50):
        print("LO \n")
        sense.show_message("LO", scroll_speed=.04, text_colour=[0,255,0])
    elif (number > 50) and (number <= 100):
        print("HI \n")
        sense.show_message("HI", scroll_speed=.04, text_colour=[0,255,255])
    else:
        print("Value is out of bounds \n")
        sense.show_message("Value is out of bounds", scroll_speed=.04, text_colour=[255,255,255])
except ValueError:
    print("You didn\'t enter a number \n")
    sense.show_message("You didn\'t enter a number", scroll_speed=.04, text_colour=[255,0,0])

