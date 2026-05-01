import re
def check_capital(word):
    if re.match(r'^[A-Z]', word):
        print("Starts with a capital letter.")
    else:
        print("Does not start with a capital letter.")
check_capital("Python")
