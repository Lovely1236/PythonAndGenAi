def sales_by_category(data):
    totals = {}

    for category, amount in data:
        totals[category] = totals.get(category, 0) + amount

    return totals
print(sales_by_category([
    ("Electronics", 1000),
    ("Furniture", 2000),
    ("Electronics", 1500)
]))