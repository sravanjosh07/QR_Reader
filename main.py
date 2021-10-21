import cv2
from pyzbar.pyzbar import decode
import time
import winsound

cap = cv2.VideoCapture(1)
scanned_codes = []

camera = True

while camera == True:
    ret, frame = cap.read()
    frame = cv2.bitwise_not(frame)
    frame = frame[:200, :200]

    for code in decode(frame):
        mycode = code.data.decode("utf-8")
        if mycode not in scanned_codes:
            print(mycode)
            scanned_codes.append(mycode)
            winsound.Beep( 500, 500)
            time.sleep(5)
        elif mycode in scanned_codes:
            print(mycode)
            winsound.Beep(1000, 1000)
            time.sleep(5)
        else:
            pass

    cv2.imshow("QR_Scanner", frame)
    cv2.waitKey(1)
