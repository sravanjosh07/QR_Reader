# import cv2
# from pyzbar.pyzbar import decode
#
# def read_video(cap):
#     while True:
#         ret, frame = cap.read()
#         frame = cv2.bitwise_not(frame)
#         frame = frame[:200, 0:200]
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         return frame
#
#
# def checking_Qr(frame):
#     code = decode(frame)
#     if code == []:
#         return False
#     else:
#         return True
#
# def decoding(frame):
#     code = decode(frame)
#     if code != []:
#         the_code = barcode.data.decode('utf-8')
#         return the_code
#     else:
#         pass
#     return the_code
#
#
#
#
# cap = cv2.VideoCapture(1)
# while True:
#     ret, frame = cap.read()
#     frame = cv2.bitwise_not(frame)
#     frame = frame[:200, 0:200]
#     frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#     cv2.imshow("window", frame)
#     cv2.waitKey(0) #& 0xFF == ord("q")
# #
# # if checking_Qr(frame) == True:
# #     code = decoding(frame)
