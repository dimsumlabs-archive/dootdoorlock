#!/usr/bin/python
#
# untested and WIP
#
from __future__ import print_function
import os, subprocess
from hashlib import sha512 as hashfun
from time import sleep
b = 'A0B0C0D0E0'
found = 0

octopus_reader ="/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_\
        Controller_0001-if00-port0"
doorlock = "/dev/serial/by-id/usb-usb-Prolific_Technology_Inc._USB-Serial_\
        Controller-if00-port0"

def read_users(fname):
    users, keys = dict(), dict()
    with open(fname) as userfile:
        for line in userfile:
	    name, key = line.rsplit(" ", 1)
            users[name] = key
            keys[key] = name
    return users, keys

def save_users(fname, users):
    with open(fname, 'w') as userfile:
        for name in sorted(users):
            print("{0} {1}".format(name, users[name]), file=userfile)

def add_user(users, keys, name, key):
    if name in users:
        print("{0} is already in database. To overwrite type: y".format(name))
        if raw_input().lower() is not "y":
            return
    users[name] = key
    keys[key] = name

def open_door():
    p = subprocess.Popen("cat {0}".format(doorlock))
    sleep(5)
    p.terminate()

if __name__ == "__main__":
    users, keys = read_users("users.txt")
    print(users,keys)
    #while True:
    #	print("blah")
        #with open(octopus_reader) as reader:
        #    for line in reader:
        #        if hashfun(line) in keys
        #for line in users:
        #    if b in line:
        #        print("FOUND")
        #        found = 1
        #users.close()
        #if found == 0:
        #    print("NOT FOUND.")
        #reader.close()
