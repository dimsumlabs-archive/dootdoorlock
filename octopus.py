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

class Octopus:
    def __init__(self, userfilename, baudrate=9600):
        reader ="/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0"
        self.ser = serial.Serial(reader, baudrate)
        self.userfilename = userfilename
        self.users = read_users()

    def read_users(self):
        users = dict()
        with open(self.userfilename) as userfile:
            for line in userfile:
                name, key = line.strip("\n").rsplit(" ", 1)
                users[name] = key
        return users

    def save_users(self):
        with open(userdata, 'w') as userfile:
            for name in sorted(users):
                print("{0} {1}".format(name, users[name]), file=userfile)
        print("Saved users")

    def add_user(self):
        #self.users = self.read_users()
        print("Enter name (lastname firstname) of user to add then press enter.")
        name = raw_input()
        print("Now scan octopus card.")
        key = self.read_user()
        if name in users:
            print("{0} is already in database. To overwrite type: y".format(name))
            if raw_input().lower() != "y":
                print("not adding")
                return
        self.users[name] = key
        save_users()

    def read_user(self):
        return hashfun(re.sub("[^0-F]", "", ser.readline())).hexdigest()

    def authfun(self):
        return self.read_user() in self.users.values()


    #def run():
    #    users = read_users()
    #    while True:
    #        key = read_user()
    #        if key in users.values():
    #            print("Opening")
    #            open_door()

if __name__ == "__main__":
    octo = Octopus("users.txt")
