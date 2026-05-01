def merge_dicts(d1, d2):
    keys = set(d1) | set(d2)
    return {k: d1.get(k, 0) + d2.get(k, 0) for k in keys}

print(merge_dicts({"A": 5, "B": 10}, {"A": 3, "C": 8}))
