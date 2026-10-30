weekdays = ("Monday", "Tuesday", "Wednesday",
            "Thursday", "Friday", "Saturday", "Sunday")

print("Days of the Week")

for day in weekdays:
    print(day)

print("\nFirst Day:", weekdays[0])
print("Last Day:", weekdays[-1])

print("Number of Days:", len(weekdays))
print("Tuesday Count:", weekdays.count("Tuesday"))
print("Position of Friday:", weekdays.index("Friday"))
