# Generic function to show selected images

import cv2


def show(filename, name='FOO'):
    win2scn = cv2.imshow(name, filename)
    return win2scn
