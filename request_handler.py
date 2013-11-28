#A hanlder for putting data to the aggregator node
import urllib2
import httplib
import requests
from datetime import datetime
import time as time
import json
import socket
from logging_framework import *
from client_mq_handler import send_json

agg_add='https://thicketagg-paulscloud.rhcloud.com/'

#puts a value change onto the server
def put_value_change(phidget_id, sensor_data, rest):
	url='https://thicketagg-paulscloud.rhcloud.com/data'
	headers = {'content-type':'application/json'}
	temp_data = {
		         'phid':phidget_id,
		     }

	for item in sensor_data:
		temp_data[item] = sensor_data[item]
 	
 	print temp_data

	try:
		if rest:
			temp_data=json.dumps(temp_data)
			the_request = requests.post(str(url), data=temp_data, headers=headers)
			print 'Response:%s'%the_request.text
			#return parse_response(the_request.text)
		else:
#			the_request = send_json(temp_data,5505,False,True)
			print 'Response:%s'%the_request
#			print the_request

#			log_info('Response:%s'%the_request.text)	
	except:
		pass


def parse_response(response):
	if response == '_data_put':
		print '_data_put'
	else:
		loaded = json.loads(response)
		response_dict =  loaded[0]
		print response_dict
		#date = json.loads(response_dict['date'])
		#date = datetime.fromtimestamp(date['$date'])
		response = response_dict['response']
		print response
		if response['identify']:
			return 0
			#print 'ID yourself!'
			#device = InterfaceKit()
			#device.openPhidget()
			#device.setOutputState(0,1)	

#Function that registeres the device, will return a JSON object if the device has not been registered, 1 if registration
#has been sucessful, 2 if the device has already been registered.
#Data looks like:
#reg_info:

def register_device(ip_address, dev_id):
	#reg_info = {
			#'ipaddress':str(ip_address),
			#'devid':str(dev_id),
			#'d':datetime.now().day,
                        #'y':datetime.now().year,
                        #'month':datetime.now().month,
                        #'h':datetime.now().hour,
                        #'min':datetime.now().minute,
		#}
	reg_info = {
			'min':'hiii',
		}


	headers = {'content-type':'application/json'}
        temp_data = {
                         
			 'ipaddress':ip_address,
			 'devid':dev_id,
			 'd':datetime.now().day,
                         'y':datetime.now().year,
                         'month':datetime.now().month,
                         'h':datetime.now().hour,
                         'min':datetime.now().minute,
                         's':datetime.now().second,
                         #'ms':int(round(time_.time()*1000)), 
                         #'val':'10',
                         #'phid':'123',
                         #'sensid':'0',
                     }

	
	#print temp_data
	
	temp_data=json.dumps(temp_data)

        the_request = requests.put(str('http://%s/devices/register'%agg_add), data=temp_data, headers=headers)
        log_info('Register_device response:%s'%the_request.text)
