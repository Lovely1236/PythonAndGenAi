def browser_history():
    back_stack = []
    forward_stack = []
    current = None

    # Visit pages
    for page in ["A", "B", "C"]:
        if current:
            back_stack.append(current)
        current = page
        forward_stack.clear()

    # Back
    forward_stack.append(current)
    current = back_stack.pop()

    # Forward
    back_stack.append(current)
    current = forward_stack.pop()

    print("Current Page:", current)

browser_history()