# Asks for the mass of an object and calculates its energy using the formula E=mc^2.

m = input("Enter the mass of the objects in kg: ")
c = 300000000
m = int(m)

e = m * c**2

print(f"The energy of the objects is {e} joules.")
