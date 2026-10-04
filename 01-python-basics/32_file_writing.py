# File Writing Practice

order_summary = "Order 101: Laptop - Quantity 2"

with open("order_summary.txt", "w") as file:
    file.write(order_summary)
