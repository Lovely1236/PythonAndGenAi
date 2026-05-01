from queue import Queue
def process_queue():
    q = Queue()

    for req in ["Req1", "Req2", "Req3"]:
        q.put(req)

    while not q.empty():
        print("Processed:", q.get(), end=" → ")
    print()