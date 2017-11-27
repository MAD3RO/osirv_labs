# import numpy as np
# import cv2

# def invert_image(img):
#     out_img = 255-img
#     return out_img

# image_path = "Images/airplane.bmp"

# img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
# imgg = cv2.imread(image_path, cv2.IMREAD_COLOR)

# inv_img = invert_image(img)
# inv_imgg = invert_image(imgg)
# cv2.imshow("Invert",inv_img)
# cv2.imshow("Original",img)
# cv2.imshow("Original_color",imgg)
# cv2.imshow("Invert_original",inv_imgg)
# cv2.waitKey()
# cv2.destroyAllWindows()
 
#zad2

import numpy as np
import cv2

def invert_image(img):
    out_img = 255-img
    return out_img

images_path = ["Images/airplane.bmp", 
                "Images/baboon.bmp",
                "Images/barbara.pgm",
                "Images/goldhill.bmp",
                "Images/pepper.bmp",
                "Images/lenna.bmp"]

# - perform the threshold operation with the parameter values of `63`, `127`, `191`
# - save the images to `problem2/imagename_parametervalue_thresh.png`
for image_path in images_path:
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    inv_img = invert_image(img)
    naziv_slike = image_path[7:-4]
    cv2.imwrite("problem1/"+naziv_slike+".png",inv_img)
    # for i in img:
    #     for j in img:
    #         if j[0]>63:
    #             j[0]=63
    thres1 = img[:,:,0] > 63
    img[thres1,0]=63
    thres2 = img[:,:,0] > 127
    thres3 = img[:,:,0] > 191
    img63=img[thres1,0]=63
    img127=img[thres2,0]=127
    img191=img[thres3,0]=191

            
    cv2.imshow("Threshold63",img)
    # cv2.imshow("Threshold127",img127)
    # cv2.imshow("Threshold191",img191)
    cv2.waitKey()
    cv2.destroyAllWindows()

    




 