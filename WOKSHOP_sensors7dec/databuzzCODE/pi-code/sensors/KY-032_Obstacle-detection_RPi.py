# Needed modules will be imported and configured
import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)
 
# Declaration of the input pin which is connected with the sensor.
GPIO_PIN = 24
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
 
# Break between the results will be defined here (in seconds)
delayTime = 0.5
 
print "Sensor-Test [press ctrl+c to end]"
 
# main program loop
try:
        while True:
            if GPIO.input(GPIO_PIN) == True:
                print "No obstacle"
            else:
                dateTimeObj = datetime.now()
                file = open("data/032-object-detection.txt","a") 
                file.write(str(dateTimeObj)+ " = Obstacle detected\n")
                file.close()
                print "Obstacle detected"
            print "---------------------------------------"
 
            # Reset + Delay
            time.sleep(delayTime)
 
# Scavenging work after the end of the program
except KeyboardInterrupt:
        GPIO.cleanup()
