#!/usr/bin/python
#
# usage:
#   to run: ./octopus.py
#
from __future__ import print_function
import shutil, json, os, re, subprocess, serial, signal, sys
from hashlib import sha256 as hashfun
from time import sleep, ctime

reader = "/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0"
bkpdir = "bkp"

try:
    os.mkdir(bkpdir)
except OSError:
    pass

class Octopus:
    def __init__(self, userfilename, baudrate=9600):
        self.ser = serial.Serial(reader, baudrate)
        self.userfilename = userfilename
        self.users = self.read_users()

    def read_users(self):
        return json.load(open(self.userfilename))

    def backup(self):
        shutil.copy(self.userfilename, "bkp/{0}.txt".format(ctime())) 

    def save_users(self):
        self.backup()
        json.dump(self.users, open(self.userfilename, 'w'), indent=2)
        print("Saved users")

    def add_user(self):
        print("Enter name (lastname firstname) of user to add then press enter.")
        name = raw_input()
        print("Now scan octopus card.")
        key = self.read_user()
        if name in self.users:
            print("{0} is already in database. To overwrite type: y".format(name))
            if raw_input().lower() != "y":
                print("not adding")
                return
        self.users[name] = key
        self.save_users()

    def rm_user(self, name):
        self.users.pop(name)
        self.save_users()

    def read_user(self):
        return hashfun(re.sub("[^0-F]", "", self.ser.readline())).hexdigest()

    def __call__(self):
        return self.read_user() in self.users.values()

if __name__ == "__main__":
    octo = Octopus("users.txt")
    if sys.argv[1] == "add":
        octo.add_user()
    elif sys.argv[1] == "rm":
        octo.rm_user(sys.argv[2])
    else:
        test = octo()
        print("testing, output of call is: {0}".format(test))
