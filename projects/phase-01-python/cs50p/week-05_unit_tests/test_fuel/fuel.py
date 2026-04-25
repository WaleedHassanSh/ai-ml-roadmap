# Prompt the user for a fraction, convert it to a percentage, and display the result. If the percentage is less than or equal to 1%, display "E". If the percentage is greater than or equal to 99%, display "F". Otherwise, display the percentage followed by a percent sign. The program should continue to prompt the user until a valid fraction is entered.


def main():

    fraction = input("Fraction: ")

    percentage = convert(fraction)

    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")

    x = int(x)
    y = int(y)

    if y == 0:
        raise ZeroDivisionError

    elif x < 0 or y < 1 or x > y:
        raise ValueError

    else:
        return round(x / y * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    else:
        return f"{str(percentage)}%"


if __name__ == "__main__":
    main()
