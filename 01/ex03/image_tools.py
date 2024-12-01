from PIL import Image
import numpy as np

def create_random_image(width, height, filename):
    # Generate random pixel data
    random_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

    # Create an image from the random data
    image = Image.fromarray(random_data)

    # Save the image to the specified filename
    image.save(filename)
