from PIL import Image
from cv2 import *
import webbrowser
# import playsound
from pyzbar.pyzbar import decode

def beep():
    playsound._playsoundWin("beepsound.wav")

def bar_decoder(file):
    #Decodes the barcode
    code=decode(Image.open(file))
    #Incase the scanner cannot read the image.
    if code != []:
        #Turns the byte type barcode into string
        the_code=code[0][0].decode()
    else:
        return code
    return the_code
    os.remove(Product.png)


import cv2
def check(file):
    """
    The function that checks if the frame has a barcode in it
    :param file: the file that needs to be checked
    :return: True or False
    """
    #Decoder
    code=decode((file))
    if code == []:
        #No Barcode
        return False
    #Yes Barcode
    return True
def webcam_capture(camera):
    """
    Function that takes video feed from the webcamera and checks frames for the presence of a barcode.
    as soon as a barcode is detected it takes a snapshot of the image and stores it as a file.
    :param camera: Camera that does the video taking
    :return:
    """
    #Live video feed

    while True:
        #Reading the video feed
        shape,frame=camera.read()
        frame = cv2.bitwise_not(frame)
        # frame = frame[:400, :,400]
        # if not shape:
        #     break
        #Normal Window
        # color_scheme=cv2.cvtColor(frame, cv2.WINDOW_NORMAL)
        #What we see
        cv2.imshow('window',frame)
        #Live barcode detection
        detection=check(frame)
        #Barcode detected
        if detection==True:
            #Saving an image with the barcode
            # beep()
            i = 10
            while i < 10:
                cv2.imwrite("Product%d.png", i, frame)
                i += 1
                return "Product%d.png"
                #Stop Video Feed
                break
        #Manual Stop
        elif cv2.waitKey(1) & 0xFF == ord ("q"):
            break
    camera.release()
    cv2.destroyAllWindows()

def capture(camera,show=False):
    """
    Takes a picture of whatever webcam is filming. Mainly there for taking images with webcam.
    :param camera: Camera to be used
    :return:
    """
    sub, img = camera.read()


    if sub:    # frame captured without any errors
        #If the user wants to see the image they take
        if show == True:
            namedWindow("Product Barcode",cv2.WINDOW_NORMAL)
            imshow("Product Barcode",img)
        waitKey(0)
        destroyWindow("Product Barcode")
        name ="Product.png"
        imwrite(name,img) #save image


# def web_browse(code):
#     """
#     Opens the product page in a web browser
#     :param code: The barcode
#     """
#     webbrowser.open('https://www.barcodelookup.com/'+code)


cap = cv2.VideoCapture(1)
img = webcam_capture(cap)
Qr =bar_decoder(img)
print(Qr)





