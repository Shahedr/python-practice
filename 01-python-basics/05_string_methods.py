# String Methods Practice

customer_name = "  sample customer  "
product_name = "laptop"
category = "ELECTRONICS"

clean_customer_name = customer_name.strip().title()
formatted_product_name = product_name.title()
formatted_category = category.lower()

print(clean_customer_name)
print(formatted_product_name)
print(formatted_category)

#.strip() cleans spaces at the beginning/end
#.title() formats words like names/products
#.lower() standardizes text to lowercase
#chain methods together like .strip().title()
