from PIL import Image, ImageEnhance
import numpy as np
import time

IMG_DIR = "./images/chapter1.jpg"

# Calculate a number based on the current time
current_time = int(time.time())
generated_number = (current_time % 100) + 100

# Adjust the number if it's even
if generated_number % 2 == 0:
    generated_number += 10

print(f"Generated number: {generated_number}")

def add_value_to_all_channels(image, value):
    """
    Add a specified value to all three color channels (R, G, B)
    
    Args:
        image (PIL.Image.Image): Input image (in RGB format).
        value (int): Value to add to each channel.

    Returns:
        PIL.Image.Image: Image with the value added to each channel.
    """
    # Convert image to NumPy array
    img_array = np.array(image)
    # Ensure the value is within the valid range [0, 255]
    value = np.clip(value, 0, 255)
    # Create a NumPy array with the same shape as the image where each channel is the value to add
    add_array = np.full_like(img_array, value)
    result_array = np.clip(img_array + add_array, 0, 255)
    result_image = Image.fromarray(result_array.astype(np.uint8))
    return result_image

# Read the image
img = Image.open(IMG_DIR)

# Check if the image is in RGB mode, if not, convert it
if img.mode != 'RGB':
    img = img.convert('RGB')

print(f"Original image size: {img.size}")

# Add the generated number to all channels
modified_img = add_value_to_all_channels(img, generated_number)

# Display the original and modified images
img.show(title="Original Image")
modified_img.show(title="Modified Image")
red_channel = np.array(modified_img)[:, :, 0] # extract the red channel from the modified images 
red_sum = np.sum(red_channel)

# Optionally save the modified image
output_file = "./images/chapter1out.png"
modified_img.save(output_file)
print(f"Modified image saved to {output_file}")
print(red_sum)
