def clean_list(data):
    return [item for item in data if item]
print(clean_list(["Alex", "", "John", None, "Riya"]))
