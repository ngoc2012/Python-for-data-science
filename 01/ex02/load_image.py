from PIL import Image
import numpy as np

def ft_load(path: str) -> np.array:
    image = Image.open(image_path)
    print(f"Image format: {image.format}")
    if image.mode != 'RGB':
        image = image.convert('RGB')
    image_array = np.array(image)
    print("Pixel content in RGB format:")
    return image_array
