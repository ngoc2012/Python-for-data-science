from load_image import zoom_image

def main():
    try:
        zoom_image("animal.jpeg", 0, 500, 0, 500)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
