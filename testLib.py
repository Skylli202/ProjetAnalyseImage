#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 14:43:57 2019

@author: Elouan
"""
# =============================================================================
# Import
# =============================================================================
import numpy as np
import function as f

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