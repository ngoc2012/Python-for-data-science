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


def zoom(f: np.ndarray, left: int, right: int, top: int, bottom: int) -> np.ndarray:
    """Slice a 2D numpy array."""
    if not isinstance(left, int) or not isinstance(right, int) or not isinstance(top, int) or not isinstance(bottom, int):
        raise TypeError("Positions must be integers.")
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

    scale_factor = desired_height / text_height
    scaled_width = int(text_width * scale_factor)
    scaled_height = int(text_height * scale_factor)

    text_image = Image.new("RGBA", (text_width, text_height), (255, 255, 255, 0))
    text_draw = ImageDraw.Draw(text_image)
    text_draw.text((0, 0), text, fill="black", font=default_font)

    scaled_text_image = text_image.resize(
            (scaled_width, scaled_height),
            resample=Image.Resampling.NEAREST)

    if h_align == "center":
        x -= scaled_width // 2
    elif h_align == "right":
        x -= scaled_width

    if v_align == "center":
        y -= scaled_height // 2
    elif v_align == "bottom":
        y -= scaled_height
    draw.bitmap((x, y), scaled_text_image, fill="black")


def dislay_img(image_array: np.ndarray) -> None:
    """Display an image from a numpy array."""
    image_path = "/tmp/00.png"
    image = Image.fromarray(image_array, 'RGB')
    width, height = image.size

    n_digits = len(str(height))
    text_ratio = get_text_ratio(n_digits)

    margin = max(20, int(min(width, height) / 10))
    text_height = int(margin / 3)
    text_width = int(n_digits * text_ratio * text_height)
    line_width = max(1, int(margin / 40))
    line_height = int(margin / 10)

    margin_top = int(text_height / 2) + 1
    margin_left = line_height + text_width
    margin_bottom = line_height + text_height

    new_width = width + margin_left + line_width
    new_height = height + margin_bottom + margin_top
    enlarged_image = Image.new("RGB", (new_width, new_height), color=(255, 255, 255))
    enlarged_image.paste(image, (margin_left, margin_top))
    draw = ImageDraw.Draw(enlarged_image)

    draw.rectangle([(
        margin_left - line_width / 2 + 1,
        margin_top - line_width / 2 + 1
        ), (
        margin_left + width + line_width / 2,
        height + margin_top + line_width / 2
        )], outline="black", width=line_width)
    # Draw X-axis scale (along the bottom margin)
    x_interval = pow(10, max(len(str(width)) - 2, 0)) * 5
    for x in range(0, width, x_interval):
        pos_x = margin_left + x
        draw.line([
            (pos_x, height + margin_top),
            (pos_x, height + margin_top + line_height)
            ], fill="black", width=line_width)
        draw_text_with_height(draw, str(x),
            x=pos_x,
            y=height + margin_top + line_height,
            desired_height=text_height,
            h_align="center",
            v_align="top")
    # Draw Y-axis scale (along the left margin)
    y_interval = pow(10, max(n_digits - 2, 0)) * 5
    for y in range(0, height, y_interval):
        pos_y = height - y
        draw.line([
            (margin_left - line_height, pos_y + margin_top - y_interval),
            (margin_left, pos_y + margin_top - y_interval)
            ], fill="black", width=line_width)
        draw_text_with_height(draw, str(y),
            x=margin_left - line_height,
            y=y + margin_top,
            desired_height=text_height,
            h_align="right",
            v_align="center")

    enlarged_image.save(image_path)
    enlarged_image.show()
    #print(f"The shape of image is: {image_array.shape}")
