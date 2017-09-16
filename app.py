import numpy as np
import cv2
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from pdi import PDI

def select_image():
    global panelA, image_cv

    path = filedialog.askopenfilename()

    if len(path) > 0:
        image_cv = cv2.imread(path, 0)
        image = Image.fromarray(image_cv)
        image = image.resize((250, 250), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)

    if panelA is None and panelB is None:
        panelA = Label(image=image)
        panelA.image = image
        panelA.pack(side='left', padx=10, pady=10)
    else:
        panelA.configure(image=image)
        panelA.image = image


def show_image(image, panel):
    image = Image.fromarray(image)
    image = image.resize((250, 250), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    if panel is None:
        panel = Label(image=image)
        panel.image = image
        panel.pack(side='left', padx=10, pady=10)
    else:
        panel.configure(image=image)
        panel.image = image

class Callbacks():

    def __init__(self, panel, image):
        self.panel = panel
        self.image = image

    def log_call(self):
        show_image(PDI.log_transformation(self.image,50), self.panel)

    def pow_call(self):
        show_image(PDI.powerrating_transformation(self.image, 3), self.panel)

    def bits_call(self, bits_plane_list):
        plane = int(bits_plane_list.get(ACTIVE)[6])
        show_image(PDI.bits_plane(self.image, plane), self.panel)

    def contrast_call(self):
        show_image(PDI.alargamento_constrate(self.image,56), self.panel)


def init_list_options(root):
    bits_plane_list = Listbox(root)
    bits_plane_list.insert(0,'Plano 0')
    bits_plane_list.insert(1,'Plano 1')
    bits_plane_list.insert(2,'Plano 2')
    bits_plane_list.insert(3,'Plano 3')
    bits_plane_list.insert(4,'Plano 4')
    bits_plane_list.insert(5,'Plano 5')
    bits_plane_list.insert(6,'Plano 6')
    bits_plane_list.insert(7,'Plano 7')
    return bits_plane_list

if __name__ == '__main__':
    image_cv = None
    root = Tk()
    panelA = None
    panelB = None
    image_loaded = False
    btn = Button(root, text='Selecionar Imagem', command=select_image)
    btn.pack(side='bottom', fill='both', expand='yes', padx='10', pady='10')


    while True:
        root.update()
        if (panelA is not None and image_loaded == False):
            image_loaded = True
            callbacks = Callbacks(panelB, image_cv)
            bits_plane_list = init_list_options(root)
            bits_plane_list.pack()
            btn = Button(root, text='Transformação Logaritimica', command=callbacks.log_call)
            btn.pack(side='bottom', fill='both', expand='yes', padx='10', pady='10')
            btn = Button(root, text='Transformação de Potência', command=callbacks.pow_call)
            btn.pack(side='bottom', fill='both', expand='yes', padx='10', pady='10')
            btn = Button(root, text='Plano De Bits', command=lambda: callbacks.bits_call(bits_plane_list))
            btn.pack(side='bottom', fill='both', expand='yes', padx='10', pady='10')
            btn = Button(root, text='Alargamento De Contraste', command=callbacks.contrast_call)
            btn.pack(side='bottom', fill='both', expand='yes', padx='10', pady='10')
