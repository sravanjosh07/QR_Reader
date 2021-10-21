

from imutils.video import VideoStream
from pyzbar import pyzbar
import argparse
import datetime
import imutils
import time
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-o", "--output", type = str, default="barcodes.csv", help = "path to output CSF file containing barcodes")
args = vars(ap.parse_args())
cap = VideoStream(src=1).start()
time.sleep(2.0)
csv = open(args["output"], "w")
found = set()

while True:
    frame = cap.read()
    frame = cv2.bitwise_not(frame)
    frame = frame[:200, :200]
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        barcodeData = barcode.data.decode("utf-8")
        if barcodeData not in found:
            csv.write("{},{}\n".format(datetime.datetime.now(), barcodeData))
            csv.flush()
            found.add(barcodeData)

    cv2.imshow("BarcodeScanner", frame)
    key = cv2.waitKey(1)& 0xFF
    if key == ord("q"):
        break


print("[INFO] cleaning up...")
csv.close()
cv2.destroyAllWindows()
vs.stop()

import cv2
import numpy as np
from pyzbar.pyzbar import decode
import playsound
import csv
lst = []
data = dict()

def beep():
    playsound._playsoundWin("beep sound.wav")

def check(file):
    code=decode((file))
    if code == []:
        #No Barcode
        return False
    #Yes Barcode
    return True

def take_snaps(cap):
    for i in range(10):
        ret, frame = cap.read()
        cv2.imwrite()




cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    frame = cv2.bitwise_not(frame)
    frame = frame[:200, :200]
    for barcode in decode(frame):
        if barcode != []:
            myData = barcode.data.decode('utf-8')
            lst.append(myData)
            break
        # checking1 = check(frame)
        # if myData not in lst:
        #
        # else:
        #     pass
        # if checking1 == True:
        #     break


# >>>>>>> 6b6d8848df9bc0275c6745e6101a4c7a603b9bd0
    cv2.imshow('results', frame)
    cv2.waitKey(1)

    print(lst)