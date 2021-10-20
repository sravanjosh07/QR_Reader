

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