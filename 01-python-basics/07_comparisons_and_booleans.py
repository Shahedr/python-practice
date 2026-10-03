order_total = 120
minimum_for_free_shipping = 100
items_in_stock = 8
requested_quantity = 5

qualifies_for_free_shipping = order_total >= minimum_for_free_shipping
enough_stock = items_in_stock >= requested_quantity

print(qualifies_for_free_shipping)
print(enough_stock)
