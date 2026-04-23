months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


while True:
    try:
        date = input("Date: ").strip()

        if "/" in date:
            m, d, y = date.split("/")

        elif "," in date:
            m, d, y = date.replace(",", "").split()

            if m in months:
                m = months.index(m) + 1

            else:
                continue

        else:
            continue

        d = int(d)
        m = int(m)
        y = int(y)

        if m < 1 or m > 12 or d < 1 or d > 31:
            continue

        print(f"{y}-{m:02}-{d:02}")

        break

    except ValueError:
        continue
