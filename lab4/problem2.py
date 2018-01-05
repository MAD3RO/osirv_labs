# Create a program which will load all images from images directory
# perform the threshold operation with the parameter values of 63, 127, 191
# save the images to problem2/imagename_parametervalue_thresh.png

import numpy as np
import cv2

images = ["airplane.bmp", "baboon.bmp", "barbara.bmp", "barbara.pgm", "boats.bmp",
          "BoatsColor.bmp", "dioslike.jpg", "goldhill.bmp", "hp_logo.jpg", 
          "lenna.bmp", "pepper.bmp", "pero.jpg"]


for i in images:
    img = cv2.imread("images/"+i, 0) #grayscale
    ret,thr1 = cv2.threshold(img, 63, 255, cv2.THRESH_TOZERO)
    ret,thr2 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    ret,thr3 = cv2.threshold(img, 191, 255, cv2.THRESH_TOZERO)
    cv2.imwrite("problem2/"+i.split('.')[0]+"_63_thresh.png", thr1)
    cv2.imwrite("problem2/"+i.split('.')[0]+"_127_thresh.png", thr2)
    cv2.imwrite("problem2/"+i.split('.')[0]+"_191_thresh.png", thr3)