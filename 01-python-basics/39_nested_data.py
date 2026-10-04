# Nested Data Practice

orders = [
    {"order_id": 101, "product": "Laptop", "price": 899.99},
    {"order_id": 102, "product": "Mouse", "price": 24.99},
    {"order_id": 103, "product": "Keyboard", "price": 79.99}
]

print(orders[0])
print(orders[0]["product"])

for order in orders:
    print(f"{order['order_id']}: {order['product']} - ${order['price']}")
