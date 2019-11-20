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
file3 = './ressource/logo_couleur.jpg'
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

img = np.zeros((8,8))
img[2:6,2:6] = 1

plt.imshow(img, cmap='gray', vmin=0, vmax=1)
plt.show()

elemStruct = np.ones((3,3))
elemStruct[0,0] = 0
elemStruct[0,2] = 0
elemStruct[2,0] = 0
elemStruct[2,2] = 0
print(elemStruct)

imgEro = f.erosion(img, elemStruct)
plt.imshow(imgEro, cmap='gray', vmin=0, vmax=1)
plt.show()