import numpy as np
from PIL import Image


def ft_invert(array) -> np.ndarray:
    '''Inverts the color of the image received.'''
    inverted_array = 255 - array
    image = Image.fromarray(inverted_array)
    image.show()
    return inverted_array

def ft_red(array) -> np.ndarray:
    '''Keep only the red channel, set green and blue channels to 0'''
    red_array = array.copy()
    red_array[:, :, 1] = 0  # Set green channel to 0
    red_array[:, :, 2] = 0  # Set blue channel to 0
    image = Image.fromarray(red_array)
    image.show()
    return red_array

def ft_green(array) -> np.ndarray:
    '''Keep only the green channel, set red and blue channels to 0'''
    green_array = array.copy()
    green_array[:, :, 0] = 0  # Set red channel to 0
    green_array[:, :, 2] = 0  # Set blue channel to 0
    image = Image.fromarray(green_array)
    image.show()
    return green_array

def ft_blue(array) -> np.ndarray:
    '''Keep only the blue channel, set red and green channels to 0'''
    blue_array = array.copy()
    blue_array[:, :, 0] = 0  # Set red channel to 0
    blue_array[:, :, 1] = 0  # Set green channel to 0
    image = Image.fromarray(blue_array)
    image.show()
    return blue_array

def ft_grey(array) -> np.ndarray:
    '''Convert the image to grayscale'''
    grey_array = array.copy()
    grey_array = np.dot(grey_array[..., :3], [0.2989, 0.5870, 0.1140])
    grey_array = grayscale_array.astype(np.uint8)
    grey_array = np.stack((grey_array,) * 3, axis=-1)
    image = Image.fromarray(grey_array, mode='L')
    image.show()
    return grey_array
