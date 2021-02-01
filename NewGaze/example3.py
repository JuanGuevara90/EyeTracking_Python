"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking
import serial
import time
port = serial.Serial("/dev/ttyACM0", baudrate=9600)
text = ""
gaze = GazeTracking()
webcam = cv2.VideoCapture(0)

right= 0
left= 0
blinking = 0
center= 0


while True:
    try:
        # We get a new frame from the webcam
        _, frame = webcam.read()

        # We send this frame to GazeTracking to analyze it
        gaze.refresh(frame)

        frame = gaze.annotated_frame()
        

        if gaze.is_blinking():
            text = "Looking blinking"
            blinking = blinking +1
            print(blinking)
            right= 0
            left= 0
            center= 0
            if (blinking==4):
                port.write(b"B\n")
                blinking = 0
                
                
        elif gaze.is_right():
            text = "Looking right"
            right = right +1
            print(right)
            left= 0
            blinking = 0
            center= 0
                
            if (right==4):
                port.write(b"R\n")
                right= 0
                
        elif gaze.is_left():
            text = "Looking left"
            left = left +1
            print(left)
            blinking = 0
            center= 0
            right= 0
            if (left==4):
                port.write(b"L\n")
                left= 0
                

        elif gaze.is_center():
            text = "Looking center"
            center = center +1
            print(center)
            right= 0
            left= 0
            blinking = 0
            if (center==4):
                port.write(b"C\n")
                center= 0

        cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

        left_pupil = gaze.pupil_left_coords()
        separado_por_espacios = str(left_pupil).split(",")
        right_pupil = gaze.pupil_right_coords()
        cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
        cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

        cv2.imshow("Ventana", frame)


    except: 
        print("Error")




    if cv2.waitKey(1) == 27:
        break


    

