import cv2 as cv
import numpy as np
crop = False
ix = -1
iy = -1
img = cv.imread("images/bird.jpeg")

def crop(event,x,y,flags,params):
    global crop , ix, iy
    if event == 1:
        crop = True
        ix = x
        iy = y 

    elif event == 4:
        crop = False
        cv.rectangle(img, pt1=(ix,iy), pt2= (x,y),color=(0,0,0),thickness= 2)
        cropped = img[iy:y,ix:x]
        cv.imshow("cropped", cropped)
        cv.waitKey(0)
        cv.imwrite('cropedimage.jpeg', cropped)

cv.namedWindow("window")
cv.setMouseCallback("window" , crop)
while True:
    cv.imshow("window", img)

    if cv.waitKey(1) & 0xFF == ord("x"):
        break
    
cv.destroyAllWindows()