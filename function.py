import numpy as np

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


# -- Projet : Etape 1 --

# Seuillage
def threshold_high(img, thresh):
    print("this is a threshold function")
    res = np.copy(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if(res[i][j] > thresh):
                res[i][j] = 1
            else:
                res[i][j] = 0
    return res


def threshold_low(img, thresh):
    res = np.copy(img)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if(res[i][j] < thresh):
                res[i][j] = 0
            else:
                res[i][j] = 1
    return res

def threshold_auto(img):
    print("later")

# Addition
def addition(im1, im2):
    if(im1.shape != im2.shape):
        print("error both image do not have the same shape")
    else:
        #shape are equals
        res = np.zeros(im1.shape)
        for i in range(im1.shape[0]):
            for j in range(im1.shape[0]):
                px1 = im1[i][j]
                px2 = im2[i][j]
                if(px1 == 0 and px2 == 0):
                    res[i,j] = 0
                else:
                    res[i,j] = 1
        return res


# Soustraction
def soustraction(im1, im2):
    if(im1.shape != im2.shape):
        print("error both image do not have the same shape")
    else:
        #shape are equals
        res = np.zeros(im1.shape)
        for i in range(im1.shape[0]):
            for j in range(im1.shape[0]):
                px1 = im1[i][j]
                px2 = im2[i][j]
                if(px1 == 1 and px2 == 0):
                    res[i,j] = 1
                else:
                    res[i,j] = 0
        return res

# Erosion
def erosion3x3(img):
    elemStruct = np.ones((3,3))

    res = np.copy(img)
    backup = np.copy(img)

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            slice = backup[i-1:i+2,j-1:j+2]
            #print(slice)
            if((np.count_nonzero(elemStruct) - np.count_nonzero(slice)) == 0):
                continue
            else:
                res[i,j] = 0
                
    # Ne vérifie pas que les 1 soient au même endroit dans slice qu'ils ne le soient dans l'element structurant

    return res

# Dilatation
def dilatation3x3(img):
    backup = np.copy(img)
    res = np.zeros((img.shape))

    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            x = i-1
            y = j-1
            if(x<0):
                x=0
            if(y<0):
                y=0
            slice = backup[x:i+2,y:j+2]
            #print("--- \n", i, " ", j, "\n", slice, "\n", np.count_nonzero(slice))
            if(np.count_nonzero(slice) != 0):
                res[i,j] = 1
            else:
                res[i,j] = 0
                
    # Ne vérifie pas que les 1 soient au même endroit dans slice qu'ils ne le soient dans l'element structurant
    
    return res
