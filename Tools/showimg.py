# Generic function to show selected images

import cv2


def show(filename, name='FOO'):

    win2scn = cv2.imshow(name, filename)  # this function shows an image using OpenCv, needs a timer to be shown
    return win2scn
