prices = [120, 250, 80, 400, 150]

print("Product Prices:", prices)

prices.insert(2, 300)
print("After Insertion:", prices)

prices.pop()
print("After Removing Last Item:", prices)

print("Highest Price:", max(prices))
print("Lowest Price:", min(prices))
print("Total Price:", sum(prices))

print("Prices Above 200:")
for price in prices:
    if price > 200:
        print(price)
