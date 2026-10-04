# Keyword Arguments Practice

def calculate_total(price, tax_rate=0.08):
    tax_amount = price * tax_rate
    total = price + tax_amount
    return total

first_total = calculate_total(price=100, tax_rate=0.08)
second_total = calculate_total(tax_rate=0.10, price=200)

print(first_total)
print(second_total)
