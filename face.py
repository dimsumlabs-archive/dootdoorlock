#!/usr/bin/env python2
import SimpleCV as scv
from SimpleCV.Features import FaceRecognizer
import numpy as np
import itertools, os, sys, time

class Face:
    def __init__(self):
        self.picsdir = "data/all"
        self.interval_seconds = 0.1
        self.camera_id = 0
        self.cam = scv.Camera(self.camera_id)
        self.face_recognizer = FaceRecognizer()
        self.filename = "trainingsdata.xml"
        self.threshold = 1000               # tolerance for NN classifier

    def auth_user(self):
        name, dist = self.face_recognizer.predict(self.cam.getImage())
        print("{0}: {1}".format(name, dist))
        return True if dist < 1000 else False

    def load(self):
        self.face_recognizer.load(self.filename)
    
    def train(self):
        sets = os.listdir(self.picsdir)
        labels, imgs = [], []
        for s in sets:
            print(s)
            i = scv.ImageSet("{0}/{1}".format(self.picsdir,s))
            labels += ["".join([c for c in s if c.isalnum()])] * len(i)
            imgs += i
       
        self.face_recognizer.train(imgs, labels)
        self.face_recognizer.save(self.filename)

    def add_user(self):
        def prompt():
            print("Please enter name for new user and press return.")
            return raw_input()
        name = prompt()
        while os.path.exists("{0}/{1}".format(self.picsdir, name)):
            print("User '{0}' exists, please use a different\
                    name.".format(name))
            name = prompt()

        mkdir("{0}/{1}".format(self.picsdir, name))

        self.shoot_user(30, name)

    def shoot_user(self, npics, name):
        n = 0
        n_taken = 0
        while n_taken < npics:
            fname = "{0}/{1}/{2}.jpg".format(self.picsdir, name, str(n).zfill(4))
            if not os.path.exists(fname):
                print('taking pic number {0}'.format(n_taken + 1))
                self.save_raw(fname)
                n_taken += 1
                time.sleep(self.interval_seconds)
            n += 1

    def save_raw(self, fname):
        self.cam.getImage().save(fname)

def mkdir(name):
    try: 
        os.mkdir(name)
    except OSError:
        pass

def take_pic(fname):
    img = prepare(cam.getImage())
    img.save(fname)

def find_face(img):
    for n in ["", "2", "3", "4"]:
        face = img.findHaarFeatures("face{0}.xml")
        if len(face) == 1:
            img = face[0].crop()
            break
    return img

def find_eyes(img):
    try:
        re = img.findHaarFeatures("lefteye.xml")[0]
        le = img.findHaarFeatures("right_eye.xml")[0]
    except:
        return img
    lec = le.coordinates()
    rec = re.coordinates()
    print(lec, rec)
    angle = np.arctan(float(lec[1] - rec[1]) / (lec[0] - rec[0])) * 180 / np.pi
    center = (lec + rec) / 2.0
    return img.rotate(angle, point=center)

def prepare(img):
    img = find_face(img)
    img = find_eyes(img)
    img = find_face(img)
    return img.grayscale()



def main():
    f = Face()
    f.add_user()
    f.train()
    f.auth_user()

if __name__ == "__main__":
    main()
