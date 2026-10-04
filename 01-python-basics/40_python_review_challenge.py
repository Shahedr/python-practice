# Python Fundamentals Review Challenge

orders = [
    {"order_id": 101, "product": "Laptop", "price": 899.99, "quantity": 1},
    {"order_id": 102, "product": "Mouse", "price": 24.99, "quantity": 2},
    {"order_id": 103, "product": "Keyboard", "price": 79.99, "quantity": 3}
]

def calculate_order_total(price, quantity):
    return price * quantity

grand_total = 0

for order in orders:
    order_total = calculate_order_total(order["price"], order["quantity"])
    grand_total = grand_total + order_total

    print(f"{order['product']}: ${order_total:.2f}")

    if order_total >= 200:
        print("High Value Order")

print(f"Grand Total: ${grand_total:.2f}")


#Laptop: $899.99
#Mouse: $49.98
#Keyboard: $239.97

#Start:        $0.00
#+ Laptop:   $899.99
#             ↓
#            $899.99

#+ Mouse:     $49.98
 #            ↓
  #          $949.97

#+ Keyboard: $239.97
  #           ↓
   #       $1,189.94

#Laptop: $899.99
#Mouse: $49.98
#Keyboard: $239.97
#Grand Total: $1189.94
