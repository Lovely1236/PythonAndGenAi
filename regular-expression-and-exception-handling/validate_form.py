import re
def validate_form(name, email, phone):
    try:
        if not re.match(r'^[A-Za-z]+$', name):
            raise ValueError("Invalid name")

        if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
            raise ValueError("Invalid email")

        if not re.match(r'^\d{10}$', phone):
            raise ValueError("Invalid phone number")

        print("Valid inputs.")
    except ValueError as e:
        print(f"Error: {e}")
validate_form("Alex", "alex@corp.com", "9876543210")