from PIL import Image
import numpy as np

def ft_load(path: str) -> np.array:
    image = Image.open(image_path)

    # Print the image format
    print(f"Image format: {image.format}")

    # Convert the image to RGB format if it's not already
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Convert the image to a NumPy array
    image_array = np.array(image)
    
    # Print the pixel content in RGB format
    print("Pixel content in RGB format:")
    print(image_array)
