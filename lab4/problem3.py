# Perform the quantisation on the image BoatsColor.bmp 
# for all values of q in the interval [1,8]. 
# Save the images as .bmp files with the filename format boats_q.bmp,  where q is the
# numeric value of q used for that image.
# Comment the visual quality of quantised images compared to original image, for
# all  values of  q.

import numpy as np
import cv2

img = cv2.imread("images/BoatsColor.bmp", 0) # grayscale
img = img.astype(np.float32)
img[img>255.0]=255.0 # sve vrijednosti piksela vece od 255 stavljamo na 255
img[img<0.0]=0.0 # sve vrijednosti piksela manje od 0 stavljamo na 0
for i in range(1,9):
    d=2**(8-i)
    img_quant = (np.floor(img/d)+0.5)*d
    img_quant = img_quant.astype(np.uint8)
    cv2.imwrite("problem3/boats_"+str(i)+".bmp", img_quant)

