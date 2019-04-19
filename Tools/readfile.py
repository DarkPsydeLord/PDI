# Generic file reader

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import cv2


def openfile():
    Tk().withdraw()  # closes the default window and wait for the customised one to be opened
    file = askopenfilename()  # uses the default file opener
    filename = cv2.imread(file)  # passes the parameter obtained from python to OpenCv
    return filename

