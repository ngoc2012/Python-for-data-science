from load_image import ft_load, slice_me, dislay_img


img = dislay_img(ft_load("/home/ngoc/Downloads/eyes-sparkled-with-vibrant-colors-autumn-leaves-generative-ai.jpg"))
#img = dislay_img(ft_load("/home/ngoc/Downloads/Nature-Wallpaper-with-Trees-and-Lake.jpg"))

from PIL import Image
import numpy as np

# Generate random pixel data
random_data = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

# Create an image from the random data
image = Image.fromarray(random_data)

# Save the image to the specified filename
image.save("/home/ngoc/Downloads/00.png")

