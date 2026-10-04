# Try and Except Practice

try:
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    subtotal = price * quantity

    print(f"Subtotal: ${subtotal:.2f}")

except:
    print("Invalid input. Please enter numbers only.")
