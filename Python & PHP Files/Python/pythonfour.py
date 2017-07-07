#pythonfour.py

import smtplib  # Library necessary to send emails
from email.mime.text import MIMEText  # Allows us to create email text messages
from sense_hat import SenseHat
from time import sleep
from random import randint
sense = SenseHat()

#Step 2
def compute_discount(cost, membership):
    if(membership == True):
        cost = cost * .9
    else:
        cost = cost

    # Apply Cyber Tuesday discount of 5%
    cost = cost * .95

    return format(cost, '0.2f')  #format to 2 decimal points of precision

#Step 3
def phone_card(card):
    if(card >= 10 and card <= 20):
        minutes = card / 0.10
    elif(card == 50 or card == 100):
        minutes = (card / 0.08) + (5 / 0.08)

    return minutes

#Step 4
def multi_comp(value_one, value_two):
    result1 = value_one * value_two
    result2 = value_one + value_two
    result3 = value_one ** value_two

    return result1, result2, result3

#Step 5
def compute_balance(current_balance = 1000, payment = 20):
    current_balance = current_balance - payment
    if(current_balance > 0):
        string = "balance owed"
        return string + " = " + str(current_balance)
    elif(current_balance < 0):
        string = "credit"
        return string + " = " + str(abs(current_balance))
    elif(current_balance == 0):
        string = "paid in full"
        return string + " = 0"
        
#Step 6
def find_sum(lower_param, upper_param):
    i = lower_param
    totalSum = lower_param
    while i < upper_param:
        i += 1
        totalSum = totalSum + i
    return totalSum

#Step 8
def draw_pattern(x1, y1, x2, y2, s):
    s.set_pixel(x1,y1,[0,0,255])
    s.set_pixel(x2,y2,[0,0,255])
    sleep(5)

    s.clear()

#Step 9
def data_center_monitor(minimum_temperature, maximum_temperature,
                        minimum_humidity, maximum_humidity,
                        email_address, s):
    try:
        print("Start...")
        email_sent = False

        fromaddress = email_address
        toaddress = email_address
        username = 'velazquezraf@gmail.com'
        password = '*************'  #Modify password to test
        
        while True:
            print("Sensing environment...")
            temperature = s.get_temperature()
            fahr = temperature * (9//5) + 32 # Convert to Fahrenheit
            fahr = round(fahr, 2)
            s.show_message(str(fahr), 0.1) # Convert float value into String data
            sleep(1)

            humidity = s.get_humidity()
            humidity = round(humidity, 2)
            s.show_message(str(humidity), 0.1)
            sleep(1)
                
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        #Conditional will execute if temperature reading is outside the range of 70 and 90. Or if 40 > humidity > 55.
        if(fahr < minimum_temperature or
            fahr > maximum_temperature or
            humidity < minimum_humidity or
            humidity > maximum_humidity):
            
            # Setup code to generate email message
            msg_text = "Warning: Readings not within range. " + "Temperature = " + str(fahr) + " Humidity = " + str(humidity)
            msg = MIMEText(msg_text)
            msg['Subject'] = "Temperature/Humidity out of range"
            msg['From'] = email_address
            msg['To'] = email_address
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(username,password)
            server.send_message(msg)
            server.quit()

            print("Email sent")
            email_sent = True
        else:
            print("Temperature and humidity within range.")
            
        s.clear()
        print("Done\n")

#(BONUS)
def roll_dice():
    while True:
        number1 = randint(1, 6)
        number2 = randint(1, 6)
        sum = number1 + number2
        print("The sum is " + str(sum))
        if(sum == 7):
            print("\nYou win!")
            return sum
            break
        else:
            print("Roll again")


# Main Function Starts
def main():
    #Step 1 - (Main function called at the end of script)
    print("Rafael Velazquez")
    print("")

    #Step 2 - Call compute_discount function within main and print final cost
    print("Your total cost is " + compute_discount(150.78, True))
    print("The cost is now " + compute_discount(98.23, False))
    print("")

    #Step 3 - Call phone_card function
    print("Minutes = " + str(phone_card(100)))
    print("Minutes = " + str(phone_card(20)))
    print("")

    #Step 4 - Call multi_comp function
    print("The values are " + str(multi_comp(5, -2)))
    print("The values are " + str(multi_comp(3, 4)))
    print("")

    #Step 5
    print(compute_balance(500))
    print(compute_balance(payment = 1100))
    print(compute_balance(payment = 1000))
    print("")

    #Step 6
    print(find_sum(5, 10))
    print("")

    #Step 7
    sense = SenseHat()

    #Step 8
    draw_pattern(4,5,7,2,sense)

    #Step 9
    s = SenseHat()
    data_center_monitor(70, 90, 40, 55, 'velazquezraf@gmail.com', s)

    #(BONUS)
    roll_dice()

main()  # Call the main function
