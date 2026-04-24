def product_prices(products, prices):
    return dict(zip(products, prices))
print(product_prices(
    ["Laptop", "Phone", "Tablet"],
    [70000, 30000, 25000]
))