"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2

webcam = cv2.VideoCapture(0)

while True:
    try:
        # We get a new frame from the webcam
        ret, frame = webcam.read()
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) == 27:
            break
        
    except Exception as e:
        print(e)
        
webcam.release()
cv2.destroyAllWindows()