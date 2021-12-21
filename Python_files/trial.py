#
# import cv2
# from pyzbar.pyzbar import decode
# import time
# import winsound
# import datetime
# from matplotlib import pyplot as plt
#
# cap = cv2.VideoCapture('videos/video_9.h264')
# while True:
#     ret, frame = cap.read()
#     frame = cv2.bitwise_not(frame)
#     # frame = cv2.medianBlur(frame,5)
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     thresh = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
#                                    cv2.THRESH_BINARY, 11, 2)
#     ret, thresho = cv2.threshold(thresh, 60, 255, cv2.THRESH_OTSU)
#
#     for code in decode(thresho):
#         mycode = code.data.decode("utf-8")
#         winsound.Beep(500, 500)
#
#         print(mycode + '    ', datetime())
#
#     cv2.imshow('frame', frame)
#     cv2.imshow('thresh', thresho)
#     cv2.waitKey(1)

#
#
# import cv2 as cv
# import cv2.cv2
# import numpy as np
# from matplotlib import pyplot as plt
# cap = cv2.cv2.VideoCapture('img_data/slow1_with_light.h264')
# while True:
#     ret, img = cap.read()
#     img = cv2.bitwise_not(img)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
#     th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
#                 cv.THRESH_BINARY,11,2)
#     th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
#                 cv.THRESH_BINARY,11,2)
#     titles = ['Original Image', 'Global Thresholding (v = 127)',
#                 'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
#     images = [img, th1, th2, th3]
#     for i in range(4):
#         plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
#         plt.title(titles[i])
#         plt.xticks([]),plt.yticks([])
#     plt.show()
import os

import cv2
from pyzbar.pyzbar import decode
import time
import winsound
import datetime

import cv2

detected_location = r"C:\Users\opv-operator\Desktop\QR_Reader\Deteced"
undetected_location = r"C:\Users\opv-operator\Desktop\QR_Reader\undetected"
cap = cv2.VideoCapture('avivideos/sunlight8.avi')
# Get the frames per second
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
# Get the total numer of frames in the video.
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
# fps1 = cap.get(5)
# fr1 = cap.get(7)
# print(fps1, fr1)
print(frame_count)
no_detected_frames = 0
detected_frames = []
dictionary_of_Boolean = {}

frame_number = 0
# cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)  # optional

while True:  # and frame_number <= frame_count:
    # cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    ret, frame = cap.read()
    frame_number += 1
    dictionary_of_Boolean[frame_number] = 0
    frame = cv2.bitwise_not(frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # frame = cv2.blur(frame, (3,3))
    # ret, thresh1 = cv2.threshold(frame, 0, 255, cv2.THRESH_TOZERO)
    thresh1 = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 31, 7)
    # thresh1 = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
    #                             cv2.THRESH_BINARY, 21, 5)
    ret, thresh1 = cv2.threshold(thresh1, 0, 255, cv2.THRESH_OTSU)
    #
    x = int(time.time())
    code = decode(thresh1)
    print('frame number:', frame_number)
    if code:
        dictionary_of_Boolean[frame_number] = 'Detected'
        detected_frames.append(frame_number)
        no_detected_frames += 1
        print(code, 'at', frame_number)
        cv2.imwrite(os.path.join(detected_location, "frame%d.jpg" % frame_number), frame)

    else:
        print("this frame is not decoded")
        cv2.imwrite(os.path.join(undetected_location, "frame%d.jpg" % frame_number), frame)
    # for code in decode(thresh1):
    #     code = code.data.decode("utf-8")
    #     print(code, 'at',frame_number)
    #
    #     if code:
    #         dictionary_of_Boolean[frame_number] = 'Detected'
    #         detected_frames.append(frame_number)
    #         no_detected_frames += 1
    #         print('hey!!')
    #
    #     else:
    #         print("this frame is not decoded")

    with open('metrics.csv', 'a') as csv:
        csv.write('{},{}\n'.format(frame_number, dictionary_of_Boolean[frame_number]))
        csv.flush()
    print(no_detected_frames)

    cv2.imshow("QR_Scanner", frame)
    cv2.imshow("QR_Scanner thresh", thresh1)
    cv2.waitKey(1)
