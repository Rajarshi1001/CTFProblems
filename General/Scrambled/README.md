# Scrambled

The link results in two images which consists of white noice named as __scrambled1.png__, 
__scramble2.png__. I have written a python script which adds the pixels values of the 
two images and produces the resultant image in __result.png__.

```python
import numpy as np
from PIL import Image, ImageOps

i1 = ImageOps.grayscale(Image.open("scrambled1.png"))
i2 = ImageOps.grayscale(Image.open("scrambled2.png"))
arr1 = np.asarray(i1)
arr2 = np.asarray(i2)

img = arr1 + arr2
data = Image.fromarray(img)
data.save("result.png")
```
The flag is available in __result.png__