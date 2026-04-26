# A grocery store has a single checkout line, and they have asked you to write a program to tally the items that customers are purchasing. Your program should accept input until the user signals that there are no more items by hitting Control-D (which raises an EOFError). Then, your program should output a sorted list of all of the items that were purchased, along with a tally of how many times each item was purchased.

grocery = {}

while True:
    try:
        items = input().strip().upper()
        if items in grocery:
            grocery[items] += 1
        else:
            grocery[items] = 1
    except EOFError:
        break

for item in sorted(grocery):
    print(grocery[item], item)
