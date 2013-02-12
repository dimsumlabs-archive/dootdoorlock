#!/usr/bin/python
#
# TODO: easily add users
# 
# To keep running once the ssh connections terminates: 
#     nohup ./door.py &
#
# Add users:
# start python shell and execute:
# 	 import door
# 	 users, keys = door.read_users("users.txt")
# 	 door.add_user(users, keys, "Lastname  Firstname", door.read_user())
# then go beep your card
# restart ./door.py
#
from __future__ import print_function
import re, subprocess, serial, sys
from hashlib import sha256 as hashfun
from time import sleep

octopus_reader ="/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0"
doorlock = "/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller-if00-port0"
ser = serial.Serial(octopus_reader, 9600)
userdata = "users.txt"

def read_users(fname):
    users, keys = dict(), dict()
    with open(fname) as userfile:
        for line in userfile:
	    name, key = line.strip("\n").rsplit(" ", 1)
            users[name] = key
            keys[key] = name
    return users, keys

def save_users(users):
    with open(userdata, 'w') as userfile:
        for name in sorted(users):
            print("{0} {1}".format(name, users[name]), file=userfile)
    print("Saved users")

def add_user(users, keys, name, key):
    if name in users:
        print("{0} is already in database. To overwrite type: y".format(name))
        if raw_input().lower() != "y":
	    print("not adding")
            return
    users[name] = key
    keys[key] = name
    save_users(users)

def open_door():
    p = subprocess.Popen(["cat", doorlock])
    sleep(5)
    p.terminate()

def read_user():
    return hashfun(re.sub("[^0-F]", "", ser.readline())).hexdigest()

if __name__ == "__main__":
    users, keys = read_users("users.txt")
    while True:
	key = read_user()
	if key in keys:
            print("Opening for {0}".format(keys[key]))
	    open_door()
