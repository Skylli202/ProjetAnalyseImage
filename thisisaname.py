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

img = np.zeros((64,64))
img[16:48,16:48] = 1
plt.imshow(img, cmap='gray', vmin=0, vmax=1)
plt.show()

imgAmin = f.amincissement(img)
plt.imshow(imgAmin, cmap='gray', vmin=0, vmax=1)
plt.show()

imgAmin2 = f.amincissement(imgAmin)
plt.imshow(imgAmin2, cmap='gray', vmin=0, vmax=1)
plt.show()

imgAmin3 = f.amincissement(imgAmin2)
plt.imshow(imgAmin3, cmap='gray', vmin=0, vmax=1)
plt.show()
























