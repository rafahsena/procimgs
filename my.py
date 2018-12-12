import matplotlib.pyplot as plt
import numpy

def clamp(pixel):
    if pixel < 0:
        pixel = 0
    elif pixel > 255:
        pixel = 255
    return pixel

def imread(img):
    image = 255 * plt.imread(img)
    return image.astype('uint8')

def nchannels(img):
    return img[0][0].size

def size(img):
    array = []
    array.append(len(img[0])) #Largura
    array.append(len(img)) #Altura
    return array

def rgb2gray(img):
    grayimg = numpy.array([[pixel[0]*0.299 + pixel[1]*0.587 + pixel[2]*0.114 for pixel in img[n]] for n in range(len(img))])
    return grayimg.astype('uint8')

def imreadgray(img):
    new = imread(img)
    if(nchannels(new) > 2):
        return rgb2gray(new)
    return new

def imshow(img):
    cmap = None
    if(nchannels(img) == 1):
        cmap = "gray"
    print(img)
    plt.imshow(img, cmap=cmap, interpolation="nearest")
    plt.show()

def thresh(img, threshold):
    binary_img = numpy.array([[255 if pixel >= threshold else 0 for pixel in img[n]] for n in range(len(img))])
    return binary_img.astype('uint8')

def negative(img):
    if(nchannels(img) == 1):
        negative = numpy.array([[255 - pixel for pixel in img[n]] for n in range(len(img))])
    else:
        negative = numpy.array([[[255 - channel for channel in pixel] for pixel in img[n]] for n in range(len(img))])
    return negative

def contrast(img, r, m):
    contrast = numpy.array([[[clamp(r*(channel - m) + m) for channel in pixel] for pixel in img[n]] for n in range(len(img))])
    return contrast.astype('uint8')

def hist(img):
    if(nchannels(img) == 1):
        hist = numpy.zeros((256, 1), int)
        for line in img:
            for pixel in line:
                hist[pixel][0] += 1
        return hist
    else:
        hist = numpy.zeros((256, 3), int)
        for line in img:
            for pixel in line:
                for index, channel in enumerate(pixel):
                    hist[channel][index] += 1
        return hist

def histeq(img):
    histo = hist(img)
    aux = size(img)
    total = aux[0]*aux[1]
    px = []
    if(nchannels(img) == 1):
        for line in histo:
            for intensity in line:
                px.append(intensity/total)
    cdf = []
    for i in range(0, len(px) + 1):
        cdf.append(int(sum(px[:i]) * 255))
    print(cdf)
    histeq = numpy.array([[cdf[pixel] for pixel in img[n]] for n in range(len(img))])
    return histeq