# Perform the quantisation with the added noise, according to the formula
# above. Use the same image and quantisation values as in Problem 3.
# Save the images as .bmp files with the filename format boats_qn.bmp,  where q is the
# numeric value of q used for that image.
# Comment the visual quality of quantised images with noise compared to
# quantised images in Problem 3, for all the values of q.

import numpy as np
import cv2

img = cv2.imread("images/BoatsColor.bmp", 0) # grayscale
img = img.astype(np.float32)
img[img>255.0]=255.0 # sve vrijednosti piksela vece od 255 stavljamo na 255
img[img<0.0]=0.0 # sve vrijednosti piksela manje od 0 stavljamo na 0
for i in range(1,9):
    n = np.random.uniform(0, 1, img.shape)
    d = 2**(8-i)
    noise = (np.floor(img/d+n)+0.5)*d
    noise = noise.astype(np.uint8)
    cv2.imwrite("problem4/boats_"+str(i)+"n.bmp", noise)