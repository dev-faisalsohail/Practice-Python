from PIL import Image

img = Image.open(r"f1.png")
print(img.format)

img.show()
