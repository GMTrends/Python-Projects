#ldrtwo.py
# IoT basic program that will text a mobile phone an alert message if the light sensor is blocked.

from gpiozero import LightSensor
from twilio.rest import TwilioRestClient
from time import sleep

ACCOUNT_SID = "AC312ffc062eace1ec90dd2610363611ec"
AUTH_TOKEN = "921ec55355d1753b3952453bfd397f2b"

ldr = LightSensor(4)
client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

# Twilio Code
try:
    while True:
        sleep(0.2)
        print("ldr.value " + str(ldr.value))
        if ldr.value < 0.95: # make the sensitivity different
            print("Light Blocked")
            client.messages.create(to = "+16518954575",
            from_ = "+15612200110",
            body="Your name light was blocked")  #Use your twilio phone number given on your twilio email
            break;
        else:
            print("Light On")
except KeyboardInterrupt:
    print("Exiting ...")
finally:
    ldr.close()
