# # #
# # #
# # # from imutils.video import VideoStream
# # # from pyzbar import pyzbar
# # # import argparse
# # # import datetime
# # # import imutils
# # # import time
# # # import cv2
# # #
# # # ap = argparse.ArgumentParser()
# # # ap.add_argument("-o", "--output", type = str, default="barcodes.csv", help = "path to output CSF file containing barcodes")
# # # args = vars(ap.parse_args())
# # # cap = VideoStream(src=1).start()
# # # time.sleep(2.0)
# # # csv = open(args["output"], "w")
# # # found = set()
# # #
# # # while True:
# # #     frame = cap.read()
# # #     frame = cv2.bitwise_not(frame)
# # #     frame = frame[:200, :200]
# # #     barcodes = pyzbar.decode(frame)
# # #     for barcode in barcodes:
# # #         barcodeData = barcode.data.decode("utf-8")
# # #         if barcodeData not in found:
# # #             csv.write("{},{}\n".format(datetime.datetime.now(), barcodeData))
# # #             csv.flush()
# # #             found.add(barcodeData)
# # #
# # #     cv2.imshow("BarcodeScanner", frame)
# # #     key = cv2.waitKey(1)& 0xFF
# # #     if key == ord("q"):
# # #         break
# # #
# # #
# # # print("[INFO] cleaning up...")
# # # csv.close()
# # # cv2.destroyAllWindows()
# # # vs.stop()
# # #
# # # import cv2
# # # import numpy as np
# # # from pyzbar.pyzbar import decode
# # # import playsound
# # # import csv
# # # lst = []
# # # data = dict()
# # #
# # # def beep():
# # #     playsound._playsoundWin("beep sound.wav")
# # #
# # # def check(file):
# # #     code=decode((file))
# # #     if code == []:
# # #         #No Barcode
# # #         return False
# # #     #Yes Barcode
# # #     return True
# # #
# # # def take_snaps(cap):
# # #     for i in range(10):
# # #         ret, frame = cap.read()
# # #         cv2.imwrite()
# # #
# # #
# # #
# # #
# # # cap = cv2.VideoCapture(1)
# # #
# # # while True:
# # #     ret, frame = cap.read()
# # #     frame = cv2.bitwise_not(frame)
# # #     frame = frame[:200, :200]
# # #     for barcode in decode(frame):
# # #         if barcode != []:
# # #             myData = barcode.data.decode('utf-8')
# # #             lst.append(myData)
# # #             break
# # #         # checking1 = check(frame)
# # #         # if myData not in lst:
# # #         #
# # #         # else:
# # #         #     pass
# # #         # if checking1 == True:
# # #         #     break
# # #
# # #
# # # # >>>>>>> 6b6d8848df9bc0275c6745e6101a4c7a603b9bd0
# # #     cv2.imshow('results', frame)
# # #     cv2.waitKey(1)
# # #
# # #     print(lst)
# # #
# # import csv
# # # csv = open("scanned_code_list.csv", "w")
# # # list2 = [1,2,3,4,5,6,7,8]
# # # for num in list2:
# # #     csv.write("%d num")
# # #
# # # print(csv)
# #
# # import cv2
# # from pyzbar.pyzbar import decode
# # import time
# # import winsound
# # import datetime
# # import csv
# #
# # cap = cv2.VideoCapture(0)
# # scanned_code_list = []
# # scanned_data_dict = {"code":["time"]}
# # csv = open("scanned_QRcodes.csv", "w")
# # camera = True
# # square = 200
# #
# # while camera == True:
# #     ret, frame = cap.read()
# #
# #     frame_crop = frame[-200:, int(frame.shape[1]/2-square/2):int(frame.shape[1]/2+square/2)]
# #     frame_crop = cv2.bitwise_not(frame_crop)
# #     frame_crop = cv2.cvtColor(frame_crop, cv2.COLOR_BGR2GRAY)
# #     ret, frame_crop = cv2.threshold(frame_crop, 0, 255, cv2.THRESH_OTSU)
# #
# #     cv2.imshow("QR_Scanner thresh", frame_crop)
# #     if decode(frame_crop) != []:
# #
# #         for code in decode(frame_crop):
# #             mycode = code.data.decode("utf-8")
# #             if mycode not in scanned_code_list:
# #                 print(mycode)
# #                 scanned_code_list.append(mycode)
# #                 csv.write("{},{}\n".format(datetime.datetime.now(), mycode))
# #                 csv.flush()
# #                 x = time.time()
# #                 # winsound.Beep(500, 500)
# #                 # time.sleep(0.5)
# #             elif mycode in scanned_code_list:
# #                 continue
# #
# #
# #             # else:
# #             #     scanned_code_list.clear()
# #     elif decode(frame_crop) == []:
# #         scanned_code_list.clear()
# #
# #     frame = cv2.rectangle(
# #         frame,
# #         (int(frame.shape[1]/2-square/2), frame.shape[0]-square),
# #         (int(frame.shape[1]/2+square/2), frame.shape[0]),
# #         (0, 255, 0),
# #         thickness=3)
# #     cv2.imshow("QR_Scanner", frame)
# #     cv2.waitKey(1)
# #     # print(scanned_code_list)
# #
# # # elif mycode in scanned_code_list:
# # # continued_code = decode(frame_crop)
# # # if mycode == continued_code:
# # #     continue
# # # else:
# # #     scanned_code_list.clear()
#
# import datetime
# # import time
# # l = []
# #
# # for i in range(10):
# #     now = time.time()
# #     l.append(now)
# #
# #
# # print(l)
#
# import cv2
# from pyzbar.pyzbar import decode
# import time
# import winsound
# import datetime
#
# cap = cv2.VideoCapture(0)
# scanned_codes = []
# scanned_data_dict: dict[str, time.time()] = {}  # key: code, value: last detection
# csv = open("scanned_QRcodes.csv", "w")
# camera = True
# square = 200
#
# while camera == True:
#     ret, frame = cap.read()
#
#     frame_crop = frame[-200:, int(frame.shape[1]/2-square/2):int(frame.shape[1]/2+square/2)]
#     frame_crop = cv2.bitwise_not(frame_crop)
#     frame_crop = cv2.cvtColor(frame_crop, cv2.COLOR_BGR2GRAY)
#     ret, frame_crop = cv2.threshold(frame_crop, 0, 255, cv2.THRESH_OTSU)
#
#     cv2.imshow("QR_Scanner thresh", frame_crop)
#
#     now = datetime.datetime.now()
#     x = int(time.time())
#
#     for code in decode(frame_crop):
#         mycode = code.data.decode("utf-8")
#
#
#         if mycode not in scanned_codes:
#             print(mycode)
#             scanned_codes.append(mycode)
#             csv.write("{},{}\n".format(datetime.datetime.now(), mycode))
#             scanned_data_dict["mycode"] = x
#             csv.flush()
#
#             winsound.Beep(500, 500)
#             time.sleep(0.5)
#         # elif mycode == []:
#         #     scanned_code_list.clear()
#         elif mycode in scanned_codes and x - scanned_data_dict["mycode"] > 5:
#             # print(mycode)
#             scanned_codes.clear()
#             continue
#         else:
#             continue
#         #
#         # elif mycode == []:
#         #     scanned_code_list.clear()
#         # else:
#         #     scanned_code_list.clear()
#
#     frame = cv2.rectangle(
#         frame,
#         (int(frame.shape[1]/2-square/2), frame.shape[0]-square),
#         (int(frame.shape[1]/2+square/2), frame.shape[0]),
#         (0, 255, 0),
#         thickness=3)
#     cv2.imshow("QR_Scanner", frame)
#     cv2.waitKey(1)
# print(scanned_data_dict)
#     # print(scanned_code_list)
#
# import cv2
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, img  = cap.read()
#     img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#     cv2.imshow("frame", img)
#     cv2.waitKey(0)



