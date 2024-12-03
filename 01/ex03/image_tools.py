from PIL import Image
import numpy as np


def create_random_image(width, height, filename):
    """
    from image_tools import create_random_image
    images = [
            [5, 5],
            [1000, 5],
            [5, 1000],
            [100, 100],
            [200, 200],
            [400, 400],
            [1000, 200],
            [200, 1000],
            [1000, 1000]]
    for i in images:
        create_random_image(i[0], i[1], f"/home/ngoc/Downloads/{i[0]}x{i[1]}.png")
    """
    random = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    image = Image.fromarray(random)
    image.save(filename)
