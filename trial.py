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
