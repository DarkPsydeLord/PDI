# All color transformations should be kept in this file

import cv2


def graytransform(filename):

    gris = cv2.cvtColor(filename, cv2.COLOR_BGR2GRAY)  # transforms the original image to greyscale
    return gris
