from load_image import zoom_image

def main():
    try:
        zoom_image("animal.jpeg", 450, 850, 100, 500)
        #zoom_image("animal_empty.jpeg", 450, 850, 100, 500)
        #zoom_image(None, 450, 850, 100, 500)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
