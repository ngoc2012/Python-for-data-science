import os
import imghdr
from PIL import Image, ImageDraw
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Load an image from a file and convert it to a numpy array."""
    if not isinstance(path, str):
        raise TypeError("Path must be a string.")
    if not os.path.exists(path):
        raise FileNotFoundError("File not found.")
    if imghdr.what(path) is None:
        raise TypeError("Invalid image format.")
    image = Image.open(path)
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image_array = np.array(image)
    print(f"The shape of image is: {image_array.shape}")
    return image_array


def slice_me(f: np.ndarray, start: int, end: int) -> np.ndarray:
    """Slice a 2D numpy array."""
    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("Start and end must be integers.")
    if not isinstance(f, np.ndarray):
        raise TypeError("Family must be a numpy array.")
    shape = f.shape
    if len(shape) != 2:
        raise ValueError("Family must be a 2D array.")
    rows = shape[0]
    if start < 0:
        start = rows + start
    if end < 0:
        end = rows + end
    if start < 0 or start >= end or end > rows:
        raise IndexError("Index out of range.")
    new_shape = (end - start, shape[1])
    print(f"My shape is : {shape}")
    print(f"My new shape is : {new_shape}")
    return f[start:end]


def dislay_img(image_array: np.ndarray) -> None:
    """Display an image from a numpy array."""
    image_path = "/tmp/00.png"
    image = Image.fromarray(image_array, 'RGB')
    margin_left = 50
    margin_bottom = 20
    width, height = image.size
    new_width = width + margin_left
    new_height = height + margin_bottom
    enlarged_image = Image.new("RGB", (new_width, new_height), color=(255, 255, 255))
    enlarged_image.paste(image, (margin_left, 0))
    enlarged_image.save(image_path)
    enlarged_image.show()
    #print(f"The shape of image is: {image_array.shape}")

