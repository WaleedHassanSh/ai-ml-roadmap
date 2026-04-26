# A program that reads a CSV file, transforms the data, and writes it to a new CSV file.

import csv
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as input_file:
        reader = csv.DictReader(input_file)

        with open(sys.argv[2], "w") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])

            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(",")

                first = first.strip()
                last = last.strip()

                writer.writerow({"first": first, "last": last, "house": row["house"]})


except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")
