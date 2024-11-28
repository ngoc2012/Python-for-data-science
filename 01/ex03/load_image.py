import os
import imghdr
from PIL import Image, ImageDraw, ImageFont
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

def get_text_ratio(n: int) -> float:
    default_font = ImageFont.load_default()
    text_bbox = default_font.getbbox(n * "0")
    text_width = text_bbox[2]
    text_height = text_bbox[3]
    return text_width / n / text_height


def draw_text_with_height(draw: ImageDraw, text: str, x: int, y: int, desired_height: int, h_align="left", v_align="top"):
    """
    Draw text at a specified height using the default font with justification.
    """
    default_font = ImageFont.load_default()
    text_bbox = default_font.getbbox(text)
    text_width = text_bbox[2]
    text_height = text_bbox[3]
    print(f"Text width: {text_width}, Text height: {text_height}, {text_height / text_width}")
    scale_factor = desired_height / text_height
    scaled_width = int(text_width * scale_factor)
    scaled_height = int(text_height * scale_factor)

    text_image = Image.new("RGBA", (text_width, text_height), (255, 255, 255, 0))
    text_draw = ImageDraw.Draw(text_image)
    text_draw.text((0, 0), text, fill="black", font=default_font)

    scaled_text_image = text_image.resize((scaled_width, scaled_height), resample=Image.Resampling.NEAREST)
    scaled_text_image.save(f"/tmp/{text}.png")

    # Adjust position based on alignment
    if h_align == "center":
        x -= scaled_width // 2
    elif h_align == "right":
        x -= scaled_width

    if v_align == "center":
        y -= scaled_height // 2
    elif v_align == "bottom":
        y -= scaled_height

    # Paste the scaled text onto the main image
    draw.bitmap((x, y), scaled_text_image, fill="black")

def dislay_img(image_array: np.ndarray) -> None:
    """Display an image from a numpy array."""
    image_path = "/tmp/00.png"
    image = Image.fromarray(image_array, 'RGB')
    width, height = image.size

    margin = max(20, int(min(width, height) / 10))
    margin_left = margin
    text_height = int(margin / 3)
    margin_top = int(text_height / 2) + 1
    line_width = max(1, int(margin / 20))
    line_height = int(margin / 5)
    margin_bottom = line_height + text_height

    new_width = width + margin_left + line_width
    new_height = height + margin_bottom + margin_top
    enlarged_image = Image.new("RGB", (new_width, new_height), color=(255, 255, 255))
    enlarged_image.paste(image, (margin_left, margin_top))

    x_interval = calculate_interval(width)
    y_interval = calculate_interval(height)
    
    # Draw scales on the axes
    draw = ImageDraw.Draw(enlarged_image)

    draw.rectangle([(margin_left - line_width / 2 + 1, margin_top - line_width / 2 + 1), (margin_left + width + line_width / 2, height + margin_top + line_width / 2)], outline="black", width=line_width)
    # Draw X-axis scale (along the bottom margin)
    for x in range(0, width, x_interval):  # Use calculated interval
        pos_x = margin_left + x
        draw.line([(pos_x, height + margin_top), (pos_x, height + margin_top + line_height)], fill="black", width=line_width)
        draw_text_with_height(draw, str(x), x=pos_x, y=height + margin_top + line_height, desired_height=text_height, h_align="center", v_align="top")
    # Draw Y-axis scale (along the left margin)
    for y in range(0, height, y_interval):
        pos_y = height - y
        draw.line([(margin_left - line_height, pos_y + margin_top - y_interval), (margin_left, pos_y + margin_top - y_interval)], fill="black", width=line_width)
        draw_text_with_height(draw, str(y), x=margin_left - line_height, y=y + margin_top, desired_height=text_height, h_align="right", v_align="center")

    enlarged_image.save(image_path)
    enlarged_image.show()
    #print(f"The shape of image is: {image_array.shape}")

