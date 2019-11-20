#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:43:57 2019

@author: Elouan
"""
# =============================================================================
# Import
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np
import function as f

from PIL import Image

# =============================================================================
# Test Addition
# =============================================================================
def genAdditionSample():
    im1 = np.zeros((2,2))
    im2 = np.zeros((2,2))
    im1[0,0] = 1
    im2[1,1] = 1
    return im1, im2

def testAddition(im1, im2):
    additionDone = f.addition(im1,im2)
    return additionDone

def displayTestAddition():
    data = genAdditionSample()
    print(testAddition(data[0], data[1]), "\n")

# =============================================================================
# Soustraction
# =============================================================================
def genSoustractionSample():
    im1 = np.ones((2,2))
    im2 = np.zeros((2,2))
    im1[1,0] = 0
    im1[1,1] = 0
    
    im2[1,0] = 1
    im2[0,0] = 1
    return [im1, im2]

def testSoustraction(im1, im2):
    soustractionDone = f.soustraction(im1, im2)
    return soustractionDone

def displayTestSoustraction():
    data = genSoustractionSample()
    print(testSoustraction(data[0], data[1]), "\n")

# =============================================================================
# Wiki exemple : https://en.wikipedia.org/wiki/Erosion_(morphology)
# =============================================================================
def genWikiErosion():    
    wikiErosion = np.ones((13,13))
    wikiErosion[1,6] = 0
    return wikiErosion

def testErosion3x3(img):
    wikiErosionDone = f.erosion3x3(img)
    return wikiErosionDone

def displayTestWikiEro3x3():
    print(testErosion3x3(genWikiErosion()), "\n")
    
# =============================================================================
# Wiki exemple : https://en.wikipedia.org/wiki/Dilation_(morphology)
# =============================================================================
def genWikiDilatation():
    wikiDilatation = np.ones((11,11))
    for i in range(0, wikiDilatation.shape[0]):
        wikiDilatation[i,0] = 0
        wikiDilatation[0,i] = 0
        wikiDilatation[i,10] = 0
        wikiDilatation[10,i] = 0
    wikiDilatation[1,5] = 0
    wikiDilatation[1,6] = 0
    wikiDilatation[2,5] = 0
    wikiDilatation[2,6] = 0
    
    wikiDilatation[6,3] = 0
    wikiDilatation[6,4] = 0
    wikiDilatation[6,5] = 0
    wikiDilatation[7,3] = 0
    wikiDilatation[7,4] = 0
    wikiDilatation[7,5] = 0
    wikiDilatation[8,3] = 0
    wikiDilatation[8,4] = 0
    wikiDilatation[8,5] = 0
    
    wikiDilatation[8,9] = 0
    wikiDilatation[8,8] = 0
    wikiDilatation[9,9] = 0
    wikiDilatation[9,8] = 0
    return wikiDilatation

def testDilatation3x3(img):
    wikiDilatationDone = f.dilatation3x3(img)
    return wikiDilatationDone

def displayTestWikiDila3x3():
    print(testDilatation3x3(genWikiDilatation()), "\n")
 

def testEroDilaOpenCloseWithRealImage(fname):
    image = Image.open(fname).convert("L")
    print("Image de départ :")
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.show()
    
    # Conversion en numpy.array
    arr = np.asarray(image)
    carr = np.copy(arr)
    
    # Conversion en image binaire
    carr = f.threshold_low(carr, 128)
    print("Image binarisée :")
    plt.imshow(carr, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    # Erosion de l'image
    imgErosion = f.erosion3x3(carr)
    print("Image érodée :")
    plt.imshow(imgErosion, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    # Dilatation de l'image
    imgDilatation = f.dilatation3x3(carr)
    print("Image dilatée :")
    plt.imshow(imgDilatation, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    # Ouverture de l'image
    imgOuverture = f.ouverture(carr)
    print("Image Ouverte : ")
    plt.imshow(imgOuverture, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    # Fermeture d'une image
    imgFermeture = f.fermeture(carr)
    print("Image fermée : ")
    plt.imshow(imgFermeture, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
def testOpenCloseWithBinaryArray():
    # Création de l'image
    img1 = f.genPerfectSquareWithArgs((16,16), 3, 10, 5, 5)
    
    # Créons un troue que la fermeture devrait fermer et l'ouverture agrandir
    img1[4][11] = 0
    
    # Créons une excroissance que la fermeture devrai adoussir 
    img1[8][13] = 1
    
    #print (img1)
    
    print("Image de départ : ")
    plt.imshow(img1, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    # Fermeture
    img1Close = f.fermeture(img1)
    print("Fermeture : ")
    plt.imshow(img1Close, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    # Ouverture
    img1Open = f.ouverture(img1)
    print("Ouverture : ")
    plt.imshow(img1Open, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
def testDilatationErosion():
    square = np.zeros((16,16))
    square[2:7,2:7] = 1
    square[3,3] = 0
    print("Image de départ : ")
    plt.imshow(square, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    squareDilatation = f.dilatation3x3(square)
    print("Dilatation de l'image : ")
    plt.imshow(squareDilatation, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    squareErosion = f.erosion3x3(squareDilatation)
    print("Erosion du dilatée de l'image : ")
    plt.imshow(squareErosion, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    print("Fermeture fonctionnel")
    
def testErosionDilatation():
    square = np.zeros((16,16))
    square[2:7,2:7] = 1
    square[3,3] = 0
    print("Image de départ : ")
    plt.imshow(square, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    squareErosion = f.erosion3x3(square)
    print("Erosion de l'image : ")
    plt.imshow(squareErosion, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    squareDilatation = f.dilatation3x3(squareErosion)
    print("Dilatation de l'érodée de l'image : ")
    #plt.imshow(squareDilatation, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    print("Ouverture fonctionnel")
    
# =============================================================================
#  Dilatation   
# =============================================================================
def testCheckFiltre():           
    print (f.checkFiltre(np.ones((1,1))))
    print (f.checkFiltre(np.ones((3,3))))
    print (f.checkFiltre(np.ones((11,11))))
    
    print (f.checkFiltre(np.ones((1,2))))
    print (f.checkFiltre(np.ones((4,4))))
    filtre = np.ones((3,3))
    filtre[1,1] = 0
    print (f.checkFiltre(filtre))
    
    print ("Expected : true true true false false false")
    
def testDilatation():
    file3 = './ressource/logo_couleur.jpg'
    fname = file3
    image = Image.open(fname).convert("L")
    print("Image de départ :")
    plt.imshow(image, cmap='gray', vmin=0, vmax=255)
    plt.show()
    
    img = np.array(image)
    threshold = 124
    imgBin = f.threshold_high(img, threshold)
    print("Image binariser avec un seuil de ",threshold)
    plt.imshow(imgBin, cmap='gray', vmin=0, vmax=1)
    plt.show()
    
    elemStruct = np.ones((3,3))
    
    imgDilate = f.dilatation(imgBin, elemStruct)
    print("dilatation : ")
    plt.imshow(imgDilate, cmap='gray', vmin=0, vmax=1)
    plt.show()

    
    
    
    
    
    
    
    
    