#!/usr/bin/python
#
# usage:
#   to run: ./door.py
#   to add users: ./door.py add
#
from __future__ import print_function
import subprocess, serial, sys, os
import time
from time import sleep
from octopus import Octopus
from twython import Twython

unlock = "1 > /sys/class/gpio/gpio17/value"
lock = "0 > /sys/class/gpio/gpio17/value"

CONSUMER_KEY ='2DKmty7tJrdqQEp6K6rbBQ'
CONSUMER_SECRET = 'hTk77aiSsvLaeAwQctWOLV4XOcy138sjRDMxTyo'
ACCESS_KEY = '2248113774-oEbT4i32DwP8qw7Xlu2t3bRWvN1XaPn7XQqUxdP'
ACCESS_SECRET = 'qJlgkMGTrOz46AvwuGzeTz8JMB7dT7BsCl7A85A662EJE'

api = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
os.environ['TZ'] = 'GMT+16'
time.tzset()

class Door:
    def __init__(self, seconds=5):
        self.lock = lock
	self.unlock = unlock
        self.seconds = seconds
	print("here")

    def open(self):
        print("opening...")
	os.popen("echo 1 > /sys/class/gpio/gpio17/value")
	sleep(self.seconds)
        os.popen("echo 0 > /sys/class/gpio/gpio17/value")
	api.update_status(status='Someone entered DSL at '+time.strftime('%H:%M:%S'))

    def run(self, auth_module):
        while True:
            sleep(1)
            if auth_module():
                self.open()

    def add_user(self, auth_module):
        auth_module.add_user()

if __name__ == "__main__":
    door = Door()
    octopus = Octopus("/home/pi/door/dootdoorlock/users.txt")
    print ("running")	
    if len(sys.argv) == 2: 
        if sys.argv[1] == "add":
            door.add_user(octopus)
        elif sys.argv[1] == "open":
            door.open()
    else:
        door.run(octopus)

