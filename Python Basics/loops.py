total = 0

print("Enter 5 numbers")

for i in range(5):
    value = int(input("Enter number: "))
    total += value

print("\nTotal:", total)
print("Average:", total / 5)

print("\nEven Numbers from 1 to 20")

number = 2

while number <= 20:
    print(number, end=" ")
    number += 2

print()
