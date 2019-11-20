import numpy as np

def rgb2gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])


# -- Projet : Etape 1 --

# Seuillage
def threshold_high(img, thresh):
    #print("this is a threshold function")
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
#    if(im1.shape != im2.shape):
#        #print("error both image do not have the same shape")
#        continue
#    else:
     if(im1.shape == im2.shape):
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

def erosion(img, elemStruct):
    # Vérifions si l'élément structurant est correct
    if(not checkFiltre(elemStruct)): # si il n'est pas correct alors fin
      print ("L'élément structurant n'est pas correct")
      return False
  
    backup = np.copy(img)
    res = np.zeros((img.shape))
    
    rayon_elemStruct = int((elemStruct.shape[0]-1)/2)
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # do something here
            lower_value = i-rayon_elemStruct
            upper_value = i+rayon_elemStruct+1
            
            if(lower_value < 0):
                lower_value = 0
            if(upper_value < 0):
                upper_value = 0
            
            slice = backup[lower_value:upper_value, j-rayon_elemStruct:j+rayon_elemStruct+1]
            
            if(np.count_nonzero(slice) != 0):
                #print("(",i,";",j,")")
                if(np.count_nonzero(elemStruct) != np.count_nonzero(slice)):
                    res[i,j] = 0
                else:
                    res[i,j] = 1
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

def dilatation(img, elemStruct):
    # Vérifions si l'élément structurant est correct
    if(not checkFiltre(elemStruct)): # si il n'est pas correct alors fin
      print ("L'élément structurant n'est pas correct")
      return False
  
    backup = np.copy(img)
    res = np.zeros((img.shape))
    
    rayon_elemStruct = int((elemStruct.shape[0]-1)/2)
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            # do something here
            lower_value = i-rayon_elemStruct
            upper_value = i+rayon_elemStruct+1
            
            if(lower_value < 0):
                lower_value = 0
            if(upper_value < 0):
                upper_value = 0
            
            slice = backup[lower_value:upper_value, j-rayon_elemStruct:j+rayon_elemStruct+1]
            #print("(",i, ";", j,")\n", slice)
            
            # Vérifions a présent si les 1 de l'élément structurant touchent des 1 de l'image
            #.. Si le slice n'a pas de 0 inutile de vérifier
            if(np.count_nonzero(slice) != 0):
                #print("(",i,";",j,")")
                if(np.count_nonzero(addition(slice,elemStruct)) != 0):
                    res[i,j] = 1
            
    return res

def checkFiltre(filtre):
    # Verifions si le filtre est de forme carré
    if(filtre.shape[0] != filtre.shape[1]):
        return False
    
    # Verifions que le filtre est de taille impaire
    if((filtre.shape[0] % 2) != 1):
        return False
        
    # Verifions que le centre du carré est à 1
    if(filtre[int((filtre.shape[0]-1)/2),int((filtre.shape[1]-1)/2)] != 1):
        return False
    
    return True
    

# Ouverture = erosion + dilatation
def ouverture(img):
    backup = np.copy(img)
    res = erosion3x3(img)
    res = dilatation3x3(res)
    return res;
    
# Fermeture = dilatation + erosion
def fermeture(img):
    backup = np.copy(img)
    res = dilatation3x3(img)
    res = erosion3x3(res)
    return res;
    
# Amincissement
# Epaississement
    

# Gen d'image binaire test
def genPerfectSquare():
    #shape is 16x16
    res = np.zeros((16,16))
    
    # Carré blanc
    res[6][4] = 1
    res[7][4] = 1
    res[8][4] = 1
    res[9][4] = 1
    
    res[6][5] = 1
    res[7][5] = 1
    res[8][5] = 1
    res[9][5] = 1
    
    res[6][6] = 1
    res[7][6] = 1
    res[8][6] = 1
    res[9][6] = 1
    
    res[6][7] = 1
    res[7][7] = 1
    res[8][7] = 1
    res[9][7] = 1
    return res

def genPerfectSquareWithArgs(shape, startX, startY, width, height):
    res = np.zeros(shape)
    for i in range(width):
        for j in range(height):
            res[startX + i][startY + j] = 1
    
    return res

def genSqareWithHole():
    res = genPerfectSquare()
    
    res[7][5] = 0
    res[7][6] = 0
    
    return res









