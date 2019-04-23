# All filter transformations should come here

import cv2


def gaussian(filename, sigmax, sigmay, matrixsize = (0,0)):
    # Gaussian filters use a kernel which can be seen as a matrix of n x n pixels wide which
    # needs to be positive and odd, a standard deviation known as sigma is needed for x and y values

    gauss = cv2.GaussianBlur(filename, matrixsize, sigmax, sigmay)  # kernel size must be declared inside parenthesis
    return gauss
