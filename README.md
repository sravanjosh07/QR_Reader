# QR_Reader
A [QR code](https://upload.wikimedia.org/wikipedia/commons/d/d0/QR_code_for_mobile_English_Wikipedia.svg) (Quick Response Code) is a type of matrix code (2-Dimensional Bar code) invented in 1994 by an automobile company, Denso Wave. A QR code is a machine readable optical label that contains information about the item to which it is attached to. It was primarily developed to locate, identify and track the automotive parts. However, due to its fast readability it has become popular across different industries. 


## Detecting and decoding the code
The video feed is preprocessed and fed into the [pyzbar](https://pypi.org/project/pyzbar/) function, which detects and decodes the QR code.

## Adding sound and taking the output
sound is played when the code finding is a success, a timer is set to freeze the recording to prevent further detection of the same QR-code. The output is then appended to a list, which is also used to detect the duplicates of the scanned code. 



