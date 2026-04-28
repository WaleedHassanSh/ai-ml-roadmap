# A program that extracts a YouTube embed URL from HTML and converts it to a shareable short URL.

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'<iframe.+"(?:https?://)?(?:www\.)?youtube\.com/embed/([^"]+)'
    match = re.search(pattern, s)

    if match:
        return f"https://youtu.be/{match.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()
