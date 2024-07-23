import cv2
import numpy as np
from PIL import Image
from rembg import remove

def remove_background(input_path, output_path):
    # Read the image
    img = Image.open(input_path)
    
    # Remove the background
    img_no_bg = remove(img)
    
    # Save the result
    img_no_bg.save(output_path)

input_image_path = 'C:/Users/ADMIN/Documents/10.jpg'
output_image_path = 'C:/Users/ADMIN/Documents/10bg.jpg'

remove_background(input_image_path, output_image_path)
