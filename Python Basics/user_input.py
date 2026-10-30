number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

total = number1 + number2
difference = number1 - number2
product = number1 * number2

print("\nCalculation Results")
print(f"Sum: {total}")
print(f"Difference: {difference}")
print(f"Product: {product}")

if number2 != 0:
    print(f"Division: {number1 / number2}")
else:
    print("Division: Cannot divide by zero")
