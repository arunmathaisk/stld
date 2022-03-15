# This code is Authored By Arun Mathai S.K.
# Website : https://arunmathaisk.in

import os
import requests
import sys

LAB_NUMER = sys.argv[1]

SERVER_IP = sys.argv[2]

STATUS_ENDPOINT = "/status.php"

PAYLOAD_ENDPOINT = "/payload.php"

ARGUMENT_URL = "?lab_number=" + LAB_NUMER

STATUS_URL = SERVER_IP + STATUS_ENDPOINT + ARGUMENT_URL

PAYLOAD_URL = SERVER_IP + PAYLOAD_ENDPOINT + ARGUMENT_URL

RESPONSE_COMMAND = requests.get(STATUS_URL)

if(RESPONSE_COMMAND.text=='shutdown'):
	os.system("/usr/sbin/shutdown -h now")

if(RESPONSE_COMMAND.text=='reboot'):
	os.system("/usr/sbin/reboot")

if(RESPONSE_COMMAND.text=='payload'):
	PAYLOAD_RESPONSE_COMMAND = requests.get(PAYLOAD_URL)
	os.system(RESPONSE_COMMAND.text)
