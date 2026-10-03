# Logical Operators Practice

order_total = 150
is_member = True
has_coupon = False
is_sold_out = False

if order_total >= 100 and is_member:
    print("Member qualifies for free shipping")

if order_total >= 100 or has_coupon:
    print("Order qualifies for a benefit")

if not is_sold_out:
    print("Product is available")

#and → both conditions must be true
#or → at least one condition must be true
#not → reverses True/False
