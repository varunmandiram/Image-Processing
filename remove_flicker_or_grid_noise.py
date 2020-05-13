
import cv2
import numpy as np
import sys
import imutils
def remove_flicker(file_name):

    #Read image
    img = cv2.imread(file_name, 0)

    #Resized image
    resized = imutils.resize(img, height=1024)
    
#    print("beofre fft")
    f = np.fft.fft2(resized)
    fshift = np.fft.fftshift(f)
#    print("after fft")

#    # calculate amplitude spectrum
#    mag_spec = 20*np.log(np.abs(fshift))
    
    r = int(f.shape[0]/2)        # number of rows/2
    c = int(f.shape[1]/2)        # number of columns/2   
    p = 3                         
    n = 1                   # to suppress all except for the DC component       
    fshift2 = np.copy(fshift)
    
    # suppress upper part
    print(r,n,c,p)
    fshift2[0:r-n , c-p:c+p] = 0.001
    # suppress lower part
    fshift2[r+n:r+r, c-p:c+p] = 0.001

#    # calculate new amplitude spectrum
#    mag_spec2 = 20*np.log(np.abs(fshift2))

    inv_fshift = np.fft.ifftshift(fshift2)
    # reconstruct image
    img_recon = np.real(np.fft.ifft2(inv_fshift))

    target_file_name = '.'.join(file_name.split('.')[:-1]) + '_flickrremove' + '.jpg'
    cv2.imwrite(target_file_name, img_recon)

#    img2 = cv2.imread(target_file_name, 0)
##    thresh1 = cv2.adaptiveThreshold(img2,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,8)
#    ret, thresh1 = cv2.threshold(img2,20,255,cv2.THRESH_TOZERO)
#
#
#    ret,thresh1 = cv2.threshold(img2,20,255,cv2.THRESH_BINARY)
#    ret,thresh2 = cv2.threshold(img2,20,255,cv2.THRESH_BINARY_INV)
#    ret,thresh3 = cv2.threshold(img2,80,255,cv2.THRESH_TRUNC)
#    ret,thresh4 = cv2.threshold(img2,80,255,cv2.THRESH_TOZERO)
#    ret,thresh5 = cv2.threshold(img2,80,255,cv2.THRESH_TOZERO_INV)
#    
#    titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
#    images = [img2, thresh1, thresh2, thresh3, thresh4, thresh5]
#    
#    for i in range(6):
#        plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
#        plt.title(titles[i])
#        plt.xticks([]),plt.yticks([])
#    
#    plt.show()
#    
#    target_file_name1 = '.'.join(file_name.split('.')[:-1]) + '_flickrremove_thresh1' + '.jpg'
#    cv2.imwrite(target_file_name1, thresh1)
#
#    target_file_name2 = '.'.join(file_name.split('.')[:-1]) + '_flickrremove_thresh2' + '.jpg'
#    cv2.imwrite(target_file_name2, thresh2)
#
#    target_file_name3 = '.'.join(file_name.split('.')[:-1]) + '_flickrremove_thresh3' + '.jpg'
#    cv2.imwrite(target_file_name3, thresh3)
#
#    target_file_name4 = '.'.join(file_name.split('.')[:-1]) + '_flickrremove_thresh4' + '.jpg'
#    cv2.imwrite(target_file_name4, thresh4)
#
#    target_file_name5 = '.'.join(file_name.split('.')[:-1]) + '_flickrremove_thresh5' + '.jpg'
#    cv2.imwrite(target_file_name5, thresh5)
    
    return target_file_name

if __name__ == "__main__":
    filename= sys.argv[1]
    ##Input an image here
    remove_flicker(filename)