import os
import imghdr
from PIL import Image, ImageDraw, ImageFont
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Load an image from a file and convert it to a numpy array."""
    if not isinstance(path, str):
        raise TypeError("Path must be a string.")
    if not os.path.exists(path):
        raise FileNotFoundError("File " + path + " not found.")
    try:
        output = imghdr.what(path)
    except PermissionError:
        raise PermissionError("Can not open file " + path + ".")
    if output is None:
        raise TypeError("Invalid image format.")
    file_size = os.path.getsize(path)
    max_size = 100 * 1024 * 1024
    if file_size > max_size:
        raise TypeError("File is too large.")
    image = Image.open(path)
    if image.mode != 'RGB':
        try:
            image = image.convert('RGB')
        except ValueError:
            raise ValueError("Unsupported image format.")
    image_array = np.array(image)
    return image_array
