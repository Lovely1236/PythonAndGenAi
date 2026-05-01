def stack_cache():
    stack = []

    for r in ["R1", "R2", "R3"]:
        stack.append(r)

    print("Last Cached Response:", stack.pop())
