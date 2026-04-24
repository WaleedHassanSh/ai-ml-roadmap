# A simple program that converts text with emoji aliases into actual emojis using the `emoji` library.

import emoji

text = input("Input: ")

print(f"Output: {emoji.emojize(text, language='alias')}")
