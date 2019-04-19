from tkinter import Tk
from tkinter.filedialog import askopenfilename
import cv2


def openfile():
    Tk().withdraw()
    file = askopenfilename()
    filename = cv2.imread(file)
    return filename

