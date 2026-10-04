# File Appending Practice

new_order = "Order 102: Mouse - Quantity 1"

with open("order_summary.txt", "a") as file:
    file.write("\n" + new_order)

#existing file
 #     ↓
#"a" opens in append mode
      ↓
#"\n" starts a new line
#      ↓
#new_order is added
