# Function waitKey in open cvs keeps the image alive for a certain amount of time
# Function destroyAllWindows will close all the opened images after a single keystroke like "esc"

import cv2


def wait():
    cv2.waitKey(0)  # keeps img alive for an indefinite amount of time, a parameter != 0 will set that amount of time
    cv2.destroyAllWindows()  # detects a keystroke to close all opened windows

