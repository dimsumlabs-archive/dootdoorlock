#!/usr/bin/python
#
# TODO: run as daemon
#       maybe with http://pypi.python.org/pypi/python-daemon/
# 
# usage:
#   to run: ./door.py
#   to add users: ./door.py add
#
from __future__ import print_function
import os, re, subprocess, serial, signal, sys
from hashlib import sha256 as hashfun
from time import sleep

octopus_reader ="/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0"
doorlock = "/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller-if00-port0"
ser = serial.Serial(octopus_reader, 9600)
userdata = "users.txt"
pidfile = "/tmp/dootdoorlock.pid"

def read_users(fname):
    users = dict()
    with open(fname) as userfile:
        for line in userfile:
	    name, key = line.strip("\n").rsplit(" ", 1)
            users[name] = key
    return users

def save_users(users):
    with open(userdata, 'w') as userfile:
        for name in sorted(users):
            print("{0} {1}".format(name, users[name]), file=userfile)
    print("Saved users")

def add_user():
    users = read_users(fname)
    print("Enter name (lastname firstname) of user to add then press enter.")
    name = raw_input()
    print("Now scan octopus card.")
    key = read_user()
    if name in users:
        print("{0} is already in database. To overwrite type: y".format(name))
        if raw_input().lower() != "y":
	    print("not adding")
            return
    users[name] = key
    save_users(users)

def open_door():
    p = subprocess.Popen(["cat", doorlock])
    sleep(5)
    p.terminate()

def read_user():
    return hashfun(re.sub("[^0-F]", "", ser.readline())).hexdigest()

def run():
    users = read_users("users.txt")
    while True:
        key = read_user()
    	if key in user.values():
            print("Opening for {0}".format(keys[key]))
            open_door()

def main(argv):
    if len(argv) == 3:
        if argv[2] == "add":
            print("To add user press y followed by enter.")
            while raw_input() == "y":
                add_user()
                print("To add another user press y followed by enter.")
        else if argv[2] == "run":
            run()


    if os.path.isfile(pidfile):
        print("Doorlock already running, I'm killing it.")
        old_pid = int(open(pidfile).read())
        os.kill(pid, signal.SIGKILL)
    
    # nohup prevents the process from dying with the parent shell
    # couldn't test this yet!
    p = subprocess.Popen(["nohup", "python", "door.py", "run"])
    print(p.pid, file=open(pidfile, 'w'))
    print("Running door.py in background.")

if __name__ == "__main__":
    main(sys.argv)
