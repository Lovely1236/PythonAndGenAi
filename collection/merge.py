def merge_configs(*configs):
    merged = {}

    for config in configs:
        merged.update(config)

    return merged
print(merge_configs(
    {"timeout": 10},
    {"timeout": 20, "debug": True}
))