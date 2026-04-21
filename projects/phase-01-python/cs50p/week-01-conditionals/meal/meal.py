# Asks the user for a time. If the time is between 7:00 and 8:00, then output "breakfast time". If the time is between 12:00 and 13:00, then output "lunch time". If the time is between 18:00 and 19:00, then output "dinner time". Otherwise, output nothing. Assume that the user will input the time in the format of hours:minutes, where hours will be between 0 and 23, and minutes will be between 0 and 59.


def main():
    time = input("What time is it? ")

    time = convert(time)

    if 7.0 <= time <= 8.0:
        print("breakfast time")
    elif 12.0 <= time <= 13.0:
        print("lunch time")
    elif 18.0 <= time <= 19.0:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")

    hours = float(hours)
    minutes = float(minutes)

    time = hours + minutes / 60

    return time


if __name__ == "__main__":
    main()
