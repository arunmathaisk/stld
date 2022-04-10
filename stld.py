# This code is Authored By Arun Mathai S.K.
# Website : https://arunmathaisk.in

import os
import requests
import sys

LAB_NUMER = sys.argv[1]

SERVER_IP = sys.argv[2]

STATUS_ENDPOINT = "/status"

ARGUMENT_URL = "/" + LAB_NUMER

STATUS_URL = SERVER_IP + STATUS_ENDPOINT + ARGUMENT_URL

RESPONSE_COMMAND = requests.get(STATUS_URL)

if(RESPONSE_COMMAND.text=='shutdown'):
	os.system("/sbin/shutdown -h now")
	os.system("/usr/sbin/shutdown -h now")
