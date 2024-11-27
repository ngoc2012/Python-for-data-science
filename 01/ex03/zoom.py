from load_image import ft_load, slice_me, dislay_img


img = dislay_img(ft_load("/home/ngoc/Downloads/eyes-sparkled-with-vibrant-colors-autumn-leaves-generative-ai.jpg"))
#img = dislay_img(ft_load("/home/ngoc/Downloads/Nature-Wallpaper-with-Trees-and-Lake.jpg"))

from PIL import Image
import numpy as np

def create_random_image(width, height, filename):
    """
    Create a random image with fixed dimensions and save it to a file.

    Args:
        width (int): Width of the image.
        height (int): Height of the image.
        filename (str): Name of the output image file.
    """
    # Generate random pixel data
    random_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

    # Create an image from the random data
    image = Image.fromarray(random_data)

    # Save the image to the specified filename
    image.save(filename)

# Example usage:
create_random_image(5, 5, "/home/ngoc/Downloads/5x5.png")
