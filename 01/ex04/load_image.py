import os
import imghdr
from PIL import Image, ImageDraw, ImageFont
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Load an image from a file and convert it to a numpy array."""
    if not isinstance(path, str):
        raise TypeError("Path must be a string.")
    if not os.path.exists(path):
        raise FileNotFoundError("File " + path + " not found.")
    try:
        output = imghdr.what(path)
    except PermissionError:
        raise PermissionError("Can not open file " + path + ".")
    if output is None:
        raise TypeError("Invalid image format.")
    file_size = os.path.getsize(path)
    max_size = 100 * 1024 * 1024
    if file_size > max_size:
        raise TypeError("File is too large.")
    image = Image.open(path)
    if image.mode != "RGB":
        try:
            image = image.convert("RGB")
        except ValueError:
            raise ValueError("Unsupported image format.")
    image_array = np.array(image)
    print(f"The shape of image is: {image_array.shape}")
    print(image_array)
    return image_array


def slide_2D(
        f: np.ndarray,
        left: int,
        right: int,
        top: int,
        bottom: int
        ) -> np.ndarray:
    """Slice a 2D numpy array."""
    if (
        not isinstance(left, int)
        or not isinstance(right, int)
        or not isinstance(top, int)
        or not isinstance(bottom, int)
    ):
        raise TypeError("Positions must be integers.")
    if not isinstance(f, np.ndarray):
        raise TypeError("First argument must be a numpy array.")
    shape = f.shape
    if len(shape) < 2:
        raise ValueError("Family must be at least a 2D array.")
    height = shape[0]
    width = shape[1]
    if left < -width or right < -width:
        raise IndexError("Index of left or right out of range.")
    if top < -height or bottom < -height:
        raise IndexError("Index of top or bottom out of range.")
    if left < 0:
        left = width + left
    if right < 0:
        right = width + right
    right = min(right, width)
    if left >= right:
        raise IndexError(f"Right {right} must be bigger than left {left}.")
    if top < 0:
        top = height + top
    if bottom < 0:
        bottom = height + bottom
    bottom = min(bottom, height)
    if top >= bottom:
        raise IndexError(f"Bottom {bottom} must be bigger than top {top}.")
    if top < 0 or top >= bottom or bottom > height:
        raise IndexError("Index out of range.")
    return f[top:bottom, left:right]


def get_text_ratio(n: int) -> float:
    default_font = ImageFont.load_default()
    text_bbox = default_font.getbbox(n * "0")
    text_width = text_bbox[2]
    text_height = text_bbox[3]
    return text_width / n / text_height


def draw_text(
        draw: ImageDraw, text: str,
        x: int, y: int, desired_height: int,
        h_align="left", v_align="top"):
    """ Draw text at a specified height.  """
    default_font = ImageFont.load_default()
    text_bbox = default_font.getbbox(text)
    text_width = text_bbox[2]
    text_height = text_bbox[3]

    scale_factor = desired_height / text_height
    scaled_width = int(text_width * scale_factor)
    scaled_height = int(text_height * scale_factor)

    text_image = Image.new("RGBA",
                           (text_width, text_height), (255, 255, 255, 0))
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


def get_interval(L: int) -> int:
    d = pow(10, max(len(str(L)) - 2, 1)) * 5
    if int(L / d) < 5 and d > 50:
        d = int(d / 10)
    return d


def display_img(image_array: np.ndarray, mode="RGB") -> None:
    """Display an image from a numpy array."""
    default_colors = {
        "RGB": (255, 255, 255),
        "L": 255,
        "RGBA": (255, 255, 255, 255),
        "CMYK": (0, 0, 0, 0),
        "1": 1,
        "P": 0,
        "I": 0,
        "F": 0.0
    }
    if mode not in default_colors:
        raise ValueError("Unsupported image mode.")
    image_path = "/tmp/00.png"
    image = Image.fromarray(image_array, mode=mode)
    width, height = image.size
    width = int(width)
    height = int(height)

    n_digits = len(str(height))
    text_ratio = get_text_ratio(n_digits)

    margin = max(40, int(min(width, height) / 10))
    text_height = int(margin / 3)
    text_width = int(n_digits * text_ratio * text_height)
    line_width = max(1, int(margin / 40))
    line_height = int(margin / 10)

    margin_top = int(text_height / 2) + 1
    margin_left = line_height + text_width + line_width
    margin_bottom = line_height + text_height

    new_width = width + margin_left + line_width
    new_height = height + margin_bottom + margin_top
    enlarged_image = Image.new(
                        mode,
                        (new_width, new_height),
                        color=default_colors[mode])
    enlarged_image.paste(image, (margin_left, margin_top))
    draw = ImageDraw.Draw(enlarged_image)

    min_to_draw_border = 0
    if width > min_to_draw_border and height > min_to_draw_border:
        draw.rectangle([(
            margin_left - line_width,
            margin_top - line_width
            ), (
            margin_left + width + line_width / 2,
            height + margin_top + line_width / 2
            )], outline="black", width=line_width)
    # Draw X-axis scale (along the bottom margin)
    x_interval = get_interval(width)
    for x in range(0, width, x_interval):
        pos_x = margin_left + x
        draw.line([
            (pos_x, height + margin_top),
            (pos_x, height + margin_top + line_height)
            ], fill="black", width=line_width)
        draw_text(
                draw,
                str(x),
                x=pos_x,
                y=height + margin_top + line_height,
                desired_height=text_height,
                h_align="center",
                v_align="top")
    # Draw Y-axis scale (along the left margin)
    y_interval = get_interval(height)
    for y in range(0, height, y_interval):
        draw.line([
            (margin_left - line_height - line_width / 2,
             y + margin_top + line_width / 2),
            (margin_left - line_width / 2,
             y + margin_top + line_width / 2)
            ], fill="black", width=line_width)
        draw_text(
            draw,
            str(y),
            x=margin_left - line_height - line_width,
            y=y + margin_top,
            desired_height=text_height,
            h_align="right",
            v_align="center")

    enlarged_image.save(image_path)
    enlarged_image.show()


def rotate_image(path: str, left: int, right: int, top: int, bottom: int)\
        -> None:
    """Slice a 2D numpy array."""
    f = ft_load(path)
    new_shape = slide_2D(f, left, right, top, bottom)
    if new_shape.ndim != 3 and new_shape.shape[2] != 3:
        raise ValueError("Unsupported image formar")
    if new_shape.ndim == 2:
        display_img(new_shape)
    grayscale_array = np.dot(new_shape[..., :3], [0.2989, 0.5870, 0.1140])
    grayscale_array = grayscale_array.astype(np.uint8)
    rows, cols = grayscale_array.shape
    transposed_array = np.empty((cols, rows), dtype=grayscale_array.dtype)
    for i in range(rows):
        for j in range(cols):
            transposed_array[j, i] = grayscale_array[i, j]

    print(f"New shape after slicing: {transposed_array.shape}")
    print(transposed_array)
    display_img(transposed_array, mode="L")
