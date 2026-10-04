# Mini Order Analyzer

orders = [
    {"order_id": 101, "product": "Laptop", "price": 899.99, "quantity": 1},
    {"order_id": 102, "product": "Mouse", "price": 24.99, "quantity": 2},
    {"order_id": 103, "product": "Keyboard", "price": 79.99, "quantity": 3},
    {"order_id": 104, "product": "Monitor", "price": 249.99, "quantity": 1}
]

def calculate_order_total(price, quantity):
    return price * quantity

grand_total = 0
high_value_orders = 0

for order in orders:
    order_total = calculate_order_total(order["price"], order["quantity"])
    grand_total = grand_total + order_total

    print(f"{order['order_id']} - {order['product']}: ${order_total:.2f}")

    if order_total >= 200:
        print("High Value Order")
        high_value_orders = high_value_orders + 1

total_orders = len(orders)
average_order_value = grand_total / total_orders

print(f"Total Orders: {total_orders}")
print(f"High Value Orders: {high_value_orders}")
print(f"Grand Total: ${grand_total:.2f}")
print(f"Average Order Value: ${average_order_value:.2f}")

#Total Orders: 4
#High Value Orders: 3
#Grand Total: $1439.93
#Average Order Value: $359.98
