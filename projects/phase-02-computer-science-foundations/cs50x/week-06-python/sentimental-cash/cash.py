# A program that calculates the minimum number of coins required to give a user change.

while True:
    try:
        change = round(float(input("Change: "))) * 100
        if change >= 0:
            break

    except ValueError:
        continue

coins = 0

while True:
    if change >= 25:
        change -= 25
        coins += 1
        continue

    elif change >= 10:
        change -= 10
        coins += 1
        continue

    elif change >= 5:
        change -= 5
        coins += 1
        continue

    elif change >= 1:
        change -= 1
        coins += 1
        continue

    else:
        break

print(coins)
