import cv2
import numpy as np

#we create an empty function which does nothing just as to be called by the createTracker function to fullfill the parameters obligation
def nothing(arg):
    pass

#create a count variable to assign unique number to image names to avoid conflicts or overwriting
count = 0
#create some kernels
identity_kernel = np.array([[0,0,0], [0,1,0], [0,0,0]]) #has no effect on the image
sharpen_kernel = np.array([[0,-1,0], [-1,5,-1], [0,-1,0]]) #sharpens the image
gaussian_kernel = cv2.getGaussianKernel(3,0) #blurs the image
box_kernel = np.array([[1,1,1], [1,1,1], [1,1,1]], np.float32) / 16 #blurs the image in a neat way
#we create a list of kernels
kernels = [identity_kernel, sharpen_kernel, gaussian_kernel, box_kernel]
#load an image
original_image = cv2.imread("scenery.jpg")
#we want to save our final changes to the new image
modified_image = original_image.copy()
#convert image to grayscale
gray_original = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)
#create a copy of the gray scale image
gray_modified = gray_original.copy()

#create a window
cv2.namedWindow("Application")
#add trackbars to the window
cv2.createTrackbar("Brightness", "Application", 50, 100, nothing) #(name of the trackbar,name of the window,initial value,final value,onCreate function)
cv2.createTrackbar("Contrast", "Application", 1, 100, nothing)
cv2.createTrackbar("Filter", "Application", 0, len(kernels)-1, nothing)
cv2.createTrackbar("GrayScale", "Application", 0, 1, nothing)
#create a UI loop
while True:
    grayScale = cv2.getTrackbarPos("GrayScale", "Application")
    if grayScale == 0:
        #show the image
        cv2.imshow("Application", modified_image)  # (name of the window,image file)
    else:
        cv2.imshow("Application", gray_modified)

    key = cv2.waitKey(1) & 0xFF  #cv2.waitKey(1) returns a value of -1 which is masked using & 0xFF to get char value
    if key == ord('q'): #gives ASCII value of 'q'
        break
    elif key == ord('s'): #gives the ASCII value of 's'
        if grayScale == 0:
            #save the 'modified_image' to a file when no gray scale is applied
            cv2.imwrite("modified {}.png".format(count), modified_image)
        else:
            #save the 'gray_modified' to a file when gray scale is applied
            cv2.imwrite("modified {}.png".format(count), gray_modified)

        count+=1
    #get the trackbar position
    brightness = cv2.getTrackbarPos("Brightness", "Application") #(name of the trackbar,name of the window)
    contrast = cv2.getTrackbarPos("Contrast", "Application")
    kernel = cv2.getTrackbarPos("Filter", "Application")

    #set the brightness and contrast based on the openCV equation
    modified_image = cv2.addWeighted(original_image, contrast, np.zeros(original_image.shape, dtype = original_image.dtype), 0, brightness - 50)
    #set the filters on the image
    modified_image = cv2.filter2D(modified_image, -1, kernels[kernel])

    #set the brightness and contrast on the gray scale image
    gray_modified = cv2.addWeighted(gray_original,contrast,np.zeros(gray_original.shape,dtype = gray_original.dtype),0,brightness - 50)
    #set the filters on the gray scale image
    gray_modified = cv2.filter2D(gray_modified,-1,kernels[kernel])

#destroy all the windows
cv2.destroyAllWindows()