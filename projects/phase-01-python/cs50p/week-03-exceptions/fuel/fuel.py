# Prompt the user for a fraction, convert it to a percentage, and display the result. If the percentage is less than or equal to 1%, display "E". If the percentage is greater than or equal to 99%, display "F". Otherwise, display the percentage followed by a percent sign. The program should continue to prompt the user until a valid fraction is entered.

while True:
    try:
        fraction = input("Fraction: ")

        x, y = fraction.split("/")

        x = int(x)
        y = int(y)

        if x > y or y <= 0 or x < 0:
            continue

        percent = round((x / y) * 100)

        if percent <= 1:
            print("E")

        elif percent >= 99:
            print("F")

        else:
            print(f"{percent}%")

        break

    except (ValueError, ZeroDivisionError):
        continue
