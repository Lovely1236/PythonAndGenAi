orders = ["Pending", "Processing", "Delivered", "Failed", "Pending"]
for status in orders:
    if status == "Failed":
        print("Processing stopped due to Failed status.")
        break
    print("Processing order:", status)