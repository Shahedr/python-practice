# List Comprehensions Practice

prices = [24.99, 49.99, 79.99]

prices_with_tax = [price * 1.08 for price in prices]

print(prices_with_tax)

rounded_prices = [round(price, 2) for price in prices_with_tax]

print(rounded_prices)

#original prices → taxed prices → rounded prices
