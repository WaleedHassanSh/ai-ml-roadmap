# Asks the user for a greeting. If the greeting starts with "hello" (in any case), then output $0. If the greeting starts with an "h" (in any case), then output $20. Otherwise, output $100.

greeting = input("Enter your greeting: ")

greeting = greeting.lower().strip()

if greeting.startswith("hello"):
    print("$0")
elif greeting.startswith("h"):
    print("$20")
else:
    print("$100")
