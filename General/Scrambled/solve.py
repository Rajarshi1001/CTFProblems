

import numpy as np
from PIL import Image, ImageOps

i1 = ImageOps.grayscale(Image.open("scrambled1.png"))
i2 = ImageOps.grayscale(Image.open("scrambled2.png"))
arr1 = np.asarray(i1)
arr2 = np.asarray(i2)

img = arr1 + arr2
data = Image.fromarray(img)
data.save("result.png")