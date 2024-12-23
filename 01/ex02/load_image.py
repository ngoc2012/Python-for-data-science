import os
import imghdr
from PIL import Image
import numpy as np


def ft_load(path: str) -> np.array:
    """Load an image from a file and convert it to a numpy array."""
    if not isinstance(path, str):
        raise TypeError("Path must be a string.")
    if not os.path.exists(path):
        raise FileNotFoundError("File not found.")
    try:
        output = imghdr.what(path)
    except PermissionError:
        raise PermissionError(f"Can not open file {path}.")
    if output is None:
        raise TypeError("Invalid image format.")
    file_size = os.path.getsize(path)
    max_size = 100 * 1024 * 1024
    if file_size > max_size:
        raise TypeError("File is too large.")
    image = Image.open(path)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image_array = np.array(image)
    print(f"The shape of image is: {image_array.shape}")
    return image_array
