# Function Reuse Practice

def calculate_total(price, tax_rate):
    tax_amount = price * tax_rate
    total = price + tax_amount
    return total

laptop_total = calculate_total(899.99, 0.08)
mouse_total = calculate_total(24.99, 0.08)
keyboard_total = calculate_total(79.99, 0.08)

print(laptop_total)
print(mouse_total)
print(keyboard_total)
