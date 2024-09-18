
"""
GitHub Repository

https://github.com/veddahit/Soft_assignment/blob/main/qn2_1st_task.py

"""

import time

current_time = int(time.time())

generated_number = (current_time % 100) + 50

if generated_number %2 ==0:
    generated_number +=10

print(generated_number)    


from PIL import Image

def read_rgb_values(image_path):
    
    image = Image.open(image_path)

    
    rgb_values = list(image.getdata())

    return rgb_values


image_path = r''
rgb_values = read_rgb_values(image_path)


for i in range(min(5, len(rgb_values))):
    print(f"Pixel {i + 1}: {rgb_values[i]}")

import time
from PIL import Image

def read_rgb_values_with_generated_number(image_path):
    
    image = Image.open(image_path)

    
    current_time = int(time.time())

    
    generated_number = (current_time % 100) + 50

    if generated_number % 2 == 0:
        generated_number += 10
    print(generated_number)
    
    rgb_with_generated_number = [
        (pixel[0] + generated_number, pixel[1] + generated_number, pixel[2] + generated_number)
        for pixel in image.getdata()
    ]
   

    return rgb_with_generated_number


image_path = r'C:\Users\USER\Desktop\Software Now_Assignment 2\chapter1.jpg'
rgb_with_generated_number = read_rgb_values_with_generated_number(image_path)

# Display the (x, y, RGB) values of the first few pixels
for i in range(min(5, len(rgb_with_generated_number))):
    print(f"Pixel {i + 1}: {rgb_with_generated_number[i]}")

output_image_path = r'C:\Users\USER\Desktop\Software Now_Assignment 2\Assignment_2\outputs\chapter1output.jpg'

import time
from PIL import Image

def read_rgb_values_with_generated_number(image_path):
   
    image = Image.open(image_path)

    
    current_time = int(time.time())

    
    generated_number = (current_time % 100) + 50

    if generated_number % 2 == 0:
        generated_number += 10

    
    rgb_with_generated_number = [
        (pixel[0] + generated_number, pixel[1] + generated_number, pixel[2] + generated_number)
        for pixel in image.getdata()
    ]

    return rgb_with_generated_number, image.width, image.height

def create_and_save_new_image(image_path, new_image_path):
    # Get the modified RGB values and image dimensions
    rgb_with_generated_number, width, height = read_rgb_values_with_generated_number(image_path)

    # Create a new image with the modified RGB values
    new_image = Image.new('RGB', (width, height))
    new_image.putdata(rgb_with_generated_number)

    
    new_image.save(new_image_path)

    return new_image

def sum_red_pixel_values(image):
    # Calculate the sum of red (R) pixel values
    red_sum = sum([pixel[0] for pixel in image.getdata()])
    return red_sum

def print_pixels(image):
    
    pixels = list(image.getdata())
    for i in range(min(5, len(pixels))):
        print(f"Pixel {i + 1}: {pixels[i]}")


input_image_path = r'C:\Users\USER\Desktop\Software Now_Assignment 2\chapter1.jpg'
output_image_path = r'C:\Users\USER\Desktop\Software Now_Assignment 2\Assignment_2\outputs\chapter1out.png'


new_image = create_and_save_new_image(input_image_path, output_image_path)


print("\nRGB values after generated number:")
print_pixels(new_image)


red_pixel_sum = sum_red_pixel_values(new_image)


print(f"\nSum of red pixel values: {red_pixel_sum}")
