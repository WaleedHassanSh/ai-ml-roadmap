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
