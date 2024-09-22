import time
from PIL import Image

# Get the current Unix timestamp (seconds since epoch) and store it as an integer
current_time = int(time.time())

# Generate a number based on the current time (last two digits + 50)
generated_number = (current_time % 100) + 50

# If the generated number is even, add 10 to make it odd
if generated_number % 2 == 0:
    generated_number += 10

# Print the generated number
print(generated_number)

# Function to read the RGB values from an image
def read_rgb_values(image_path):
    # Open the image at the provided path
    image = Image.open(image_path)
    
    # Get the pixel data (RGB values) and convert it into a list
    rgb_values = list(image.getdata())

    return rgb_values

# Path to the image
image_path = r''

# Read the RGB values of the image
rgb_values = read_rgb_values(image_path)

# Display the RGB values of the first few pixels
for i in range(min(5, len(rgb_values))):
    print(f"Pixel {i + 1}: {rgb_values[i]}")

# Function to read and modify the RGB values using the generated number
def read_rgb_values_with_generated_number(image_path):
    # Open the image
    image = Image.open(image_path)

    # Get the current time and generate a number (as before)
    current_time = int(time.time())
    generated_number = (current_time % 100) + 50

    # If the generated number is even, add 10
    if generated_number % 2 == 0:
        generated_number += 10
    
    # Print the generated number
    print(generated_number)
    
    # Modify each pixel's RGB values by adding the generated number to each color channel
    rgb_with_generated_number = [
        (pixel[0] + generated_number, pixel[1] + generated_number, pixel[2] + generated_number)
        for pixel in image.getdata()
    ]
    
    return rgb_with_generated_number

# Path to the input image
image_path = r'F:\CDU\HIT137 SOFTWARE NOW\HIT137_Software Now_Assignment 2\chapter1.jpg'

# Get the modified RGB values
rgb_with_generated_number = read_rgb_values_with_generated_number(image_path)

# Display the modified RGB values of the first few pixels
for i in range(min(5, len(rgb_with_generated_number))):
    print(f"Pixel {i + 1}: {rgb_with_generated_number[i]}")

# Path to save the output image
output_image_path = r'F:\CDU\HIT137 SOFTWARE NOW\HIT137_Software Now_Assignment 2\outputs\chapter1output.png'

# Function to read and modify RGB values, then save the new image
def read_rgb_values_with_generated_number(image_path):
    # Open the image
    image = Image.open(image_path)

    # Generate the number based on the current time
    current_time = int(time.time())
    generated_number = (current_time % 100) + 50

    # If the generated number is even, add 10
    if generated_number % 2 == 0:
        generated_number += 10

    # Modify each pixel's RGB values by adding the generated number to each channel
    rgb_with_generated_number = [
        (pixel[0] + generated_number, pixel[1] + generated_number, pixel[2] + generated_number)
        for pixel in image.getdata()
    ]

    # Return the modified RGB values and the dimensions of the image
    return rgb_with_generated_number, image.width, image.height

# Function to create and save a new image with modified RGB values
def create_and_save_new_image(image_path, new_image_path):
    # Get the modified RGB values and image dimensions
    rgb_with_generated_number, width, height = read_rgb_values_with_generated_number(image_path)

    # Create a new image with the same dimensions
    new_image = Image.new('RGB', (width, height))
    
    # Add the modified RGB values to the new image
    new_image.putdata(rgb_with_generated_number)
    
    # Save the new image at the specified path
    new_image.save(new_image_path)

    return new_image

# Function to sum up the red (R) values of all pixels in the image
def sum_red_pixel_values(image):
    # Extract and sum all red values (R channel)
    red_sum = sum([pixel[0] for pixel in image.getdata()])
    return red_sum

# Function to print the RGB values of the first few pixels
def print_pixels(image):
    # Get the pixel data from the image
    pixels = list(image.getdata())
    
    # Print RGB values of the first 5 pixels
    for i in range(min(5, len(pixels))):
        print(f"Pixel {i + 1}: {pixels[i]}")

# Input and output image paths
input_image_path = r'F:\CDU\HIT137 SOFTWARE NOW\HIT137_Software Now_Assignment 2\chapter1.jpg'
output_image_path = r'F:\CDU\HIT137 SOFTWARE NOW\HIT137_Software Now_Assignment 2\outputs\chapter1output.png'

# Create the new image with modified RGB values and save it
new_image = create_and_save_new_image(input_image_path, output_image_path)

# Print the RGB values of the new image
print("\nRGB values after generated number:")
print_pixels(new_image)

# Calculate and print the sum of red pixel values in the new image
red_pixel_sum = sum_red_pixel_values(new_image)
print(f"\nSum of red pixel values: {red_pixel_sum}")
