from collections import OrderedDict
def lru_cache(operations, size):
    cache = OrderedDict()

    for item in operations:
        if item in cache:
            cache.move_to_end(item)
        else:
            if len(cache) >= size:
                cache.popitem(last=False)
            cache[item] = True

    print("Cache:", list(cache.keys()))

lru_cache(["A", "B", "C", "A", "D"], 3)