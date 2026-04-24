employees = {
    101: {"name": "Lovely", "salary": 50000},
    102: {"name": "Rahul", "salary": 60000},
    103: {"name": "Priya", "salary": 55000}
}

emp_id = int(input("Enter Employee ID: "))
if emp_id in employees:
    print("Employee ID:", emp_id)
    print("Name:", employees[emp_id]["name"])
    print("Salary:", employees[emp_id]["salary"])
else:
    print("Employee not found.")