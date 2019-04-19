import cv2


def transgris(filename):

    gris = cv2.cvtColor(filename, cv2.COLOR_BGR2GRAY)
    return gris
