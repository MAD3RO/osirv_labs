# Create a program which will load all images from images directory in grayscale 
# perform the invert operation and 
# save the images to problem1/imagename_invert.png.

import numpy as np
import cv2

images = ["airplane.bmp", "baboon.bmp", "barbara.bmp", "barbara.pgm", "boats.bmp",
          "BoatsColor.bmp", "dioslike.jpg", "goldhill.bmp", "hp_logo.jpg", 
          "lenna.bmp", "pepper.bmp", "pero.jpg"]

for i in images:
    img = cv2.imread("images/"+i, 0) # 0 = grayscale
    inv = 255 - img
    cv2.imwrite("problem1/"+i.split('.')[0]+"_invert.png", inv)

