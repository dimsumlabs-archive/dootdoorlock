#!/usr/bin/python
#
# usage:
#   to run: ./door.py
#   to add users: ./door.py add
#
from __future__ import print_function
import subprocess, serial, sys, os, time, ConfigParser, twython
from time import sleep
from octopus import Octopus

unlock = "1 > /sys/class/gpio/gpio17/value"
lock = "0 > /sys/class/gpio/gpio17/value"

os.environ['TZ'] = 'GMT+16'
time.tzset()

config_parser = ConfigParser.SafeConfigParser()
config_parser.read('api.cfg')
api_config = {}
try:
    api_config = dict(config_parser.items('Twitter'))
except ConfigParser.NoSectionError:
    pass
api = twython.Twython(**api_config)

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
        try:
            api.update_status(status='Someone entered DSL at '+time.strftime('%H:%M:%S'))
        except Exception as error:
            print(error.message)

    def run(self, auth_module):
        while True:
            sleep(1)
            if auth_module():
                self.open()

    def add_user(self, auth_module):
        auth_module.add_user()

if __name__ == "__main__":
    door = Door()
    octopus = Octopus("users.txt")
    print ("running")	
    if len(sys.argv) == 2: 
        if sys.argv[1] == "add":
            door.add_user(octopus)
        elif sys.argv[1] == "open":
            door.open()
    else:
        door.run(octopus)

