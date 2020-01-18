import Adafruit_BMP.BMP280 as BMP280
from datetime import datetime
import time

sensor = BMP280.BMP280(address=0x76)

print 'Temp = {0:0.2f} *C'.format(sensor.read_temperature())
print 'Pressure = {0:0.2f} Pa'.format(sensor.read_pressure())
print 'Altitude = {0:0.2f} m'.format(sensor.read_altitude())
print 'Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure())

dateTimeObj = datetime.now()
file = open("data/052-temperature.txt","a") 
file.write(str(dateTimeObj)+ " = " +'Temp = {0:0.2f} *C'.format(sensor.read_temperature()) + "\n")
file.write(str(dateTimeObj)+ " = " +'Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()) + "\n")
file.write(str(dateTimeObj)+ " = " +'Altitude = {0:0.2f} m'.format(sensor.read_altitude()) + "\n")
file.write(str(dateTimeObj)+ " = " +'Sealevel Pressure = {0:0.2f} Pa'.format(sensor.read_sealevel_pressure())+ "\n")
file.close()
