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


def calculate_interval(size, target_intervals=10):
    raw_interval = size / target_intervals
    # Round to a "nice" number
    if raw_interval <= 10:
        return max(1, int(raw_interval))  # Round down for smaller sizes
    elif raw_interval <= 50:
        return int(raw_interval // 5) * 5  # Nearest multiple of 5
    else:
        return int(raw_interval // 10) * 10  # Nearest multiple of 10


def dislay_img(image_array: np.ndarray) -> None:
    """Display an image from a numpy array."""
    image_path = "/tmp/00.png"
    image = Image.fromarray(image_array, 'RGB')
    width, height = image.size
    margin = int(min(width, height) / 10)
    margin_left = int(width / 10)
    margin_bottom = int(height / 10)
    new_width = width + margin_left
    new_height = height + margin_bottom
    enlarged_image = Image.new("RGB", (new_width, new_height), color=(255, 255, 255))
    enlarged_image.paste(image, (margin_left, 0))

    x_interval = calculate_interval(width)
    y_interval = calculate_interval(height)
    
    # Draw scales on the axes
    draw = ImageDraw.Draw(enlarged_image)

    #text = "0000"
    #default_font = ImageFont.load_default()

    ## Create a separate image for the text
    #text_width, text_height = draw_main.textsize(text, font=default_font)
    #text_image = Image.new("RGB", (text_width, text_height), color="white")
    #draw_text = ImageDraw.Draw(text_image)
    #draw_text.text((0, 0), text, fill="black", font=default_font)
    #
    ## Scale the text image to simulate font size
    #scale_factor = 3  # Adjust this to change the font size
    #scaled_width = int(text_width * scale_factor)
    #scaled_height = int(text_height * scale_factor)
    #scaled_text_image = text_image.resize((scaled_width, scaled_height), resample=Image.Resampling.NEAREST)
    #
    ## Paste the scaled text back onto the main image
    #main_image.paste(scaled_text_image, (50, 20))


    # Draw X-axis scale (along the bottom margin)
    for x in range(0, width + 1, x_interval):  # Use calculated interval
        pos_x = margin_left + x
        draw.line([(pos_x, height), (pos_x, height + 5)], fill="black", width=1)
        draw.text((pos_x - 10, height + 10), str(x), fill="black")
    
    for y in range(0, height + 1, y_interval):
        pos_y = height - y
        draw.line([(margin_left - 5, pos_y), (margin_left, pos_y)], fill="black", width=1)
        draw.text((margin_left - 40, pos_y - 5), str(y), fill="black")


    enlarged_image.save(image_path)
    enlarged_image.show()
    #print(f"The shape of image is: {image_array.shape}")

