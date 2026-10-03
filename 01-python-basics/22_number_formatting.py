# Number Formatting Practice

prices = [24.99, 49.99, 79.99]
tax_rate = 0.08

for price in prices:
    tax_amount = price * tax_rate
    total_price = price + tax_amount

    rounded_total = round(total_price, 2)

    print(rounded_total)
    print(f"${total_price:.2f}")
