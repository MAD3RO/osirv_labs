import numpy as np
import cv2

def invert_image(img):
    out_img = 255-img
    return out_img

image_path = "Images/airplane.bmp"

img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
imgg = cv2.imread(image_path, cv2.IMREAD_COLOR)

inv_img = invert_image(img)
inv_imgg = invert_image(imgg)
cv2.imshow("Invert",inv_img)
cv2.imshow("Original",img)
cv2.imshow("Original_color",imgg)
cv2.imshow("Invert_original",inv_imgg)
cv2.waitKey()
cv2.destroyAllWindows()
 