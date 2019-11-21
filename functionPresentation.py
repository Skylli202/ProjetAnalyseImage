# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 19:31:46 2019

@author: Skylli
"""
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import function as func

# =============================================================================
# Threshold, addition et soustraction
# =============================================================================
def demoThreshold(fname, threshold):
    image = Image.open(fname).convert("L")
    print("Image de départ (niveau de gris) :")
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.show()
    
    img = np.array(image)
    
    imgThreshold = func.threshold_high(img, threshold)
    print("Image binarisée :")
    plt.imshow(imgThreshold, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
def demoAddition():
    im1 = np.zeros((2,2))
    im2 = np.zeros((2,2))
    im1[1,0] = 1
    im1[1,1] = 1
    im2[0,1] = 1
    im2[1,1] = 1
    
    print("im1 : \n", im1)
    print("im2 : \n", im2)
    
    im3 = func.addition(im1, im2)
    print("im1 + im2 :\n",im3)
    
def demoSoustraction():
    im1 = np.zeros((2,2))
    im2 = np.zeros((2,2))
    im1[1,0] = 1
    im1[1,1] = 1
    im2[0,1] = 1
    im2[1,1] = 1
    
    print("im1 : \n", im1)
    print("im2 : \n", im2)
    
    im3 = func.soustraction(im1, im2)
    print("im1 - im2 :\n",im3)
    
# =============================================================================
#    Erosion 
# =============================================================================
def demoErosionBasique():
    img = np.zeros((8,8))
    img[2:6,2:6] = 1
    
    elemStruct = np.ones((3,3))
    
    imgErosion = func.erosion(img, elemStruct)
    
    #display
    print("img :\n",img)
    print("\nE(img) :\n",imgErosion)
    
def demoErosionBasiquePlot():
    img = np.zeros((8,8))
    img[2:6,2:6] = 1
    
    elemStruct = np.ones((3,3))
    
    imgErosion = func.erosion(img, elemStruct)
    
    #display
    print("img :\n")
    plt.imshow(img, cmap='gray', vmin=0, vmax=1)
    plt.show()
    print("E(img) :\n")
    plt.imshow(imgErosion, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
def demoErosionImage(fname, threshold ,elemStruct):
    image = Image.open(fname).convert("L")
    print("Image de départ (niv. gris):")
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.show()
    
    img = np.array(image)
    imgBin = func.threshold_high(img, threshold)
    if(fname != './ressource/bin2.png' and fname != './ressource/bin1.png'):
        imgBin = func.invert(imgBin)
    print("Image binariser avec un seuil de ", threshold,".")
    plt.imshow(imgBin, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    print("img érodée")
    imgEro = func.erosion(imgBin,elemStruct)
    plt.imshow(imgEro, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
# =============================================================================
#   Dilatation  
# =============================================================================
def demoDilatationBasique():
    img = np.zeros((8,8))
    img[2:6,2:6] = 1
    
    elemStruct = np.ones((3,3))
    
    imgDilate = func.dilatation(img, elemStruct)
    
    #display
    print("img :\n",img)
    print("\nD(img) :\n",imgDilate)
    
def demoDilatationBasiquePlot():
    img = np.zeros((8,8))
    img[2:6,2:6] = 1
    
    elemStruct = np.ones((3,3))
    
    imgDilate = func.dilatation(img, elemStruct)
    
    #display
    print("img :\n")
    plt.imshow(img, cmap='gray', vmin=0, vmax=1)
    plt.show()
    print("D(img) :\n")
    plt.imshow(imgDilate, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
def demoDilatationImage(fname, threshold ,elemStruct):
    image = Image.open(fname).convert("L")
    print("Image de départ (niv. gris):")
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.show()
    
    img = np.array(image)
    imgBin = func.threshold_high(img, threshold)
    if(fname != './ressource/bin2.png' and fname != './ressource/bin1.png'):
        imgBin = func.invert(imgBin)
    print("Image binariser avec un seuil de ", threshold,".")
    plt.imshow(imgBin, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    print("img dilatée")
    imgDilate = func.dilatation(imgBin,elemStruct)
    plt.imshow(imgDilate, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
# =============================================================================
# Ouverture
# =============================================================================
def demoOuvertureBasique():
    img = np.zeros((8,8))
    img[2:6,2:6] = 1
    
    elemStruct = np.ones((3,3))
    
    imgOpen = func.ouverture(img, elemStruct)
    
    #display
    print("img :\n",img)
    print("\nO(img) :\n",imgOpen)
    
def demoOuvertureBasiquePlot():
    img = np.zeros((8,8))
    img[2:6,2:6] = 1
    
    elemStruct = np.ones((3,3))
    
    imgOpen = func.ouverture(img, elemStruct)
    
    #display
    print("img :\n")
    plt.imshow(img, cmap='gray', vmin=0, vmax=1)
    plt.show()
    print("O(img) :\n")
    plt.imshow(imgOpen, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
def demoOuvertureImage(fname, threshold ,elemStruct):
    image = Image.open(fname).convert("L")
    print("Image de départ (niv. gris):")
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.show()
    
    img = np.array(image)
    imgBin = func.threshold_high(img, threshold)
    if(fname != './ressource/bin2.png' and fname != './ressource/bin1.png'):
        imgBin = func.invert(imgBin)
    print("Image binariser avec un seuil de ", threshold,".")
    plt.imshow(imgBin, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    print("img ouverte")
    imgOpen = func.dilatation(imgBin,elemStruct)
    plt.imshow(imgOpen, cmap='gray', vmin=0, vmax=1)
    plt.show()   
    
# =============================================================================
# Ouverture
# =============================================================================
def demoFermetureBasique():
    img = np.zeros((8,8))
    img[2:6,2:6] = 1
    
    elemStruct = np.ones((3,3))
    
    imgClose = func.fermeture(img, elemStruct)
    
    #display
    print("img :\n",img)
    print("\nC(img) :\n",imgClose)
    
def demoFermetureBasiquePlot():
    img = np.zeros((8,8))
    img[2:6,2:6] = 1
    
    elemStruct = np.ones((3,3))
    
    imgClose = func.fermeture(img, elemStruct)
    
    #display
    print("img :\n")
    plt.imshow(img, cmap='gray', vmin=0, vmax=1)
    plt.show()
    print("C(img) :\n")
    plt.imshow(imgClose, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
def demoFermetureImage(fname, threshold ,elemStruct):
    image = Image.open(fname).convert("L")
    print("Image de départ (niv. gris):")
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.show()
    
    img = np.array(image)
    imgBin = func.threshold_high(img, threshold)
    if(fname != './ressource/bin2.png' and fname != './ressource/bin1.png'):
        imgBin = func.invert(imgBin)
    print("Image binariser avec un seuil de ", threshold,".")
    plt.imshow(imgBin, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    print("img fermée")
    imgClose = func.fermeture(imgBin,elemStruct)
    plt.imshow(imgClose, cmap='gray', vmin=0, vmax=1)
    plt.show()

# =============================================================================
# Amincissement
# =============================================================================
def demoAmincissementBasique():
    img = np.zeros((9,9))
    img[2:7,2:7] = 1
    
    imgThin = func.amincissement(img)
    
    #display
    print("img :\n",img)
    print("\nThin(img) :\n",imgThin)
    
def demoAmincissementBasiquePlot():
    img = np.zeros((9,9))
    img[2:7,2:7] = 1
    
    imgThin = func.amincissement(img)
    
    #display
    print("img :\n")
    plt.imshow(img, cmap='gray', vmin=0, vmax=1)
    plt.show()
    print("Thin(img) :\n")
    plt.imshow(imgThin, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
def demoAmincissementImage(fname, threshold):
    image = Image.open(fname).convert("L")
    print("Image de départ (niv. gris):")
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.show()
    
    img = np.array(image)
    imgBin = func.threshold_high(img, threshold)
    if(fname != './ressource/bin2.png' and fname != './ressource/bin1.png'):
        imgBin = func.invert(imgBin)
    print("Image binariser avec un seuil de ", threshold,".")
    plt.imshow(imgBin, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    print("img amincie")
    imgThin = func.amincissement(imgBin)
    plt.imshow(imgThin, cmap='gray', vmin=0, vmax=1)
    plt.show()

# =============================================================================
# Epaississement
# =============================================================================
def demoEpaississementBasique():
    img = np.zeros((9,9))
    img[2:7,2:7] = 1
    
    imgThick = func.epaississement(img)
    
    #display
    print("img :\n",img)
    print("\nThick(img) :\n",imgThick)
    
def demoEpaississementBasiquePlot():
    img = np.zeros((9,9))
    img[2:7,2:7] = 1
    
    imgThick = func.epaississement(img)
    
    #display
    print("img :\n")
    plt.imshow(img, cmap='gray', vmin=0, vmax=1)
    plt.show()
    print("Thick(img) :\n")
    plt.imshow(imgThick, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
def demoEpaississementImage(fname, threshold):
    image = Image.open(fname).convert("L")
    print("Image de départ (niv. gris):")
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.show()
    
    img = np.array(image)
    imgBin = func.threshold_high(img, threshold)
    if(fname != './ressource/bin2.png' and fname != './ressource/bin1.png'):
        imgBin = func.invert(imgBin)
    print("Image binariser avec un seuil de ", threshold,".")
    plt.imshow(imgBin, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    print("img épaissie")
    imgThick = func.epaississement(imgBin)
    plt.imshow(imgThick, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
# =============================================================================
# Squelettisation par la méthode de Lantuejoul
# =============================================================================
def demoSqLantuejoulSquare(rang):
    img = np.zeros((9,9))
    img[2:7,2:7] = 1
    
    imgSq = func.squeletteWithLantuejoul(img, rang)
    
    #display
    print("img :\n",img)
    print("\nSq(img) :\n",imgSq)
    
def demoSqLantuejoulRectangle(rang):
    img = np.zeros((64,64))
    img[12:33,5:60] = 1
    
    imgSq = func.squeletteWithLantuejoul(img, rang)
    
    #display
    print("img :\n")
    plt.imshow(img, cmap='gray', vmin=0, vmax=1)
    plt.show()
    print("\nSq(img) [Lantuejoue]:\n")
    plt.imshow(imgSq, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
def demoSqLantuejoulImg(fname, threshold, rang):
    image = Image.open(fname).convert("L")
    print("Image de départ (niv. gris):")
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.show()
    
    img = np.array(image)
    imgBin = func.threshold_high(img, threshold)
    if(fname != './ressource/bin2.png' and fname != './ressource/bin1.png'):
        imgBin = func.invert(imgBin)
    print("Image binariser avec un seuil de ", threshold,".")
    plt.imshow(imgBin, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    print("img squelette [Lantuejoue]:")
    imgSq = func.squeletteWithLantuejoul(imgBin, rang)
    plt.imshow(imgSq, cmap='gray', vmin=0, vmax=1)
    plt.show()

# =============================================================================
# Squelettisation par la méthode de l'amincissement homothopique
# =============================================================================
def demoSqAminHomothophiqueSquare():
    img = np.zeros((9,9))
    img[2:7,2:7] = 1
    
    imgSq = func.squeletteWithThinHomothopique(img)
    
    #display
    print("img :\n",img)
    print("\nSq(img) :\n",imgSq)
    
def demoSqAminHomothophiqueRectangle():
    img = np.zeros((64,64))
    img[12:33,5:60] = 1
    
    imgSq = func.squeletteWithThinHomothopique(img)
    
    #display
    print("img :\n")
    plt.imshow(img, cmap='gray', vmin=0, vmax=1)
    plt.show()
    print("\nSq(img) [Amin. Homothopique]:\n")
    plt.imshow(imgSq, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
def demoSqAminHomothophiqueImg(fname, threshold):
    image = Image.open(fname).convert("L")
    print("Image de départ (niv. gris):")
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.show()
    
    img = np.array(image)
    imgBin = func.threshold_high(img, threshold)
    if(fname != './ressource/bin2.png' and fname != './ressource/bin1.png'):
        imgBin = func.invert(imgBin)
    print("Image binariser avec un seuil de ", threshold,".")
    plt.imshow(imgBin, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    print("img squelette [Amin. Homothopique]:")
    imgSq = func.squeletteWithThinHomothopique(imgBin)
    plt.imshow(imgSq, cmap='gray', vmin=0, vmax=1)
    plt.show()