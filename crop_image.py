import cv2
import sys
import imutils
def crop_image(file_name, area, ind):

    target_file_name = '.'.join(file_name.split('.')[:-1]) + '_cropped' + str(ind) + '.jpg'

#    #resizing if necessary
#    im = Image.open(file_name)
#    #print("Original Size", im.size)
#    
#    #Crop the 1st half of the image for ADP forms
#    #area = (0, 0, int(im.size[0]/2), int(im.size[1]/2))
#    cropped_img = im.crop(area)


    #Read image
    image = cv2.imread(file_name, 0)
    print("Image Size: ",image.shape)

    #Crop image
    (x,y,w,h) = area
    crop_img = image[y:h, x:w]

    #Resized image
    resized = imutils.resize(crop_img, height=1024)
    print("Cropped Image Size: ",resized.shape)

    cv2.imwrite(target_file_name, resized)

    return target_file_name
	
if __name__ == "__main__":
    filename= sys.argv[1]
    ##Input an image here
    crop_image(filename)