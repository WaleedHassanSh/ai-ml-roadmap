# A program that takes an image as input and outputs a new image with a shirt overlaid on top of it.

import os
import sys

from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].lower().endswith((".jpg", ".png", ".jpeg")) or not sys.argv[
    2
].lower().endswith((".jpg", ".png", ".jpeg")):
    sys.exit("Invalid output")

else:
    input_name, input_extension = os.path.splitext(sys.argv[1])
    output_name, output_extension = os.path.splitext(sys.argv[2])

    if input_extension.lower() != output_extension.lower():
        sys.exit("Input and output have different extensions")

try:
    image = Image.open(sys.argv[1])

    shirt = Image.open("shirt.png")
    size = shirt.size
    image = ImageOps.fit(image, size)
    image.paste(shirt, shirt)
    image.save(sys.argv[2])


except FileNotFoundError:
    sys.exit("Input does not exist")
