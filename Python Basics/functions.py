def greet_user(name):
    print("Welcome,", name)


def calculate_bill(price, quantity, discount=0):
    amount = price * quantity
    final_amount = amount - (amount * discount / 100)
    return final_amount


def show_bill(customer, amount):
    print("\nCustomer:", customer)
    print("Final Bill: Rs.", amount)


customer_name = input("Enter customer name: ")
greet_user(customer_name)

unit_price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

bill = calculate_bill(unit_price, quantity, 10)
show_bill(customer_name, bill)
