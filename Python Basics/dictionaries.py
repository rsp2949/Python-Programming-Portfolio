inventory = {
    "Pen": 20,
    "Notebook": 50,
    "Pencil": 15,
    "Eraser": 10
}

print("Store Inventory")

for item, quantity in inventory.items():
    print(item, ":", quantity)

inventory["Marker"] = 25
inventory["Pen"] += 10

print("\nUpdated Inventory:", inventory)

item_name = "Notebook"

if item_name in inventory:
    print(item_name, "is available.")
    print("Quantity:", inventory[item_name])
else:
    print(item_name, "is not available.")

print("\nTotal Items:", len(inventory))
