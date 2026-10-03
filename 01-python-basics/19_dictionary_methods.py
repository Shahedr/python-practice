# Dictionary Methods Practice

product = {
    "name": "Laptop",
    "price": 899.99,
    "category": "Electronics"
}

print(product.keys())
print(product.values())
print(product.items())

print(product.get("name"))
print(product.get("discount"))
print(product.get("discount", "Not available"))
