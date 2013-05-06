#!/usr/bin/python
#
# usage:
#   to run: ./door.py
#   to add users: ./door.py add
#
from __future__ import print_function
import subprocess, serial
from time import sleep
from octopus import Octopus

lock = "/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller-if00-port0"

class Door:
    def __init__(self, seconds=5):
        self.lock = lock
        self.seconds = 5

    def open(self):
	print("opening...")
        p = subprocess.Popen(["cat", self.lock])
        sleep(self.seconds)
        p.terminate()

    def run(self, auth_module):
        while True:
            sleep(1)
            if auth_module():
                self.open()

if __name__ == "__main__":
    door = Door()
    octopus = Octopus("users.txt")
    door.run(octopus)
