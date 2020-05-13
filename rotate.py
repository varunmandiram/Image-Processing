import cv2
import numpy as np
import sys
import pytesseract
import logging
from scipy import ndimage


def rotate_image(file_name):

    #Target file
    target_file_name = '.'.join(file_name.split('.')[:-1]) + '_rotated' + '.jpg'

    #Read image
    img = cv2.imread(file_name, 0)
    #logging.info("Image Size: "+img.shape)

    #Flip the foreground
    gray = cv2.bitwise_not(img)
     
    # threshold the image, setting all foreground pixels to
    # 255 and all background pixels to 0
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    
    #cv2.imwrite('.'.join(file_name.split('.')[:-1]) + '_thresh' + '.jpg', thresh)
    
    # grab the (x, y) coordinates of all pixel values that
    # are greater than zero, then use these coordinates to
    # compute a rotated bounding box that contains all
    # coordinates
    coords = np.column_stack(np.where(thresh > 0))
    angle = cv2.minAreaRect(coords)[-1]
     
    # the `cv2.minAreaRect` function returns values in the
    # range [-90, 0); as the rectangle rotates clockwise the
    # returned angle trends to 0 -- in this special case we
    # need to add 90 degrees to the angle
    if angle < -45:
        angle = -(90 + angle)
     
    # otherwise, just take the inverse of the angle to make
    # it positive
    else:
        angle = -angle

     
    logging.info(f'Angle:{angle}')
    if angle != 0.0:
        # rotate the image to deskew it
        (h, w) = img.shape[:2]
        center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, 1.0)
        rotated = cv2.warpAffine(img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
        cv2.imwrite(file_name, rotated)
    
    else:
        #rotating by right angle - use pyttesseract to rotate landscape images
        try:
            a=(pytesseract.image_to_osd(file_name,output_type=pytesseract.Output.DICT))
            logging.info(f'Orientation:{a}')
            if(a["orientation"]==270):
                x=ndimage.rotate(img, 270)
                img=x
                logging.info('\nImage Rotated...\n')
            elif(a["orientation"]==90):
                x=ndimage.rotate(img,90)
                img=x
                logging.info('\nImage Rotated...\n')
            elif(a["orientation"]==180):
                x=ndimage.rotate(img,-90)
                img=x
                logging.info('\nImage Rotated...\n')
        except:
            img=img

        cv2.imwrite(file_name, img)
        #logging.info("Image Size: "+img.shape)
    return target_file_name

if __name__ == "__main__":
    filename= sys.argv[1]
    ##Input an image here
    rotate_image(filename)