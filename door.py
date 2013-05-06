#!/usr/bin/python
#
# usage:
#   to run: ./door.py
#   to add users: ./door.py add
#
from __future__ import print_function
import subprocess, serial, sys
from time import sleep
from octopus import Octopus

lock = "/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller-if00-port0"

class Door:
    def __init__(self, seconds=5):
        self.lock = lock
        self.seconds = seconds

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

    def add_user(self, auth_module):
        auth_module.add_user()

if __name__ == "__main__":
    door = Door()
    octopus = Octopus("users.txt")

    if len(sys.argv) == 2: 
        if sys.argv[1] == "add":
            door.add_user(octopus)
    else:
        door.run(octopus)

