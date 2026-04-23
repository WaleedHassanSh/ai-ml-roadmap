# Prompt the user for an item, and display the total price of all items that the user has input so far. The user might input items that are not on the menu, and should be ignored. The program should continue to prompt the user for more items until the user inputs control-d (which is how to indicate end-of-file on most operating systems).

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

total = 0

while True:
    try:
        item = input("Item: ").title().strip()
        if item in menu:
            total += menu[item]
            print(f"Total: ${total:.2f}")
    except EOFError:
        print()
        break
