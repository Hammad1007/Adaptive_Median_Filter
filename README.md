# Digital Image Processing
## Assignment 3: Implementing Adaptive Median Filter

### Language used: 
<b>Python<b>

### Libraries used:

```python
import cv2      
import numpy as np
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk 

```
### Explanation:
The following is the explanation of the code along with code snippets.

#### Image Reading
```python
# open the image file
image = Image.open("cam.jpg")

print("Width: ", image.size[0])
print("Height: ", image.size[1])

# show the image in a new window
image.show()
```
The code above is used to read the file, displays it on the screen and prints its dimensions.


#### Salt and Pepper Noise generation
```python
# Salt and peper noise
def add_salt_pepper_noise(image_array, salt, pepper):
    salt_pepper_array = np.copy(image_array)

    # Add salt noise
    salt_mask = np.random.rand(*image_array.shape) < salt
    salt_pepper_array[salt_mask] = 255

    # Add pepper noise
    pepper_mask = np.random.rand(*image_array.shape) < pepper
    salt_pepper_array[pepper_mask] = 0

    return salt_pepper_array

```

The above code is the one where salt and pepper noise is added to the image. Moreover, the probability of salt and pepper is taken on run time form the user along with the kernel and window size of the image. Adding salt noise and pepper noise separately. 

#### Applying the Filter
```python
padding = main_size // 2
filtered_image = np.zeros_like(image_array)

for i in range(padding, image_array.shape[0]-padding):
    for j in range(padding, image_array.shape[1]-padding):
        main = image_array[i-padding:i+padding+1, j-padding:j+padding+1]
        main_size = main.shape[0] * main.shape[1]

        _min = np.min(main)
        _max = np.max(main)
        _med = np.median(main)

        if _med > _min and _med < _max:
            _xy = image_array[i, j]             # that particular pixel value
            if _xy > _min and _xy < _max:       
                filtered_image[i, j] = _xy
            else:
                filtered_image[i, j] = _med
                
        else:
            main_size = main_size + 1
            padding = main_size // 2
            main = image_array[i-padding:i+padding+1, j-padding:j+padding+1]

            _min = np.min(main)
            _max = np.max(main)
            _med = np.median(main)

            if _med > _min and _med < _max:
                _xy = image_array[i, j]
                if _xy > _min and _xy < _max:
                    filtered_image[i, j] = _xy
                else:
                    filtered_image[i, j] = _med
            else:
                filtered_image[i, j] = _med

return filtered_image
```
The above code is used to determine the adaptive median filter when applied and takes into consideration the algorithm steps. 
