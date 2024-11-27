from load_image import ft_load, slice_me, dislay_img


#img = dislay_img(ft_load("/home/ngoc/Downloads/eyes-sparkled-with-vibrant-colors-autumn-leaves-generative-ai.jpg"))
#img = dislay_img(ft_load("/home/ngoc/Downloads/Nature-Wallpaper-with-Trees-and-Lake.jpg"))
#img = dislay_img(ft_load("/home/ngoc/Downloads/1000x200.png"))
img = dislay_img(ft_load("/home/ngoc/Downloads/5x5.png"))

#from PIL import Image
#import numpy as np
#
#def create_random_image(width, height, filename):
#    """
#    Create a random image with fixed dimensions and save it to a file.
#
#    Args:
#        width (int): Width of the image.
#        height (int): Height of the image.
#        filename (str): Name of the output image file.
#    """
#    # Generate random pixel data
#    random_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)
#
#    # Create an image from the random data
#    image = Image.fromarray(random_data)
#
#    # Save the image to the specified filename
#    image.save(filename)
#
## Example usage:
#images = [
#        [5, 5],
#        [1000, 5],
#        [5, 1000],
#        [1000, 200],
#        [200, 1000],
#        [1000, 1000]]
#for i in images:
#    create_random_image(i[0], i[1], f"/home/ngoc/Downloads/{i[0]}x{i[1]}.png")
