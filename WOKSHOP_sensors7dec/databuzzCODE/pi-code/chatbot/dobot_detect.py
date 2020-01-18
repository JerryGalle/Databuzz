# Needed modules will be imported and configured
import RPi.GPIO as GPIO
#dobot libs
from serial.tools import list_ports
from pydobot import Dobot
import random
import time
 
GPIO.setmode(GPIO.BCM)
 
# Declaration of the input pin which is connected with the object sensor.
GPIO_PIN = 24
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)

#dobot variables
port = list_ports.comports()[0].device
device = Dobot(port=port, verbose=True)
(x, y, z, r, j1, j2, j3, j4) = device.pose()
print('x:{x} y:{y} z:{z} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')
 
# Break between the results will be defined here (in seconds)
delayTime = 0.5
 
# main program loop
try:
        while True:
            if GPIO.input(GPIO_PIN) == True:
                print ("No obstacle")
            else:
                #Make the dobot do a random 360 kickflip if something is detected
                print ("Obstacle detected")
                device.move_to(x + random.randrange(-10, 10), y + random.randrange(-10, 10), z + random.randrange(-10, 10), r, wait=False)
                device.move_to(x, y, z, r, wait=True)  # we wait until this movement is done before continuing
            print "---------------------------------------"
 
            # Reset + Delay
            time.sleep(delayTime)
 
# Scavenging work after the end of the program
except KeyboardInterrupt:
        GPIO.cleanup()
