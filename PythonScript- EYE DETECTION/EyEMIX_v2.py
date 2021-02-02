import numpy as np
import cv2

import argparse

import math
from scipy.spatial import distance


def pupil():
    #img = cv2.imread(roi_color2,0)
    img = cv2.imread("input2.png", 0)
    img = cv2.medianBlur(img,5)
    cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)


    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,100,param1=50,param2=25,minRadius=10,maxRadius=30)

    circles = np.uint16(np.around(circles))

    for i in circles[0,:]:
        pt = (i[0],i[1])
        print(pt)
        cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
        # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    
    cv2.imshow('detect',cimg)

    return 0



#eye_cascade = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')


#number signifies camera
cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    eyes = eye_cascade.detectMultiScale(gray)
    for (ex,ey,ew,eh) in eyes:
        #cv2.rectangle(img,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        #roi_gray2 = gray[ey:ey+eh, ex:ex+ew]
        roi_color2 = img[ey:ey+eh, ex:ex+ew]

        #cv2.imshow('img',img)
        #cv2.imshow('img2',gray)
        #cv2.imshow('img3',roi_color2)
        cv2.imwrite('input2.png', roi_color2) 
        try:
            #img = cv2.imread(roi_color2,0)
            img_ = cv2.imread("input2.png", 0)
            img_ = cv2.medianBlur(img_,5)
            cimg = cv2.cvtColor(img_,cv2.COLOR_GRAY2BGR)
            circles = cv2.HoughCircles(img_,cv2.HOUGH_GRADIENT,1,100,param1=50,param2=25,minRadius=10,maxRadius=30)

            circles = np.uint16(np.around(circles))

            for i in circles[0,:]:
                pt = (i[0],i[1])
                print(pt)
                cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
                # draw the center of the circle
                cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
            
            cv2.imshow('detect',cimg)
        except Exception as e:
            print(e)


        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break




cap.release()
cv2.destroyAllWindows()