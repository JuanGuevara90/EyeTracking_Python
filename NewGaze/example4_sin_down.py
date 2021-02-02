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

right= 0
left= 0
up= 0
down= 0
blinking = 0
center= 0
text=""

while True:
    try:
        # We get a new frame from the webcam
        _, frame = webcam.read()

        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)

        frame = gaze.annotated_frame()
        text = ""

        if gaze.is_blinking():
            text = "Looking blinking"
            blinking = blinking +1
            down = down +1
            print("Valor "+str(blinking))
            if (down==1):
                port.write(b"D\n")
                print(port)
                right=0
                left= 0
                up= 0
                down= 0
                blinking= 0
                center= 0
                
        elif gaze.is_right():
            text = "Looking right"
            right = right +1
            if (right==3):
                port.write(b'R\n')
                print(port)
                right=0
                left= 0
                up= 0
                down= 0
                blinking= 0
                center= 0
                
                
        elif gaze.is_left():
            text = "Looking left"
            left = left +1
            if (left==3):
                port.write(b'L\n')
                print(port)
                left=0
                right= 0
                up= 0
                down= 0
                blinking= 0
                center= 0
        
        elif gaze.is_center():
            text = "Looking center"
            center = center +1
            if(center==1):
                port.write(b'C\n')
                print(port)
                left=0
                right= 0
                up= 0
                down= 0
                blinking= 0
                center= 0

    except: 
        print("Error")


    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    separado_por_espacios = str(left_pupil).split(",")
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Ventana", frame)

    if cv2.waitKey(1) == 27:
        break


    

