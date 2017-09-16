class PDI():

    def alargamento_constrate(image,limiar):
        height, width = image.shape
        new_image = image.copy()
        for h in range(0,height):
            for w in range(0,width):
                if image[h, w] < limiar:
                    new_image[h,w] = 0
                else:
                    new_image[h,w] = 1
        return new_image

    def log_transformation(image,constant = 1):
        height, width = image.shape
        new_image = image.copy()
        for h in range(0,height):
            for w in range(0,width):
                new_image[h,w] = constant * np.log10(image[h,w] + 1)
        return new_image

    def powerrating_transformation(image,gama, constant = 1):
        height, width = image.shape
        new_image = image.copy()
        for h in range(0,height):
            for w in range(0,width):
                new_image[h,w] = constant * (image[h,w] ** gama)
        return new_image

    def bits_plane(image,plane):
        height, width = image.shape
        new_image = image.copy()
        for h in range(0,height):
            for w in range(0,width):
                bin_number = '{0:08b}'.format(image[h,w])
                if int(bin_number[7 - plane]) == 1:
                    new_image[h,w] = 255
                else:
                    new_image[h,w] = 0
        return new_image
