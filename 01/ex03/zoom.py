from load_image import zoom_image

def main():
    try:
        # Size (768, 1024, 3)
        #zoom_image("animal.jpeg", 450, 850, 100, 500)
        #zoom_image("animal_empty.jpeg", 450, 850, 100, 500)
        #zoom_image(None, 450, 850, 100, 500)
        #zoom_image("animal.jpeg", 0, 0, 100, 500)
        #zoom_image("animal.jpeg", 0, 1, 100, 500)
        #zoom_image("animal.jpeg", 0, 10, 100, 500)
        #zoom_image("animal.jpeg", 0, 10, 0, 10)
        #zoom_image("animal.jpeg", -999999990, 10, 0, 10)
        #zoom_image("animal.jpeg", 0, 9999999, 0, 100)
        zoom_image("animal.jpeg", 0, 9999999, 0, 1)
        #zoom_image("eye.jpg", -500, -1, 0, 500)
        #zoom_image("eye.jpg", 0, -1, 0, -1)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
