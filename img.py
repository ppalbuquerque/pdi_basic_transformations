import numpy as np
import cv2

def alargamento_constrate(image, limiar):
    height, width = image.shape
    new_image = np.zeros((height, width))
    for h in range(0,height):
        for w in range(0,width):
            if image[h, w] < limiar:
                new_image[h,w] = 0
            else:
                new_image[h,w] = 1
    cv2.imshow('new',new_image)
    cv2.waitKey(0)

def log_transformation(image, constant):
    height, width = image.shape
    new_image = np.zeros((height, width))
    for h in range(0,height):
        for w in range(0,width):
            new_image[h,w] = constant * np.log10(image[h,w] + 1)
    cv2.imshow('new',new_image)
    cv2.waitKey(0)

if __name__ == '__main__':
    img = cv2.imread('photo.jpg', 0)
    cv2.imshow('image', img)
    #alargamento_constrate(img, 50)
    log_transformation(img, 1)
