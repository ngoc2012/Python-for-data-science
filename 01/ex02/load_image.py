from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """Load an image from a file and convert it to a numpy array."""
    image = Image.open(path)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image_array = np.array(image)
    print(f"The shape of image is: {image_array.shape}")
    return image_array
