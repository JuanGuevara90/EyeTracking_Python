"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
import serial
import time
port = serial.Serial("/dev/ttyACM0", baudrate=9600)
print(port.name)

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

right= True
left= True
up= True
down= True
blinking = 0
center= 0

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Looking down"
        blinking = blinking +1
        print("Valor "+str(blinking))
        if (down):
            port.write(b"D\n")
            print(port)
            right=False
            left= False
            up= False
            down= False
            blinking= 0
            center= 0
            
    elif gaze.is_right():
        text = "Looking right"
        if (right):
            port.write(b'R\n')
            print(port)
            right=False
            left= False
            up= False
            down= False
            blinking= 0
            center= 0
            
            
    elif gaze.is_left():
        text = "Looking left"
        if (left):
            port.write(b'L\n')
            print(port)
            left=False
            right= False
            up= False
            down= False
            blinking= 0
            center= 0
    elif gaze.is_up():
        text = "Looking up"
        if (up):
            port.write(b'U\n')
            print(port)
            left=False
            right= False
            up= False
            down= False
            blinking= 0
            center= 0
    elif gaze.is_down():
        text = "Looking down"
        if (down):
            port.write(b'D\n')
            print(port)
            left=False
            right= False
            up= False
            down= False
            blinking= 0
            center= 0
    elif gaze.is_center():
        text = "Looking center"
        center = center +1
        if(center==7):
            port.write(b'C\n')
            print(port)
            left=True
            right= True
            up= True
            down= True
            blinking= 0
            center= 0


    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    separado_por_espacios = str(left_pupil).split(",")
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Ventana", frame)

    if cv2.waitKey(1) == 27:
        break


    
