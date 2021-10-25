import cv2
from pyzbar.pyzbar import decode
import time
import winsound
import datetime

cap = cv2.VideoCapture(0)
scanned_code_list = []
scanned_data_dict: dict[str, datetime.datetime] = {}  # key: code, value: last detection
csv = open("scanned_QRcodes.csv", "w")
camera = True
square = 200
while camera == True:
    ret, frame = cap.read()

    frame_crop = frame[-200:, int(frame.shape[1]/2-square/2):int(frame.shape[1]/2+square/2)]
    frame_crop = cv2.bitwise_not(frame_crop)
    frame_crop = cv2.cvtColor(frame_crop, cv2.COLOR_BGR2GRAY)
    ret, frame_crop = cv2.threshold(frame_crop, 0, 255, cv2.THRESH_OTSU)

    # cv2.imshow("QR_Scanner thresh", frame_crop)

    now = datetime.datetime.now()
    x = int(time.time())

    for code in decode(frame_crop):
        mycode = code.data.decode("utf-8")


        if mycode not in scanned_code_list:
            print(mycode)
            scanned_code_list.append(mycode)
            csv.write("{},{}\n".format(datetime.datetime.now(), mycode))
            scanned_data_dict["mycode"] = x
            csv.flush()
            # winsound.Beep(500, 500)

        elif mycode in scanned_code_list and x - scanned_data_dict["mycode"] > 5:
            # scanned_data_dict.update({"mycode": x}) #clearing the list will rewrite the dict as it's going to get scanned again
            scanned_code_list.clear()
            break

        else:
            continue

    frame = cv2.rectangle(
        frame,
        (int(frame.shape[1]/2-square/2), frame.shape[0]-square),
        (int(frame.shape[1]/2+square/2), frame.shape[0]),
        (0, 255, 0),
        thickness=3)
    cv2.imshow("QR_Scanner", frame)
    cv2.waitKey(1)
print(scanned_data_dict)
