import numpy as np
import matplotlib.pyplot as plt

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

def invert(img):
    res = np.zeros((img.shape))
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if(img[i,j] == 0):
                res[i,j] = 1
            else:
                res[i,j] = 0
    return res

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
#    if(im1.shape != im2.shape):
#        print("error both image do not have the same shape")
#    else:
    
     if(im1.shape == im2.shape):
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
  
    if(elemStruct.shape[0]*elemStruct.shape[1] != np.count_nonzero(elemStruct)):
        print("Warrning : elemStruct isn't fithfull with ones, function.erosion might not work properly")
        
    backup = np.copy(img)
    res = np.copy((img))
    
    rayon_elemStruct = int((elemStruct.shape[0]-1)/2)
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
                        
            slice = backup[i-rayon_elemStruct:i+rayon_elemStruct+1, j-rayon_elemStruct:j+rayon_elemStruct+1]
            
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

def dilatation(img, elemStruct):
    # Vérifions si l'élément structurant est correct
    if(not checkFiltre(elemStruct)): # si il n'est pas correct alors fin
      print ("L'élément structurant n'est pas correct")
      return False
  
    backup = np.copy(img)
    res = np.copy(img)
    
    rayon_elemStruct = int((elemStruct.shape[0]-1)/2)
    
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            
#            slice = backup[i-rayon_elemStruct:i+rayon_elemStruct+1, j-rayon_elemStruct:j+rayon_elemStruct+1]
#            if(np.count_nonzero(slice) != 0):
#                #print("(",i,";",j,")")
#                if(np.count_nonzero(addition(slice,elemStruct)) != 0):
#                    res[i,j] = 1
            
            if(backup[i,j] == 1):
                slice = backup[i-rayon_elemStruct:i+rayon_elemStruct+1, j-rayon_elemStruct:j+rayon_elemStruct+1]
                res[i-rayon_elemStruct:i+rayon_elemStruct+1, j-rayon_elemStruct:j+rayon_elemStruct+1] = 1
            
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
def ouverture3x3(img):
    res = erosion3x3(img)
    res = dilatation3x3(res)
    return res

def ouverture(img, elemStruct):
    res = erosion(img, elemStruct)
    res = dilatation(res, elemStruct)
    return res
    
# Fermeture = dilatation + erosion
def fermeture3x3(img):
    res = dilatation3x3(img)
    res = erosion3x3(res)
    return res

def fermeture(img, elemStruct):
    res = dilatation(img, elemStruct)
    res = erosion(res, elemStruct)
    return res
# =============================================================================
# # Amincissement
# ============================================================================
def amincissement(img):
    L1 = np.array([[1,1,1],[2,1,2],[0,0,0]])
    L2 = np.array([[2,1,1],[0,1,1],[0,0,2]])
    L3 = np.array([[0,2,1],[0,1,1],[0,2,1]])
    L4 = np.array([[0,0,2],[0,1,1],[2,1,1]]) 
    L5 = np.array([[0,0,0],[2,1,2],[1,1,1]]) 
    L6 = np.array([[2,0,0],[1,1,0],[1,1,2]]) 
    L7 = np.array([[1,2,0],[1,1,0],[1,2,0]]) 
    L8 = np.array([[1,1,2],[1,1,0],[2,0,0]]) 
    
    LFamily = np.array([L1, L2, L3, L4, L5, L6, L7, L8])
    
    backup = np.copy(img)
    res = np.copy(img)
    
    for x in range(LFamily.shape[0]):
        for i in range(1, img.shape[0]-1):
            for j in range(1, img.shape[1]-1):
                slice = backup[i-1:i+2,j-1:j+2]
            
                cpt = 0
                for a in range(slice.shape[0]):
                    for b in range(slice.shape[1]):
                        L = LFamily[x]
                        if(L[a,b] != 2):
                            if(L[a,b] == slice[a,b]):
                                cpt = 1 + cpt
                if(cpt == 7):
#                    print("(",i,";",j,")")
                    res[i,j] = 0
        backup = np.copy(res)
                
                               
    return res
            
            
# =============================================================================
# Epaississement
# =============================================================================
def epaississement(img):
    L1 = np.array([[1,1,1],[2,0,2],[0,0,0]])
    L2 = np.array([[2,1,1],[0,0,1],[0,0,2]])
    L3 = np.array([[0,2,1],[0,0,1],[0,2,1]])
    L4 = np.array([[0,0,2],[0,0,1],[2,1,1]]) 
    L5 = np.array([[0,0,0],[2,0,2],[1,1,1]]) 
    L6 = np.array([[2,0,0],[1,0,0],[1,1,2]]) 
    L7 = np.array([[1,2,0],[1,0,0],[1,2,0]]) 
    L8 = np.array([[1,1,2],[1,0,0],[2,0,0]]) 
    
    LFamily = np.array([L1, L2, L3, L4, L5, L6, L7, L8])
        
    backup = np.copy(img)
    res = np.copy(img)
    
    for x in range(LFamily.shape[0]):
        for i in range(1, img.shape[0]-1):
            for j in range(1, img.shape[1]-1):
                slice = backup[i-1:i+2,j-1:j+2]
            
                cpt = 0
                for a in range(slice.shape[0]):
                    for b in range(slice.shape[1]):
                        L = LFamily[x]
                        if(L[a,b] != 2):
                            if(L[a,b] == slice[a,b]):
                                cpt = 1 + cpt
                if(cpt == 7):
                    res[i,j] = 1
        backup = np.copy(res)
                
                               
    return res

# =============================================================================
# Squelette
# =============================================================================
def squeletteWithLantuejoul(img, rang):
    backup = np.copy(img)
    res = np.zeros((img.shape))
    
    B = np.ones((3,3))
    
    for i in range(0,rang):
        lambdaB = np.ones(((i*2)+1,(i*2)+1))
#        lambdaB = np.ones((3,3))
#        print("Lambda B :\n",lambdaB)
        
        imgEroLambdaB = erosion(backup, lambdaB)
#        print("Erosion :\n",imgEroLambdaB)
        
        imgOpen = ouverture(imgEroLambdaB, B)
#        print("Open :\n",imgOpen)
        
        res += soustraction(imgEroLambdaB, imgOpen) 
        
    return res
    

def squeletteWithThinHomothopique(img):
    backup = np.copy(img)
    res = np.copy(amincissement(img))
    while(not(np.array_equal(backup,res))):
        backup = np.copy(res)
        res = np.copy(amincissement(res))
#        plt.imshow(res, cmap='gray', vmin=0, vmax=1)
#        plt.show()
    return res




























