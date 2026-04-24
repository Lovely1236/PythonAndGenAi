def normalize_ids(ids):
    result = []
    for item in ids:
        item = item.upper().replace("_", "-")
        result.append(item)
    return result
print(normalize_ids(["prod-001", "PROD_002", "prod-003"]))