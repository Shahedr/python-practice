# Scope Practice

tax_rate = 0.08

def calculate_total(price):
    tax_amount = price * tax_rate
    total = price + tax_amount
    return total

order_total = calculate_total(100)

print(order_total)
print(tax_rate)
