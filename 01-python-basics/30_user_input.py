# User Input Practice

product_name = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
price = float(input("Enter price: "))

subtotal = quantity * price

print(f"Product: {product_name}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
