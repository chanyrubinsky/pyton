
from PIL import Image
img = Image.open("image.jpg")
# img.show()
im = img.resize((688, 643))
# im.show()

# img.crop((10, 23, 34, 54)).show()
# img.rotate(90).show()

I1 = ImagceDraw.Draw(img)

# Add Text to an image
I1.text((28, 36), "nice Car", fill=(255, 0, 0))

# Display edited image
img.show()
