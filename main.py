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