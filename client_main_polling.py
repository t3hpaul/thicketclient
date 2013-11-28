'''
The main client applicaiton.
Needs to be renamed to thicketclient_main.py


'''

from Phidgets.PhidgetException import *
from Phidgets.Events.Events import *
from Phidgets.Devices.InterfaceKit import *
from request_handler import put_value_change, register_device
from backend_utilities import gen_id_val,get_local_ip
from request_handler import put_value_change
#from register_module import register_phidget
import json
from time import sleep
from logging_framework import *
import sys
import logging


logname = 'thicket.log'
logging.basicConfig(filename=logname,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)

'''
Code to connect to the sensor itself.
'''
def connectSensors():
	try:
  		logging.info('creating the interface kit')
  		device = InterfaceKit()
	except RuntimeError as e:
  		#log_error("Error when trying to create the device: %s" % e.message)
  		print "ERROR"
  		log_error("Error when trying to create the device")

	#This connects to the device.
	try:
 		#print 'connecting to the device!'
  		device.openPhidget()
	except PhidgetException as e:
 		#log_warning("Exception when trying to connect %i: %s" % (e.code, e.detail))		
  		print "ERROR"
  		logging.warning("Exception when trying to connect" )
  		exit(1)

	return device

'''
Checks the range of sensors for the phidget
'''
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

if __name__ == '__main__':
	dev_id = gen_id_val()

	#Connect to the sensors
	device = connectSensors()
	while True:
		sleep(1.5)
		
		device.setOutputState(0,0)
		sensor_data = checkSensors(device,5)
		response = put_value_change(dev_id,sensor_data,True)
		device.setOutputState(0,1)

	device.closePhidget()

