import os

from pyzbar.pyzbar import decode
import time
import cv2

detected_location = r"C:\Users\opv-operator\Desktop\QR_Reader\Deteced"
undetected_location = r"C:\Users\opv-operator\Desktop\QR_Reader\undetected"
cap = cv2.VideoCapture(r'C:\Users\opv-operator\Desktop\QR_Reader\avivideos/sunlight_slow_extralighting.avi')
# Get the frames per second
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)
# Get the total numer of frames in the video.
frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
fps1 = cap.get(5)
fr1 = cap.get(7)
print(fps1, fr1)
print(frame_count)
no_detected_frames = 0
detected_frames = []
dictionary_of_Boolean = {}

frame_number = 0

while True:
    ret, frame = cap.read()
    frame_number += 1
    dictionary_of_Boolean[frame_number] = 0
    neg_frame = cv2.bitwise_not(frame)
    gray = cv2.cvtColor(neg_frame, cv2.COLOR_BGR2GRAY)
    # frame = cv2.blur(frame, (3,3))
    # ret, thresh1 = cv2.threshold(frame, 0, 255, cv2.THRESH_TOZERO)
    # thresh1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 2)
    # th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 89, 15)

    # thresh1 = cv2.adaptiveThreshold(frame, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 31, 7) #When there is sunlight
    thresh1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 2)
    # ret, thresh1 = cv2.threshold(thresh1, 0, 255, cv2.THRESH_OTSU)
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

    with open('metrics.csv', 'a') as csv:
        csv.write('{},{}\n'.format(frame_number, dictionary_of_Boolean[frame_number]))
        csv.flush()
    print(no_detected_frames)

    cv2.imshow("QR_Scanner", frame)
    cv2.imshow("QR_Scanner thresh", thresh1)
    cv2.waitKey(1)
