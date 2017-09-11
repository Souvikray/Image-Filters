import numpy
import cv2
img = cv2.imread("scenery.jpg")
A = numpy.array([
          [5,7,2],
          [9,7,8],
          [5,2,1]
        ])

C = numpy.array([[5,8,7],
                 [8,9,3],
                 [5,6,1]])
B = [[5,7,2],
     [9,7,8],
     [5,2,1]]

D = [[5,8,7],
     [8,9,3],
     [5,6,1]]

E = numpy.array([[5,8],
                 [8,9],
                 [1,2]])

F = numpy.zeros(img.shape,dtype = int)


print(A*C)
print()
print(numpy.dot(A,E))
print()
print(F)


