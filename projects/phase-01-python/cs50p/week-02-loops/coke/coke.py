# A program that simulates a vending machine that accepts coins and dispenses a product once enough money has been inserted.

amount_due = 50

while amount_due > 0:
    print(f"Amount Due: {amount_due}")

    coin = int(input("Insert Coin: "))

    if coin in [5, 10, 25]:
        amount_due -= coin

print(f"Change Owed: {abs(amount_due)}")
