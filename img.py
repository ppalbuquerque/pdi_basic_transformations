import numpy as np
import cv2

def alargamento_constrate(image, limiar):
    height, width = image.shape
    for h in range(0,height):
        for w in range(0,width):
            if image[h, w] < limiar:
                image[h,w] = 0
            else:
                image[h,w] = 1

def log_transformation(image, constant = 1):
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
    n = 8
    for h in range(0,height):
        for w in range(0,width):
            bin_number = '{0:08b}'.format(image[h,w])
            new_image[h,w] = int(bin_number[:n - plane],2)


if __name__ == '__main__':
    img = cv2.imread('ar_chaves.jpg', 0)
    cv2.imshow('image', img)
    #alargamento_constrate(img, 100)
    #log_transformation(img, 1)
    powerrating_transformation(img, 1.0)
