import cv2
import numpy
'''
#read an image
img = cv2.imread("scenery.jpg")
#show the dimensions of the image
print(img.shape)
#show the image
cv2.imshow("TestImage",img)
#hold the image
cv2.waitKey(0)
#destroy the windows with press of a button
cv2.destroyAllWindows()
'''

'''
#read an image
img = cv2.imread("scenery.jpg")
#convert the image to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#show the image
cv2.imshow("GrayImage",gray)
#hold the image
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
img = cv2.imread("scenery.jpg")

#apply brightness and contrast to the image
cb_img = cv2.addWeighted(img,4,img.copy(),0,10)  #here contrast value is 4 and brightness value is 10
                                                 #the third parameter needs to be given some image since
                                                 #we are performing a matrix addition with the first parameter
                                                 #we supply fourth parameter as 0 since we have only one image to deal with
                                                 #for the fifth parameter,we supply the brightness value as 10 and
                                                 #it will automatically set the matrix for us
cv2.imshow("Contrast and Brightness",cb_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

img = cv2.imread("scenery.jpg")
K1 = numpy.array([
                    [0,0,0],
                    [0,1,0],
                    [0,0,0]
                ])

K2 = numpy.array([
                    [0,-1,0],
                    [-1,5,-1],
                    [0,-1,0]
                ])

#perform convultion
#convolved = cv2.filter2D(img,-1,K1)  #gives no effect
convolved = cv2.filter2D(img,-1,K2)   #gives sharpness to the image

cv2.imshow("Original",img)
cv2.imshow("Convolved",convolved)
cv2.waitKey(0)
cv2.destroyAllWindows()


