# Asks the user for a number. If the number is 42, or if the user inputs "forty two" (in any case), then output "Yes". Otherwise, output "No".

num = input("Enter a number: ").strip()

if num == "42" or num.title() == "Forty Two" or num.lower() == "forty-two":
    print("Yes")
else:
    print("No")
