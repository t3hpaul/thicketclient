#This is a test application that connects to the sensor board
#and reads from any sensors that are changing

from Phidgets.PhidgetException import *
from Phidgets.Events.Events import *
from Phidgets.Devices.InterfaceKit import *
#from request_handler import put_value_change
#from register_module import register_phidget
import json
from logging_framework import *
from lws_client_backend import gen_id_val,get_local_ip
from request_handler import put_value_change
#Triggered/run in the event that a sensor value has hanged. 
#e.value returns the value of the current sensor in whatever
#units the sensor is being measured in. For example, the
#slider is measured from 1-1000. The light sensor is measured
#from 0-100%. The index is the integer value index of the port
#that the sensor is plugged in at. With our board it ranges from 0-5. 
#logging.basicConfig(filename='/var/log/lws/lws.log')

def sensorChanged(e):
 dev_id = gen_id_val()
 print "Sensor change at %i: %i" % (e.index, e.value)
 values = checkSensors(device,6)
 put_value_change(dev_id,values,True)

def checkSensors(device,sensor_number):
	#since we can have up to 8 sensors, we check to all 8 ports
	values_dict={}
	for n in range(0,sensor_number):
		try:
			#print 'checking sensor on %s'%n
			values_dict[n] = device.getSensorValue(n)
		except:
			#print 'no sensor attached to port %s'%n
			values_dict[n] = 'N/A'

	return values_dict 

#Create and connect to the device using the InterfaceKit() method.
#This method depends on the device that we are using. For us, it
#happens to be the interfacekit.
try:
  log_info('creating the interface kit')
  device = InterfaceKit()
except RuntimeError as e:
  loggin.error("Error when trying to create the device: %s" % e.message)

#This connects to the device.
try:
  log_info('connecting to the device!')
  device.openPhidget()
except PhidgetException as e:
  log_warning("Exception when trying to connect %i: %s" % (e.code, e.detail))		
  exit(1)

device.setOnSensorChangeHandler(sensorChanged)



#Only here to block until user keyboard input, which will end the program.
character = str(raw_input())

#we have to close the phidget after we are done..
device.closePhidget()
