from picamera.array import PiRGBArray
from picamera import PiCamera
from pyzbar.pyzbar import decode
import datetime

import cv2
import time



camera = PiCamera()
camera.resolution = (640,480)
camera.framerate = 32
PiCamera.shutter_speed = 10000
PiCamera.awb_mode = 'off'
rawCapture = PiRGBArray(camera)
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format = 'bgr', use_video_port=True):
    image = frame.array
    frame_crop = cv2.bitwise_not(image)
    frame_crop = cv2.cvtColor(frame_crop, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(frame_crop, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    
    for code in decode(thresh):
        mycode = code.data.decode("utf-8")
        print(mycode + '  ',  time.time())

    cv2.imshow('frame' , image)
    cv2.imshow('frame Crop' , thresh)
    key = cv2.waitKey(1) & 0xFF
    rawCapture.truncate(0)
    
    if key == ord('q'):
        break