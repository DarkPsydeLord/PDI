# All color transformations should be kept in this file

import cv2


def graytransform(filename):

    gray = cv2.cvtColor(filename, cv2.COLOR_BGR2GRAY)  # transforms the original image to greyscale
    return gray


def negativetransform(filename):

    bgr2gray = graytransform(filename)
    negative = cv2.bitwise_not(bgr2gray)
    return negative


def binarytransform(filename):

    rgb2gray = graytransform(filename)
    retval, binary = cv2.threshold(rgb2gray, 127, 255, cv2.THRESH_BINARY)
    return binary


def invbinarytransform(filename):

    rgb2gray = graytransform(filename)
    retval, invbinary = cv2.threshold(rgb2gray, 127, 255, cv2.THRESH_BINARY_INV)
    return invbinary


def adpbinarytransform(filename):

    rgb2gray = graytransform(filename)
    adpbinary = cv2.adaptiveThreshold(rgb2gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return adpbinary
