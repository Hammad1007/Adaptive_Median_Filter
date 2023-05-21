# Libraries
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np

# open the image file
image = Image.open("cam.jpg")

print("Width: ", image.size[0])
print("Height: ", image.size[1])

# show the image in a new window
image.show()

# Take user input
main_size = int(input("Enter the window size: "))
salt = float(input("Enter the probability of salt: "))
pepper = float(input("Enter the probability of pepper: "))

# Adaptive Median Filter

def adaptive_median_filter(image_array, main_size):
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


# Open the file on the screen
def open_file():
    global img_path, original_image
    img_path = filedialog.askopenfilename()
    original_image = Image.open(img_path).convert('L')
    show_image(original_image)
    image_array = np.array(original_image)
    noisy_image_array = add_salt_pepper_noise(image_array, salt, pepper)
    noisy_image = Image.fromarray(noisy_image_array)
    show_image(noisy_image)


# Apply the median filter after opening the image
def apply_filter():
    global img_path
    image = Image.open(img_path).convert('L')
    # show_image(image)
    image_array = np.array(image)
    filtered_image_array = adaptive_median_filter(image_array, main_size)
    filtered_image = Image.fromarray(filtered_image_array)
    show_image(filtered_image)

# Function to print the image on screen
def show_image(image):
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    canvas.image = photo

# Create main 
main = tk.Tk()
main.title("Assignment 3:   Hammad Rashid     19L-1007")

# Print the text on the screen
text1 = tk.Label(main, text="Adaptive Median Filter", font=("Times Roman", 12, "bold "), fg="blue")
text1.pack(padx=15, pady=15)

# Create canvas to display image
canvas = tk.Canvas(main, width=500, height=500)
canvas.pack()

# Create a button to open an image file
open_button = tk.Button(main, text="Select an Image", command=open_file)
open_button.pack(padx=10, pady=10)


# Create a button to apply the filter
# filter_button = tk.Button(main, text="Apply Filter", command=apply_filter)
# filter_button.pack(padx=10, pady=10)

# Main runs here
main.mainloop()
