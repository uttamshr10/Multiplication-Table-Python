print("Welcome to the Multiplication/Exponential Table App")
name = input("\nHello, what is your name: ").title().strip()
number = float(input("What number would you like to work with: "))

# Rounding the number
number_round = round(number, 2)
# For multiplication
print("\nMultiplication Table for " + str(number_round))
print("\n\t 1 * " + str(number_round) +
      " = " + str(round(1*number_round, 2)))
print("\t 2 * " + str(number_round) +
      " = " + str(round(2*number_round, 2)))
print("\t 3 * " + str(number_round) +
      " = " + str(round(3*number_round, 2)))
print("\t 4 * " + str(number_round) +
      " = " + str(round(4*number_round, 2)))
print("\t 5 * " + str(number_round) +
      " = " + str(round(5*number_round, 2)))
print("\t 6 * " + str(number_round) +
      " = " + str(round(6*number_round, 2)))
print("\t 7 * " + str(number_round) +
      " = " + str(round(7*number_round, 2)))
print("\t 8 * " + str(number_round) +
      " = " + str(round(8*number_round, 2)))
print("\t 9 * " + str(number_round) +
      " = " + str(round(9*number_round, 2)))
print("\t 10 * " + str(number_round) +
      " = " + str(round(10*number_round, 2)))

# For Exponent
print("\nExponent Table for " + str(number_round))
print("\n\t" + str(number_round) + " ** 1 = " + str(round(number_round**1, 2)))
print("\t" + str(number_round) + " ** 2 = " + str(round(number_round**2, 2)))
print("\t" + str(number_round) + " ** 3 = " + str(round(number_round**3, 2)))
print("\t" + str(number_round) + " ** 4 = " + str(round(number_round**4, 2)))
print("\t" + str(number_round) + " ** 5 = " + str(round(number_round**5, 2)))
print("\t" + str(number_round) + " ** 6 = " + str(round(number_round**6, 2)))
print("\t" + str(number_round) + " ** 7 = " + str(round(number_round**7, 2)))
print("\t" + str(number_round) + " ** 8 = " + str(round(number_round**8, 2)))
print("\t" + str(number_round) + " ** 9 = " + str(round(number_round**9, 2)))
print("\t" + str(number_round) + " ** 10 = " + str(round(number_round**10, 2)))

cool = "Math is cool!"

print("\n" + name + ", " + cool)
print("\t" + name + ", " + cool.lower())
print("\t\t" + name + ", " + cool.title())
print("\t\t\t" + name + ", " + cool.upper())
