import cv2
import numpy as np
import argparse

import math
from scipy.spatial import distance


#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "Path to the image")
#args = vars(ap.parse_args())

#img = cv2.imread(args["image"])
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

cv2.waitKey(0)
cv2.destroyAllWindows()