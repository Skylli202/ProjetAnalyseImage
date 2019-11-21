# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 19:30:53 2019

@author: Skylli
"""

# =============================================================================
# Import
# =============================================================================

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import functionPresentation as f

# =============================================================================
# File
# =============================================================================
file1 = './ressource/bin1.png'
file2 = './ressource/bin2.png'
file3 = './ressource/logo_couleur.png'
file4 = './ressource/swTrooper.png'
file5 = './ressource/sw9.png'
lenna = './ressource/lenna.png'

# =============================================================================
# Element Structurant
# =============================================================================
B1 = np.ones((1,1))
B3 = np.ones((3,3))
B5 = np.ones((5,5))
B7 = np.ones((7,7))
B9 = np.ones((9,9))
B11 = np.ones((11,11))

# =============================================================================
# Seuillage
# =============================================================================
#f.demoThreshold(lenna, 120)

# =============================================================================
# Addition
# =============================================================================
#f.demoAddition()

# =============================================================================
# Soustraction
# =============================================================================
#f.demoSoustraction()

# =============================================================================
# Erosion
# =============================================================================
#f.demoErosionBasique()
#f.demoErosionBasiquePlot()
#f.demoErosionImage(lenna, 120, B3)

# =============================================================================
# Dilatation
# =============================================================================
#f.demoDilatationBasique()
#f.demoDilatationBasiquePlot()
#f.demoDilatationImage(lenna, 120, B3)

# =============================================================================
# Ouverture
# =============================================================================
#f.demoOuvertureBasique()
#f.demoOuvertureBasiquePlot()
#f.demoOuvertureImage(lenna, 120, B3)

# =============================================================================
# Fermeture
# =============================================================================
#f.demoFermetureBasique()
#f.demoFermetureBasiquePlot()
#f.demoFermetureImage(lenna, 120, B3)

# =============================================================================
# Amincissement
# =============================================================================

# =============================================================================
# Epaississement
# =============================================================================
#f.demoEpaississementBasique()
#f.demoEpaississementBasiquePlot()
#f.demoEpaississementImage(lenna, 120)

# =============================================================================
# Squelettisation par la méthode de Lantuejoul
# =============================================================================
#f.demoSqLantuejoulSquare(3) #Rang 3 suffisant
#f.demoSqLantuejoulRectangle(500) # start at 3 - end at 
f.demoSqLantuejoulImg(lenna, 120, 200)

# =============================================================================
# Squelettisation par la méthode de l'amincissement homothopique
# =============================================================================
#f.demoSqAminHomothophiqueSquare()
#f.demoSqAminHomothophiqueRectangle()
#f.demoSqAminHomothophiqueImg(lenna, 120)