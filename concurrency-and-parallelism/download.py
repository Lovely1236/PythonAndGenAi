import asyncio
async def download(file):
    print(f"Downloading {file}...")
    await asyncio.sleep(1)

async def main_download():
    files = ["dataset1", "dataset2", "dataset3"]
    await asyncio.gather(*(download(f) for f in files))
    print("All downloads complete.")

asyncio.run(main_download())