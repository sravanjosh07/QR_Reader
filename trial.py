# # <<<<<<< HEAD
# #
# # from PIL import Image
# # import playsound
# # import cv2
# # from pyzbar.pyzbar import decode
# #
# # def beep():
# #     playsound._playsoundWin("beep sound.wav")
# #
# # def code_decoder(file):
# #     """
# #     This function decodes the QR from an image and returns a string with the number on it
# #     :param file: The image that needs to be read and decoded
# #     :return: A barcode number
# #     """
# #     #Decodes the barcode
# #     code = decode(Image.open(file))
# #     #Incese the scanner cannot read the image.
# #     if code != []:
# #         #Turns the byte type barcode into string
# #         the_code=code.data.decode('utf-8')
# #     else:
# #         return None
# #     return the_code
# #
# #
# # def check(file):
# #     """
# #     The function that checks if the frame has a barcode in it
# #     :param file: the file that needs to be checked
# #     :return: True or False
# #     """
# #     #Decoder
# #     code=decode((file))
# #     if code == []:
# #         #empty string
# #         return False
# #     #for a non empty string
# #     return True
# # def webcam_capture(cap):
# #     """
# #     Function that takes video feed from the webcamera and checks frames for the presence of a barcode.
# #     as soon as a barcode is detected it takes a snapshot of the image and stores it as a file.
# #     :param camera: Camera that does the video taking
# #     :return:
# #     """
# #     #Live video feed
# #
# #     while True:
# #         #Reading the video feed
# #         ret,frame=cap.read()
# #         frame = frame[:200, :200]
# #         if not ret:
# #             break
# #         cv2.imshow('frame',frame)
# #         #Live barcode detection
# #         detection=check(frame)
# #         #Barcode detected
# #         if detection==True:
# #             #Saving an image with the barcode
# #             beep()
# #             cv2.imwrite("QR_instance.png",frame)
# #             #Stop Video Feed
# #             break
# #         #Manual Stop
# #         elif cv2.waitKey(1) & 0xFF == ord ("q"):
# #             break
# #     camera.release()
# #     cv2.imshow("Qr_instance", Qr_instance.png)
# #     cv2.destroyAllWindows()
# #
# # def capture(cap,show=False):
# #     """
# #     Takes a picture of whatever webcam is filming. Mainly there for taking images with webcam.
# #     :param camera: Camera to be used
# #     :return:
# #     """
# #     sub, img = cap.read()
# #
# #
# #     if sub:    # frame captured without any errors
# #         #If the user wants to see the image they take
# #         if show == True:
# #             namedWindow("QR_code",cv2.WINDOW_NORMAL)
# #             imshow("QR_code",img)
# #         waitKey(0)
# #         destroyWindow("QR_code")
# #         name ="QR_instance.png"
# #         imwrite(name,img) #save image
# #
# #
# #
# #
# # cap = cv2.VideoCapture(0)
# #
# # # webcam_capture(cap)
# # # code_decoder(frame)
# #
# #
# #
# # '''
# # take the camera feed, check for the codes.
# # once detected, the data should be written into a dict, list.
# #
# #
# # '''
# #
# # def Is_Qr_Present(cap):
# #     code=decode(cap)
# #     if code == []:
# #         #empty string
# #         return False
# #     #for a non empty string
# #     return True
# #
# # def Qr_capture(cap):
# #     ret, img = cap.read()
# #     cv2.imwrite("captured_frame.jpg", img)
# #     return "captures_frame.jpg"
# #
# # if Is_Qr_Present(cap) == True:
# #     snap = Qr_capture(cap)
# #
# # print(type(snap))
# #
# #
# #
# #
# #
# # =======
# # # import numpy
# # # import cv2
# # # import pyzbar.pyzbar as pyzbar
# # # cv2.namedWindow("preview")
# # # cap = cv2.VideoCapture(0)
# # # # gray = cv2.cvtColor (frame, cv2.COLOR_BGR2GRAY)
# # # HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# # # decodedObjects = pyzbar.decode(HSV)
# # # cv2.imshow("preview", HSV)
# # # if decodedObjects is not None:
# # #     print('data: ', decodedObjects)
# # #
# # # if cv2.waitKey(1) & 0xFF == ord('q'):
# # #     break
# # #
# #
# #
# # # When everything done, release the capture
# #
# # # _detect_pyzbar(frame)
# # # cv2.destroyWindow("preview")
# # # cap.release()
# # # cv2.destroyAllWindows()
# #
# # import cv2
# # import pyzbar.pyzbar as pyzbar
# #
# # cv2.namedWindow("preview")
# # vc = cv2.VideoCapture(0)
# #
# # if vc.isOpened(): # try to get the first frame
# #     rval, frame = vc.read()
# #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# # else:
# #     rval = False
# #
# # while rval:
# #     cv2.imshow("preview", gray)
# #     rval, frame = vc.read()
# #     decodedObjects = pyzbar.decode(gray)
# #     if decodedObjects != []:
# #         print('data: ', decodedObjects)
# #     key = cv2.waitKey(20)
# #     if key == 27: # exit on ESC
# #         break
# #
# # cv2.destroyWindow("preview")
# # vc.release()
# #
# # #
# # # from imutils.video import VideoStream
# # # # from pyzbar import pyzbar
# # # import argparse
# # # import datetime
# # # import imutils
# # # import time
# # # import cv2
# # #
# # #
# # # ap = argparse.ArgumentParser()
# # # ap.add_argument("-o", "--output", type=str, default="barcodes.csv",
# # # 	help="path to output CSV file containing barcodes")
# # # args = vars(ap.parse_args())
# # #
# # # vs = cv2.VideoCapture(0)
# # #
# # # csv = open(args["output"], "w")
# # # found = set()
# # #
# # # # loop over the frames from the video stream
# # # while True:
# # #     # grab the frame from the threaded video stream and resize it to
# # #     # have a maximum width of 400 pixels
# # #     ret, frame = vs.read()
# # #     gray = cv2.cvtColor (frame, cv2.COLOR_BGR2GRAY)
# # #
# # #     # find the barcodes in the frame and decode each of the barcodes
# # #     barcodes = pyzbar.decode(frame)
# # #     # loop over the detected barcodes
# # #     for barcode in barcodes:
# # #     # extract the bounding box location of the barcode and draw
# # #         # the bounding box surrounding the barcode on the image
# # #         (x, y, w, h) = barcode.rect
# # #         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
# # #         # the barcode data is a bytes object so if we want to draw it
# # #         # on our output image we need to convert it to a string first
# # #         barcodeData = barcode.data.decode("utf-8")
# # #         barcodeType = barcode.type
# # #         # draw the barcode data and barcode type on the image
# # #         text = "{} ({})".format(barcodeData, barcodeType)
# # #         cv2.putText(frame, text, (x, y - 10),
# # #                     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
# # #         # if the barcode text is currently not in our CSV file, write
# # #         # the timestamp + barcode to disk and update the set
# # #         if barcodeData not in found:
# # #             csv.write("{},{}\n".format(datetime.datetime.now(),
# # #                                        barcodeData))
# # #             csv.flush()
# # #             found.add(barcodeData)
# # #
# # #     # show the output frame
# # #     cv2.imshow("Barcode Scanner", frame)
# # #     key = cv2.waitKey(1) & 0xFF
# # #
# # #     # if the `q` key was pressed, break from the loop
# # #     if key == ord("q"):
# # #         break
# # #     # close the output CSV file do a bit of cleanup
# # # print("[INFO] cleaning up...")
# # # csv.close()
# # # cv2.destroyAllWindows()
# # # vs.stop()
# #
# #
# # import cv2
# # # import numpy as np
# # # from pyzbar.pyzbar import decode
# # #
# # # # Create a VideoCapture object and read from input file
# # # # If the input is the camera, pass 0 instead of the video file name
# # # cap = cv2.VideoCapture(0)
# # # csv = []
# # # found = set()
# # #
# # # # Check if camera opened successfully
# # # if (cap.isOpened()== False):
# # #   print("Error opening video stream or file")
# # #
# # # # Read until video is completed
# # # while(cap.isOpened()):
# # #   # Capture frame-by-frame
# # #   ret, frame = cap.read()
# # #   if ret == True:
# # #
# # #     # Display the resulting frame
# # #     cv2.imshow('Frame',frame)
# # #
# # #     # Press Q on keyboard to  exit
# # #     if cv2.waitKey(25) & 0xFF == ord('q'):
# # #       break
# # #
# # #   # Break the loop
# # #   else:
# # #     break
# # # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
# # # #find barcodes in the image
# # # decodedObjects = pyzbar.decode(gray)
# # # # loop over the detected barcodes
# # # for code in decodedObjects:
# # # # extract the bounding box location of the barcode and draw
# # #     # the bounding box surrounding the barcode on the image
# # #     (x, y, w, h) = code.rect
# # #     cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
# # #     # the barcode data is a bytes object so if we want to draw it
# # #     # on our output image we need to convert it to a string first
# # #     codeData = code.data.decode("utf-8")
# # #     codeType = code.type
# # #     text = "{} ({})".format(barcodeData, barcodeType)
# # #     cv2.putText(frame, text, (x, y - 10),
# # #     cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
# # #     # if the barcode text is currently not in our CSV file, write
# # #     # the timestamp + barcode to disk and update the set
# # #     if codeData not in found:
# # #         csv.write("{},{}\n".format(datetime.datetime.now(),
# # #                                    codeData))
# # #         csv.flush()
# # #         found.add(codeData)
# # #     cv2.imshow("Barcode Scanner", frame)
# # #     key = cv2.waitKey(1) & 0xFF
# # # #
# # #     #if the `q` key was pressed, break from the loop
# # #     if key == ord("q"):
# # #         break
# # #     # close the output CSV file do a bit of cleanup
# # # print("[INFO] cleaning up...")
# # # csv.close()
# # # cv2.destroyAllWindows()
# # # vs.stop()
# # #
# # #
# # # # When everything done, release the video capture object
# # # cap.release()
# # #
# # # # Closes all the frames
# # # cv2.destroyAllWindows()
# # #
# #
#
# import cv2
# import numpy as np
# from pyzbar.pyzbar import decode
#
#
# def detect_code(img):
#     code = decode(img)
#     if code != []:
#         the_code = code[0][0].decode()
#         return the_code
#         i == 0
#     else:
#         return code
#     return the_code
#
# cap = cv2.VideoCapture(1)
# i = 1
# while i == 1:
#
#
# # def read_video(cap):
# #     """
#
#     # :param cap:
#     # :return:
#     # """
#     # while True:
#     #     ret, frame = cap.read()
#     #     frame = cv2.bitwise_not(frame)
#     #     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     #     frame = frame[:200, :200]
#     #     cv2.imshow("frame", frame)
#     #     is_this_happening = detect_code(frame)
#     #     cv2.waitKey(1) & 0xFF == ord("q")
#     #     return is_this_happening
#
# def read_vedio(cap):
#     pass
#


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