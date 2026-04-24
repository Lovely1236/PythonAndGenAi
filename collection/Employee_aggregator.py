from collections import defaultdict
def group_employees(data):
    dept = defaultdict(list)

    for department, employee in data:
        dept[department].append(employee)

    return dict(dept)
print(group_employees([
    ("IT", "Alex"),
    ("HR", "Riya"),
    ("IT", "John")
]))
