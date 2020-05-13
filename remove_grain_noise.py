import cv2
import numpy as np
import sys

def remove_grain_noise(file_name):
    target_file_name = '.'.join(file_name.split('.')[:-1]) + '_grain_removed' + '.jpg'
    
    img = cv2.imread(file_name)
    
    kernel = np.ones((5, 5), np.uint8)
    #cv2.dilate(img, kernel, iterations = 1)
    
    kernel = np.ones((5, 5), np.uint8)
    #cv2.erode(img, kernel, iterations = 1)
    
    #bg_img =  cv2.medianBlur(img, 3)
    cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    cv2.imwrite(target_file_name, img)

if __name__ == "__main__":
    filename= sys.argv[1]
    ##Input an image here
    remove_grain_noise(filename)