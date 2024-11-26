from load_image import ft_load


print(ft_load("/home/ngoc/Downloads/eyes-sparkled-with-vibrant-colors-autumn-leaves-generative-ai.jpg"))
try:
    print(ft_load("iuihi"))
except Exception as e:
    print(e)
try:
    print(ft_load("/home/ngoc/Downloads/meotravaux.mp4"))
except Exception as e:
    print(e)
try:
    print(ft_load(None))
except Exception as e:
    print(e)
