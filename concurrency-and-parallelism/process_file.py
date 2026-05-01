from multiprocessing import Pool
def process_file(file):
    print(f"Processed {file}")

with Pool() as pool:
    pool.map(process_file, ["file1", "file2", "file3"])
