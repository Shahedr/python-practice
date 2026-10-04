# Break and Continue Practice

order_ids = [101, 102, 103, 104, 105]

for order_id in order_ids:
    if order_id == 103:
        continue

    print(f"Processing order: {order_id}")

for order_id in order_ids:
    if order_id == 104:
        break

    print(f"Checking order: {order_id}")
