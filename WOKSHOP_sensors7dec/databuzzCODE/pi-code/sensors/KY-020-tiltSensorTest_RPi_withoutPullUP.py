# Needed modules will be imported and configured
import RPi.GPIO as GPIO
import time
from datetime import datetime
   
GPIO.setmode(GPIO.BCM)
   
# Declaration of the input pin which is connected with the sensor. Additional to that, a pullup resistor will be activated.
GPIO_PIN = 24
GPIO.setup(GPIO_PIN, GPIO.IN)
   
print "Sensor-test [press ctrl+c to end]"
   
# This outFunction will be started at signal detection.
def outFunction(null):
        dateTimeObj = datetime.now()
        file = open("data/tilt-detection.txt","a") 
        file.write(str(dateTimeObj)+ " = Tilt Signal detected! \n")
        file.close() 
        print("Signal detected")
   
# The outFunction will be started after detecting of a signal (falling signal edge)
GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback=outFunction, bouncetime=100) 
   
# Main program loop
try:
        while True:
                time.sleep(1)
   
# Scavenging work after the end of the program
except KeyboardInterrupt:
        GPIO.cleanup()
