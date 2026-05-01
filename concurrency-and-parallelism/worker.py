import multiprocessing
def worker(q):
    while not q.empty():
        order = q.get()
        print(f"Processed {order}")

if __name__ == "__main__":
    q = multiprocessing.Queue()
    orders = ["Order1", "Order2", "Order3"]

    for order in orders:
        q.put(order)

    processes = []
    for _ in range(2):
        p = multiprocessing.Process(target=worker, args=(q,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()