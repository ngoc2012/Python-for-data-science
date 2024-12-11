from load_image import rotate_image


def main():
    try:
        # Size (768, 1024, 3)
        #rotate_image("animal.jpeg", 450, 850, 100, 500)
        # rotate_image("animal_empty.jpeg", 450, 850, 100, 500)
        # rotate_image(None, 450, 850, 100, 500)
        # rotate_image("animal.jpeg", 0, 0, 100, 500)
        # rotate_image("animal.jpeg", 0, 1, 100, 500)
        # rotate_image("animal.jpeg", 0, 10, 100, 500)
        # rotate_image("animal.jpeg", 0, 10, 0, 10)
        # rotate_image("animal.jpeg", 0, 100, 0, 100)
        # rotate_image("bigfile", 0, 100, 0, 100)
        # rotate_image("animal.jpeg", -999999990, 10, 0, 10)
        rotate_image("animal.jpeg", 0, 9999999, 0, 100)
        # rotate_image("animal.jpeg", 0, 6, 0, 6)
        # rotate_image("animal.jpeg", 0, 1, 0, 1)
        # rotate_image("eye.jpg", -500, -1, 0, 500)
        # rotate_image("eye.jpg", 0, -1, 0, -1)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
