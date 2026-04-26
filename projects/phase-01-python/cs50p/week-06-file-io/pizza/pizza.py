# A program that reads a CSV file containing pizza menu items and their prices, and displays the menu in a formatted table.

import csv
import sys

from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as file:
        menu = []

        reader = csv.reader(file)

        for row in reader:
            menu.append(row)

        header = menu[0]

        print(f"{tabulate(menu[1:], headers=header, tablefmt='grid')}")

except FileNotFoundError:
    sys.exit("File does not exist")
