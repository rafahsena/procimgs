import sys
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def clamp(self, x, x_min, x_max):
    if (x < x_min):
        x = x_min
    if (x > x_max):
        x = x_max
    return x
def imread(str):
    img = plt.imread(str)
    if (nchannels(img) == 3 and img.dtype != np.int32):
        img = np.uint8(img[..., :3] * 255)
    if (nchannels(img) == 4 and img.dtype != np.int32):
        img = np.uint8(img[..., :4] * 255)
    if (nchannels(img) < 3 and img.dtype != np.int32):
        img = np.uint(img * 255)
    return img


def nchannels(img):
    if(len(img.shape) == 2):
        return 1
    *s, c = img.shape
    return c


def size(img):
    if(len(img.shape) == 2):
        s = img.shape
        return s
    *s, c = img.shape
    return s

def rgb2gray(img):
    grayimg = np.array([[pixel[0]*0.299 + pixel[1]*0.587 + pixel[2]*0.114 for pixel in img[n]] for n in range(len(img))])
    return grayimg.astype('uint8')


def imreadgray(str):
    img = imread(str)
    img = rgb2gray(img)
    return img

def test():
    a = np.array((1,2,3))
    img = np.vstack(a.ravel())
    print(img)

def imshow(img):
    if(nchannels(img) == 1):
        imgplot = plt.imshow(img, cmap="gray", interpolation="nearest")
    else:
        imgplot = plt.imshow(img, interpolation="nearest")

    plt.show()


def negative(img):
    img1 = img.copy()
    img1 = 255 - img1
    return img1


def contrast(f, r, m):
    f1 = f.copy()
    g = np.clip(r * (f1 - m) + m, 0, 255).astype(np.uint8)
    return g


def hist(img):
    if(nchannels(img) == 1):
        hist = np.zeros((256, 1), int)
        for line in img:
            for pixel in line:
                hist[pixel][0] += 1
        
        return hist
    else:
        hist = np.zeros((256, 3), int)
        for line in img:
            for pixel in line:
                for index, channel in enumerate(pixel):
                    hist[channel][index] += 1
        return hist


def showhist(hist, bin=1):
    
    showhist = 0
    newHist = None
    x = list(range(bin))
    z = 0 
    _, ax = plt.subplots()
    if(len(hist[0]) == 1):
        
        showhist = np.hstack(hist)
        newHist = showhist.copy()
        newHist = np.zeros_like(newHist)
        
        for j in range(0, 256):

            pix = showhist[j] * bin / 256
            pix = round(pix).astype(np.uint8)
            if ( pix < bin):
                newHist[pix] += 1
        
            
        for j in range(0, bin):
            ax.bar(x[j], newHist[j], color= "Blue")
                
    if(len(hist[0]) == 3):
        R = np.hstack(hist[...,0])
        G = np.hstack(hist[...,1])
        B = np.hstack(hist[...,2])
        
        newHist = R.copy()
        newHist = np.zeros_like(newHist)
        newHist1 = newHist.copy()
        newHist2 = newHist.copy()
        
        for j in range(0, 256):

            pix = R[j] * bin / 256
            pix1 = G[j] * bin / 256
            pix2 = B[j] * bin / 256

            pix = round(pix).astype(np.uint8)
            pix1 = round(pix1).astype(np.uint8)
            pix2 = round(pix2).astype(np.uint8)
            
            if ( pix < bin):
                newHist[pix] += 1
            
            if ( pix1 < bin):
                newHist1[pix1] += 1
            
            if ( pix2 < bin):
                newHist2[pix2] += 1
        
            
        

        for j in range(0, bin):
            ax.bar(x[j] - 0.2, newHist[j], width = 0.2, color= "Red", align = "center")
            ax.bar(x[j], newHist1[j], width = 0.2 ,color= "Green", align = "center")
            ax.bar(x[j] + 0.2, newHist2[j], width = 0.2, color= "Blue", align = "center")


   
     
    plt.show()
    
    
    
def convolve(img, mask):
    new = np.flip(mask, 0)
    mask = np.flip(new, 1)
    new = np.zeros((img.shape[0], img.shape[1]))
    aux = np.zeros((img.shape[0] + 2, img.shape[1] + 2), np.uint8)
    aux[1:-1, 1:-1] = img
    for x in range(img.shape[1]):  
        for y in range(img.shape[0]):
            new[y,x]=(mask*aux[y:y+3,x:x+3]).sum()        
    return new
    
    
def maskBlur():
    mask =  1/16 * np.array([[1., 2., 1.], [2., 4., 2.], [1., 2., 1.]])
    return mask
    
def setSquare3():
    Square = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    return Square
    
def setCross3():
    Cross = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    return Cross    

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
    histeq = np.array([[cdf[pixel] for pixel in img[n]] for n in range(len(img))])
    return histeq
    

    
#    if(len(hist) == 1):
#       showhist = plt.hist(hist, bins = bin)

    imgplot = showhist
    plt.show()
    return None

# Unit Test


def main(args):
    str = "11.png"
    imreadgray(str)


if __name__ == "__main__":
    main(sys.argv)