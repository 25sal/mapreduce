import cv2

coff_resize = 62.5/90
coff_pix = 9*256/1500
# if this image is 2304 px 
img=cv2.imread("images/test_6.tif")
print('Image Width is',img.shape[1])
print('Image Height is',img.shape[0])

# this should be 1600px 1m per px
img_75 = cv2.resize(img, (1500,1500), fx=coff_resize,fy=coff_resize)

cv2.imwrite("images/resized.tif", img_75) 


from PIL import Image 
  
# Open the image by specifying the image path. 
image_path = "images/resized.tif"
image_file = Image.open(image_path) 

qual = int(95 * (1500/1600)) 

# the default 
image_file.save("images/qaulity.jpeg", quality=qual) 