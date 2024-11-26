from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """Load an image from a file and convert it to a numpy array."""
    if not isinstance(path, str):
        raise TypeError("path must be a string")
    try:
        image = Image.open(path)
    except FileNotFoundError:
        raise FileNotFoundError("File not found")
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image_array = np.array(image)
    print(f"The shape of image is: {image_array.shape}")
    return image_array
