from PIL import Image
import numpy as np


def create_random_image(width, height, filename):
    random_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
    image = Image.fromarray(random_data)
    image.save(filename)
