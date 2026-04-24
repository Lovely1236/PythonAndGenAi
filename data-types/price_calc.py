product_name = input("Enter product name: ")
price = float(input("Enter product price: "))
discount_rate = float(input("Enter discount rate (%): "))

discount_amount = (price * discount_rate) / 100
final_price = price - discount_amount

print(f"Product Name: {product_name}")
print(f"Original Price: {price}")
print(f"Discount: {discount_rate}%")
print(f"Final Price: {final_price}")