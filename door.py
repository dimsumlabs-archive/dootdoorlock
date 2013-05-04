#!/usr/bin/python
#
# usage:
#   to run: ./door.py
#   to add users: ./door.py add
#
from __future__ import print_function
import os, re, subprocess, serial, signal, sys
from hashlib import sha256 as hashfun
from time import sleep
from Octopus import Octopus

octopus_reader ="/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0"
ser = serial.Serial(octopus_reader, 9600)
userdata = "users.txt"

class Door:
    def __init__(self, seconds=5):
        self.lock = "/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller-if00-port0"
        self.seconds = seconds

    def open(self):
        p = subprocess.Popen(["cat", doorlock])
        sleep(self.seconds)
        p.terminate()

    def run(self, auth_module):
        while True:
            sleep(1)
            if auth_module():
                self.open()

if __name__ == "__main__":
    door = Door()
    octopus = Octopus()
    door.run(octopus)
