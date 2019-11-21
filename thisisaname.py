# =============================================================================
# Import
# =============================================================================
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

import function as f
import testLib as test


# =============================================================================
# Ressource
file1 = './ressource/bin1.png'
file2 = './ressource/bin2.png'
file3 = './ressource/logo_couleur.png'
file4 = './ressource/swTrooper.png'
file5 = './ressource/sw9.png'
# =============================================================================

# =============================================================================
# -- main --
# =============================================================================


#test.displayTestAddition()
#test.displayTestSoustraction()
#test.displayTestWikiEro3x3()
#test.displayTestWikiDila3x3()
# fname = bin2
#test.testEroDilaOpenCloseWithRealImage(fname)
#test.testOpenCloseWithBinaryArray()
#test.testDilatationErosion() # Fermeture
#test.testErosionDilatation() # Ouverture
#test.testCheckFiltre()
#test.testDilatation()
#test.testErosion()
#test.testFinalPart1()

#img = np.zeros((8,8))
#img[2:6,2:6] = 1
#plt.imshow(img, cmap='gray', vmin=0, vmax=1)
#plt.show()
#
#elemStruct = np.ones((3,3))
#
#imgDilatation = f.dilatation(img, elemStruct)
#plt.imshow(imgDilatation, cmap='gray', vmin=0, vmax=1)
#plt.show()

imgBin = np.zeros((16,16))
imgBin[4:13,4:13] = 1
plt.imshow(imgBin, cmap='gray', vmin=0, vmax=1)
plt.show()

fname = file3
image = Image.open(fname).convert("L")
print("Image de départ :")
plt.imshow(image, cmap='gray', vmin=0, vmax=255)
plt.show()

img = np.array(image)
threshold = 200
imgBin = f.threshold_high(img, threshold)
imgBin = f.invert(imgBin)
print("Image binariser avec un seuil de ", threshold)
plt.imshow(imgBin, cmap='gray', vmin=0, vmax=1)
plt.show()

print("img sq lantuejoul")
imgSq = f.erosion(imgBin,np.ones((3,3)))
plt.imshow(imgSq, cmap='gray', vmin=0, vmax=1)
plt.show()
























