# A program that determines whether a provided credit card number is valid according to Luhn's algorithm and identifies the card type (AMEX, MASTERCARD, VISA) if valid.

while True:
    card_number = input("Number: ")
    if card_number.isdigit():
        break

checksum = 0

for digit in card_number[-2::-2]:
    product = int(digit) * 2
    checksum += (product % 10) + (product // 10)

for digit in card_number[-1::-2]:
    checksum += int(digit)

if checksum % 10 != 0:
    print("INVALID")

elif len(card_number) == 15 and card_number.startswith(("34", "37")):
    print("AMEX")

elif len(card_number) == 16 and card_number.startswith(("51", "52", "53", "54", "55")):
    print("MASTERCARD")

elif len(card_number) in [13, 16] and card_number.startswith(("4")):
    print("VISA")

else:
    print("INVALID")
