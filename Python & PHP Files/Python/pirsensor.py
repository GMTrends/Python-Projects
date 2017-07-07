# pirsensor.py
# This script will send an email alert when the Raspberry Pi's sensor detects movement.

# Connections:
# VCC   PIN1 - pwr
# OUT   PIN11 - GPIO17
# GRN   

import RPi.GPIO as GPIO
import smtplib  # Library necessary to send emails
from email.mime.text import MIMEText  # Allows us to create email text messages
from time import sleep
from ledonoff import turn_on_led  #To call the "ledonoff" script module

def send_mail(from_address,to_address,user_name,user_password,msg_text):
    msg = MIMEText(msg_text)
    msg['Subject'] = "PYTHON WITH RASPBERRY PI " + "AWESOME TEST"
    msg['From'] = from_address
    msg['To'] = to_address
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(user_name,user_password)
    server.send_message(msg)
    server.quit()

GPIO.setmode(GPIO.BCM)  # Broadcom - main chip on the Raspberry Pi
control_pin = 17  # corresponds to the GPIO pin where you connected jumper
GPIO.setup(control_pin, GPIO.IN)  # the control_pin will accept input

fromaddress = 'velazquezraf@gmail.com'
toaddress = 'velazquezraf@gmail.com'
username = 'velazquezraf@gmail.com'
password = 'mypassword' # <--- *** Update password before testing code ***

# Code for the LED
green_led = 22

try:
    print("start...")
    email_sent = False
    while True:
        print("Waiting...")
        if GPIO.input(control_pin) == 1: # detects when there is motion
            print("motion detected")
            turn_on_led(green_led,2) #Turn on LED when there is motion
            if not email_sent:  # Call function to send email
                #send_mail(fromaddress,toaddress,username,password,"Motion Detected")
                print("Email sent")
                email_sent = True
        else:
            print("no motion detected")
        sleep(0.5)
except KeyboardInterrupt:
    GPIO.cleanup()  # Use so your Pi doesn't get too overworked and fries!
    print("Exiting...")
finally:
    GPIO.cleanup() # Always use this to put device back to clean state!
    print("Done")
