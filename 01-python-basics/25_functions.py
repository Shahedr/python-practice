# Functions Practice

def calculate_total(price, tax_rate):
    tax_amount = price * tax_rate
    total = price + tax_amount
    return total

order_total = calculate_total(100, 0.08)

print(order_total)
