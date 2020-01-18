# Needed modules will be imported and configured.
import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BCM)
   
# Declaration of the LED and sensor pins
LED_PIN = 24
Sensor_PIN = 23
GPIO.setup(Sensor_PIN, GPIO.IN)
GPIO.setup(LED_PIN, GPIO.OUT)
   
print "Sensor-test [press ctrl+c to end the test]"
   
# This output function will be started at signal detection
def ausgabeFunktion(null):
        GPIO.output(LED_PIN, True)
        dateTimeObj = datetime.now()
        file = open("data/027-sensor.txt","a") 
        file.write(str(dateTimeObj)+ " = Falling signal detected! \n")
        file.close() 
        print "earthquake"
   
# This output function will be started at signal detection 
GPIO.add_event_detect(Sensor_PIN, GPIO.FALLING, callback=ausgabeFunktion, bouncetime=10) 
   
# main program loop 
try:
        
        while True:
                
                time.sleep(0.2)
                # output will be reseted if the switch turn back to the default position.
                if GPIO.input(Sensor_PIN):
                
                    GPIO.output(LED_PIN,False)
   
# Scavenging work after the program has ended
except KeyboardInterrupt:
        GPIO.cleanup()
