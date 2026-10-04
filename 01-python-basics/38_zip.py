# Zip Practice

products = ["Laptop", "Mouse", "Keyboard"]
prices = [899.99, 24.99, 79.99]

for product, price in zip(products, prices):
    print(f"{product}: ${price}")

#Laptop: $899.99
#Mouse: $24.99
#Keyboard: $79.99
