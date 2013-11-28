'''
The main client applicaiton.
Needs to be renamed to thicketclient_main.py


'''

from Phidgets.PhidgetException import *
from Phidgets.Events.Events import *
from Phidgets.Devices.InterfaceKit import *
from request_handler import put_value_change, register_device
from lws_client_backend import gen_id_val,get_local_ip
from request_handler import put_value_change
#from register_module import register_phidget
import json
from time import sleep
from logging_framework import *


'''
Code to connect to the sensor itself.
'''
def connectSensors():
	try:
  		log_info('creating the interface kit')
  		device = InterfaceKit()
	except RuntimeError as e:
  		log_error("Error when trying to create the device: %s" % e.message)

	#This connects to the device.
	try:
 		#print 'connecting to the device!'
  		device.openPhidget()
	except PhidgetException as e:
 		log_warning("Exception when trying to connect %i: %s" % (e.code, e.detail))		
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
	#get the id_val of the device
	dev_id = gen_id_val()

	#Connect to the sensors
	device = connectSensors()

	#loop through and put the data onto the server
	while True:

		sleep(1.5)
		device.setOutputState(0,0)

		#getting the IP here, don't really need to do this after some recent updates
		#ip_addy = get_local_ip('eth0')
		#print "IP is %s"%ip_addy	
		

		sensor_data = checkSensors(device,5)
		#print sensor_data

		response = put_value_change(dev_id,sensor_data,True)


		#Sets some kind of ouput based on the response that is sent back(not used at the time)
		#if response == 0:
			#device.setOutputState(0,1)
	device.closePhidget()


#Only here to block until user keyboard input, which will end the program.
#character = str(raw_input())

#we have to close the phidget after we are done..
#device.closePhidget()
