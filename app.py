import cv2
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from pdi import PDI

def select_image(callbacks):
    global panelA, image_cv

    path = filedialog.askopenfilename()

    if len(path) > 0:
        image_cv = cv2.imread(path, 0)
        image = Image.fromarray(image_cv)
        image = image.resize((350, 350), Image.ANTIALIAS)
        image = ImageTk.PhotoImage(image)
        callbacks.image = image_cv

    if panelA is None and panelB is None:
        panelA = Label(image=image)
        panelA.image = image
        panelA.place(x = 25, y = 100)
    else:
        panelA.configure(image=image)
        panelA.image = image


def show_image(image, panel):
    image = Image.fromarray(image)
    image = image.resize((350, 350), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)
    if panel is None:
        panel = Label(image=image)
        panel.image = image
        panel.place(x = 400,y = 100)
    else:
        panel.configure(image=image)
        panel.image = image

class Callbacks():

    def __init__(self, panel, image):
        self.panel = panel
        self.image = image

    def log_call(self, log_entry):
        show_image(PDI.log_transformation(self.image,int(log_entry.get())), self.panel)

    def pow_call(self, pow_entry):
        show_image(PDI.powerrating_transformation(self.image, float(pow_entry.get()), 1), self.panel)

    def bits_call(self, bits_plane_list):
        plane = int(bits_plane_list.get(ACTIVE)[6])
        show_image(PDI.bits_plane(self.image, plane), self.panel)

    def contrast_call(self, constr_entry):
        show_image(PDI.alargamento_constrate(self.image,int(constr_entry.get())), self.panel)


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
    root.title("PDI")
    root.minsize(width=760,height=660)
    panelA = None
    panelB = None
    image_loaded = False
    callbacks = Callbacks(panelB, image_cv)
    btn = Button(root, text='Selecionar Imagem', command=lambda: select_image(callbacks))
    btn.place(x = 30, y = 25)


    while True:
        root.update()
        if (panelA is not None and image_loaded == False):
            log_label = Label(text = "Constante Da Logaritimica")
            entry_log = Entry()
            pow_label = Label(text = "Gama da potência")
            entry_pow = Entry()
            contr_label = Label(text = "Limiar do alargamento")
            entry_contr = Entry()
            log_label.place(x = 25, y= 510)
            entry_log.place(x = 25, y = 530)
            pow_label.place(x = 35, y = 550)
            entry_pow.place(x = 25, y = 570)
            contr_label.place(x = 25, y = 600)
            entry_contr.place(x = 25, y = 620)
            image_loaded = True
            bits_plane_list = init_list_options(root)
            bits_plane_list.place(x=300, y = 510)
            btn = Button(root, text='Transformação Logaritimica', command=lambda: callbacks.log_call(entry_log))
            btn.place(x=25,y=475)
            btn = Button(root, text='Transformação de Potência', command=lambda: callbacks.pow_call(entry_pow))
            btn.place(x=225,y=475)
            btn = Button(root, text='Plano De Bits', command=lambda: callbacks.bits_call(bits_plane_list))
            btn.place(x=425,y=475)
            btn = Button(root, text='Alargamento De Contraste', command=lambda: callbacks.contrast_call(entry_contr))
            btn.place(x=540,y=475)
