
import cv2
from pyzbar.pyzbar import decode
import time
import winsound
import datetime
from matplotlib import pyplot as plt

cap = cv2.VideoCapture(0)
scanned_code_list = []
scanned_data_dict: dict[str, datetime.datetime] = {}  # key: code, value: last detection
# csv = open("scanned_QRcodes.csv", "w")
camera = True
square = 200
scale_percent = 70  # percent of original size



while camera == True:
    ret, frame = cap.read()
    '''
    scaling the frame, because opencv cant show large images in a single window'''
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    
    # resize image
    frame = cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)
    frame = frame#[-square:, int(frame.shape[1]/2-square/2):int(frame.shape[1]/2+square/2)]
    frame = cv2.bitwise_not(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #frame = cv2.GaussianBlur(frame, (5, 5), 0)
    th0 = frame


#Adaptive thresholding
    th2 = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY, 11, 2)
    th3 = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)
    ret, th1 = cv2.threshold(frame, 127, 255, cv2.THRESH_BINARY)

    ret, th4 = cv2.threshold(frame, 60, 255, cv2.THRESH_OTSU)

    # cv2.imshow('Global thresholding', th1)
    # cv2.imshow('Adaptive Mean Thresholding', th2)
    # cv2.imshow('Adaptive Gaussian Thresholding', th3)
    # cv2.imshow('OTSU', th4)
    list1 = [th0, th1, th2, th3, th4]
    x = int(time.time())
    for img in list1:
        for code in decode(img):
            mycode = code.data.decode("utf-8")
            if mycode not in scanned_code_list:
                print(mycode)
                scanned_code_list.append(mycode)
                # csv.write("{},{}\n".format(datetime.datetime.now(), mycode))
                scanned_data_dict["mycode"] = x
                # csv.flush()
                winsound.Beep(500, 500)

            elif mycode in scanned_code_list and x - scanned_data_dict["mycode"] > 5:
                scanned_data_dict.update({"mycode": x}) #clearing the list will rewrite the dict as it's going to get scanned again
                scanned_code_list.clear()
                continue

    cv2.imshow("QR_Scanner_thresh", frame)
    cv2.waitKey(1)
print(scanned_data_dict)

