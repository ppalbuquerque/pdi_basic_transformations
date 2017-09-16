import numpy as np
import cv2
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog

def select_image():
    global panelA, panelB

    path = filedialog.askopenfilename()

    if len(path) > 0:
        image = cv2.imread(path, 0)
        #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

    if panelA is None and panelB is None:
        panelA = Label(image=image)
        panelA.image = image
        panelA.pack(side='left', padx=10, pady=10)
    else:
        panelA.configure(image=image)
        panelA.image = image

# Global Variables
image = None

def alargamento_constrate(image, limiar):
    height, width = image.shape
    for h in range(0,height):
        for w in range(0,width):
            if image[h, w] < limiar:
                image[h,w] = 0
            else:
                image[h,w] = 1

def log_transformation(constant = 1):
    height, width = image.shape
    for h in range(0,height):
        for w in range(0,width):
            image[h,w] = constant * np.log10(image[h,w] + 1)

def powerrating_transformation(image, gama, constant = 1):
    height, width = image.shape
    for h in range(0,height):
        for w in range(0,width):
            image[h,w] = constant * (image[h,w] ** gama)

def bits_plane(image, plane):
    height, width = image.shape
    new_image = np.zeros((height, width))
    for h in range(0,height):
        for w in range(0,width):
            bin_number = '{0:08b}'.format(image[h,w])
            if int(bin_number[7 - plane]) == 1:
                image[h,w] = 255
            else:
                image[h,w] = 0


if __name__ == '__main__':
    root = Tk()
    panelA = None
    panelB = None
    btn = Button(root, text='Select a image', command=select_image)
    btn.pack(side='bottom', fill='both', expand='yes', padx='10', pady='10')

    root.mainloop()
