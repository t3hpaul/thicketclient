#A hanlder for putting data to the aggregator node
import urllib2
import httplib
import requests
from datetime import datetime
import time as time
import json
import socket
from logging_framework import *
import logging

agg_add='https://thicketagg-paulscloud.rhcloud.com/'

logname = 'thicket.log'
logging.basicConfig(filename=logname,
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.INFO)

#puts a value change onto the server
def put_value_change(phidget_id, sensor_data, rest):
	url='https://thicketagg-paulscloud.rhcloud.com/data'
	headers = {'content-type':'application/json'}
	temp_data = {
		         'phid':phidget_id,
		     }

	for item in sensor_data:
		temp_data[item] = sensor_data[item]
 	
 	logging.info(temp_data)

	try:
		if rest:
			temp_data=json.dumps(temp_data)
			the_request = requests.post(url, data=temp_data, headers=headers)
			#logging.info(the_request.text)
			#return parse_response(the_request.text)
		else:
			pass
			
	except:
		pass


def parse_response(response):
	if response == '_data_put':
		print '_data_put'
	else:
		loaded = json.loads(response)
		response_dict =  loaded[0]
		logging.info(response_dict)
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
	pass
