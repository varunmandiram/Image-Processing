from PIL import Image
import sys
def enhance_image(file_name):

    #resizing the image
    im = Image.open(file_name)
    print("Original Size", im.size)
    
    im2 = im.resize((min(4200, int(im.size[0]*2)), min(4200, int(im.size[1]*2))), Image.BICUBIC)
    
    #Improve the DPI to 1000 & save the enhanced image
    target_file_name = '.'.join(file_name.split('.')[:-1]) + '_resize' + '.jpg'
    im2.save(target_file_name,dpi=(300,300))

    return target_file_name
	
if __name__ == "__main__":
    filename= sys.argv[1]
    ##Input an image here
    enhance_image(filename)