# import cv2
# import numpy as np
#
# # Create a VideoCapture object and read from input file
# # If the input is the camera, pass 0 instead of the video file name
# cap = cv2.VideoCapture('videos/video_4.h264')
#
# # Check if camera opened successfully
# if (cap.isOpened()== False):
#   print("Error opening video stream or file")
#
# # Read until video is completed
# while(cap.isOpened()):
#   # Capture frame-by-frame
#   ret, frame = cap.read()
#   if ret == True:
#
#     # Display the resulting frame
#     cv2.imshow('Frame',frame)
#
#     # Press Q on keyboard to  exit
#     if cv2.waitKey(25) & 0xFF == ord('q'):
#       break
#
#   # Break the loop
#   else:
#     break
#
# # When everything done, release the video capture object
# cap.release()
#
# # Closes all the frames
# cv2.destroyAllWindows()

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
    # frame = cv2.bitwise_not(frame)
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


    frame_crop = frame#[-square:, int(frame.shape[1]/2-square/2):int(frame.shape[1]/2+square/2)]
    # frame_crop = cv2.bitwise_not(frame_crop)
    # frame_crop = cv2.cvtColor(frame_crop, cv2.COLOR_BGR2GRAY)

    ret, frame_crop = cv2.threshold(frame_crop, 60, 255, cv2.THRESH_OTSU)

    kernelx = np.array([[-1, 0, +1],
                       [-2, 0, +2],
                       [-1, 0, +1]])
    gradX = cv2.filter2D(frame_crop, -1, kernelx)

    kernely = np.array([[-1, -2, -1],
                       [0, 0, 0],
                       [+1, +2, -1]])
    gradY = cv2.filter2D(frame_crop, -1, kernely)

    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)

    #blurring
    blurred = cv2.blur(gradient, (5,5))
    (_, thresh) = cv2.threshold(blurred, 20, 180, cv2.THRESH_BINARY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (40, 25))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    closed = cv2.erode(closed, None, iterations = 2)
    closed = cv2.dilate(closed, None, iterations = 2)

    cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for cnt in cnts:
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)  # approx is a three dimensional array of vertices
        shape = np.shape(approx)
        # finding area of the contour so we can consider contours having area greater than 7000 sq.pixels
        area = cv2.contourArea(cnt)

        if area >=35000 and area <= 42250 and shape[0] == 4:
            rect = cv2.minAreaRect(cnt)
            # box = cv2.cv.BoxPoints(rect) if imutils.is_cv2() else cv2.boxPoints(rect)
            # box = np.int0(box)
            # cv2.drawContours(image, [box], -1, (0, 255, 0), 3)
            x, y, w, h = cv2.boundingRect(cnt)

            # ROI = image[y :y + h, x:x + w]
            ROI = image[y - 50:y + h + 50, x - 50:x + w + 50]
            print(area)
            image1 = cv2.imread('ROI')
            gray1 = cv2.cvtColor(ROI, cv2.COLOR_BGR2GRAY)
            gra = cv2.bitwise_not(frame_crop)
            ret, thresh1 = cv2.threshold(gray1, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
            msg = decode(thresh1)
            print(msg)

            cv2.imshow("ROI", thresh1)
    cv2.imshow('frame', frame_crop)
    cv2.waitKey(0)





    x = int(time.time())
    for code in decode(frame_crop):
        mycode = code.data.decode("utf-8")
        winsound.Beep(500, 500)
        print(mycode)

        # if mycode not in scanned_code_list:
        #     print(mycode)
        #     scanned_code_list.append(mycode)
        #     # csv.write("{},{}\n".format(datetime.datetime.now(), mycode))
        #     scanned_data_dict["mycode"] = x
        #     # csv.flush()
        #   #  winsound.Beep(500, 500)
        #
        # elif mycode in scanned_code_list and x - scanned_data_dict["mycode"] > 5:
        #     # scanned_data_dict.update({"mycode": x}) #clearing the list will rewrite the dict as it's going to get scanned again
        #     scanned_code_list.clear()
        #     continue

        # else:
        #     continue

    # frame = cv2.rectangle(
    #     frame,
    #     (int(frame.shape[1]/2-square/2), frame.shape[0]-square),
    #     (int(frame.shape[1]/2+square/2), frame.shape[0]),
    #     (0, 255, 0),
    #     thickness=3)
    # cv2.namedWindow('QR_Scanner', cv2.WINDOW_NORMAL)
    # cv2.namedWindow('QR_Scanner_thresh', cv2.WINDOW_NORMAL)
    # cv2.resizeWindow('QR_Scanner', 600, 600)
    # cv2.resizeWindow('QR_Scanner_thresh', 600, 600)
    cv2.imshow("QR_Scanner", frame)
    cv2.imshow("QR_Scanner_thresh", frame_crop)
    cv2.waitKey(1)
print(scanned_data_dict)

#
# import cv2
# import numpy as np
# import face_recognition
# import time
#
#
# def increase_brightness(img, value=30):
#     hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
#     h, s, v = cv2.split(hsv)
#
#     lim = 255 - value
#     v[v > lim] = 255
#     v[v <= lim] += value
#
#     final_hsv = cv2.merge((h, s, v))
#     img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
#     return img
#
#
# # camera device can be different for your computer. Try to change 0 to 1 or other if you get some error
# video = cv2.VideoCapture(0)
#
# count = 0
# l = []
# while True:
#
#     ret, frame = video.read()
#     frame = increase_brightness(frame, value=100)  # change the brighness as per your requiremens before only more the value more the brightness
#
#     cv2.imshow("frame", frame)
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break