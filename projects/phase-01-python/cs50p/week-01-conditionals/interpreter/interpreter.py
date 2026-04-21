# Asks the user for an expression. The expression will be in the form of x y z, where x and z are numbers, and y is an operator, either +, -, *, or /. Then output the result of the expression formatted to one decimal place.

expression = input("Enter an expression: ")

x, y, z = expression.split()

if y == "+":
    result = float(x) + float(z)
elif y == "-":
    result = float(x) - float(z)
elif y == "*":
    result = float(x) * float(z)
elif y == "/":
    result = float(x) / float(z)
else:
    raise ValueError("Invalid operator")

print(f"{result:.1f}")
