import heapq
def task_scheduler(tasks):
    heapq.heapify(tasks)

    while tasks:
        priority, task = heapq.heappop(tasks)
        print("Processing:", task)

task_scheduler([(2, "Low"), (1, "High"), (3, "Medium")])