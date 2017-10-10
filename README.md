Every image is basically a matrix representation.The elements of a matrix are the pixel values and we can modify the elements to modify the image itself.So we use the below equation to change the pixel value

I(out) = cI(in) + B

I(out) is the resultant pixel

I(in) is the input pixel

B is the brightness matrix

Further we look at the concept of kernel which is basically a small square of matrix of odd dimensions.So we combine the kernel with an image to produce different effects.This is usually done using a process called convolution where we carve out a portion of the image say a matrix.look at the central element or pixel and also look at the nearby pixels and perform operations.

We can use different kernels to get different effects on an image.Some examples of kernels used in this application are Sharpen Kernel,Gaussian Kernel,Box Kernel etc.

Original Image
![Alt text](https://github.com/Souvikray/Image-Filters/blob/master/scenery.jpg?raw=true "Optional Title")

Increment in brightness

![Alt text](https://github.com/Souvikray/Image-Filters/blob/master/modified%201.png?raw=true "Optional Title")

GrayScale Image
![Alt text](https://github.com/Souvikray/Image-Filters/blob/master/modified%202.png?raw=true "Optional Title")



