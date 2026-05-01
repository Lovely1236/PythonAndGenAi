import threading
import time
def query_db(db):
    print(f"Querying {db}...")
    time.sleep(1)

threads = []
for db in ["DB1", "DB2", "DB3"]:
    t = threading.Thread(target=query_db, args=(db,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All queries completed.")
