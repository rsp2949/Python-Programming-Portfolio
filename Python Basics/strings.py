message = input("Enter a sentence: ")

print("\nString Operations")
print("Original:", message)
print("Number of Characters:", len(message))
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Title Case:", message.title())
print("Reversed:", message[::-1])

if "python" in message.lower():
    print("The sentence contains the word Python.")
else:
    print("The sentence does not contain the word Python.")
