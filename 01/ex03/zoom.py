from load_image import zoom_image

def main():
    #zoom_image("/home/ngoc/Downloads/eye.jpg", 0, 500, 0, 500)
    try:
        zoom_image("/home/ngoc/Downloads/eye1.jpg", 0, 500, 0, 500)
    except Exception as e:
        print(e)

"""
from image_tools import create_random_image

# Example usage:
images = [
        [5, 5],
        [1000, 5],
        [5, 1000],
        [100, 100],
        [200, 200],
        [400, 400],
        [1000, 200],
        [200, 1000],
        [1000, 1000]]
for i in images:
    create_random_image(i[0], i[1], f"/home/ngoc/Downloads/{i[0]}x{i[1]}.png")
"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()
