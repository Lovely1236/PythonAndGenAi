def safe_division(a, b):
    try:
        result = a / b
        print(result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except TypeError:
        print("Error: Invalid input type.")

safe_division(20, 'a')