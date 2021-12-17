import cv2
from pyzbar.pyzbar import decode
import time
import winsound
import datetime

cap = cv2.VideoCapture('img_data/slow1_with_light.h264')
scanned_code_list = []
scanned_data_dict: dict[str, datetime.datetime] = {}  # key: code, value: last detection
# csv = open("scanned_QRcodes.csv", "w")
camera = True
square = 200
scale_percent = 70  # percent of original size

while camera == True:
    ret, frame = cap.read()
    frame = cv2.bitwise_not(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # frame = cv2.blur(frame, (3,3))
    # ret, thresh1 = cv2.threshold(frame, 0, 255, cv2.THRESH_TOZERO)

    # thresh1 = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 97, 43)
    thresh1 = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                cv2.THRESH_BINARY, 11, 7)

    x = int(time.time())

    for code in decode(thresh1):
        mycode = code.data.decode("utf-8")

        if mycode not in scanned_code_list:
            print(mycode)
            scanned_code_list.append(mycode)
            # csv.write("{},{}\n".format(datetime.datetime.now(), mycode))
            scanned_data_dict["mycode"] = x
            # csv.flush()

        elif mycode in scanned_code_list and x - scanned_data_dict["mycode"] > 5:
            scanned_data_dict.update(
                {"mycode": x})  # clearing the list will rewrite the dict as it's going to get scanned again
            scanned_code_list.clear()
            continue

        else:
            continue

    cv2.imshow("QR_Scanner", frame)
    cv2.imshow("QR_Scanner thresh", thresh1)
    cv2.waitKey(1)
print(scanned_data_dict)
