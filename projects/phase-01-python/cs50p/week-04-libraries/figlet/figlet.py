# A simple program that converts text into ASCII art using the `pyfiglet` library. It can either use a random font or a specified font from the command line arguments.

import random
import sys

from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    s = input("Input: ")

    font = random.choice(figlet.getFonts())
    font = figlet.setFont(font=font)

    print(f"Output: {figlet.renderText(s)}")

elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Inavalid usage")

    if sys.argv[2] not in figlet.getFonts():
        sys.exit("Invalid font")

    s = input("Input: ")

    font = sys.argv[2]
    font = figlet.setFont(font=font)

    print(f"Output: {figlet.renderText(s)}")

else:
    sys.exit("Invalid usage")
