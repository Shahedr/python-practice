# Default Parameters Practice

def calculate_total(price, tax_rate=0.08):
    tax_amount = price * tax_rate
    total = price + tax_amount
    return total

standard_tax_total = calculate_total(100)
custom_tax_total = calculate_total(100, 0.10)

print(standard_tax_total)
print(custom_tax_total)
