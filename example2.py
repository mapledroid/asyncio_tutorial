# example2.py

import time
import asyncio
import aiofile


def normal_main():
    start = time.perf_counter()
    data = []
    for x in range(10 * 1024 * 1024):
        data.append("A")
    for x in range(10):
        write_file(data, f"Nor-File-{x}")
    total_time = time.perf_counter() - start
    print(f"It took a total of {total_time}s to complete with 10 normal 10MB file writes.")

    start = time.perf_counter()
    for x in range(10):
        write_file_small(f"Nor-Small-File-{x}")
    total_time = time.perf_counter() - start
    print(f"It took a total of {total_time}s to complete with 10 normal 100KB files with small writes.")


def write_file(data, filename):
    #print(f"Starting file: {filename}.")
    with open(filename, "w") as f:
        f.write(data.__str__())
    #print(f"Done file: {filename}.")


def write_file_small(filename):
    size = 100 * 1024
    #print(f"Starting file: {filename}.")
    with open(filename, "w") as f:
        for x in range(size):
            f.write("A")
    #print(f"Done file: {filename}.")


async def async_main():
    tasks = []
    data = []
    for x in range(10 * 1024 * 1024):
        data.append("A")
    start = time.perf_counter()
    for x in range(10):
        new_task = asyncio.create_task(async_write_file(data, f"AS-File-{x}"))
        tasks.append(new_task)
    for x in range(10):
        await tasks[x]
    total_time = time.perf_counter() - start
    print(f"It took a total of {total_time}s to complete with 10 async 10MB file writes.")

    tasks2 = []
    start = time.perf_counter()
    for x in range(10):
        new_task = asyncio.create_task(async_write_file_small(f"AS-Small-File-{x}"))
        tasks2.append(new_task)
    for x in range(10):
        await tasks2[x]
    total_time = time.perf_counter() - start
    print(f"It took a total of {total_time}s to complete with 10 async 100KB files with small writes.")


async def async_write_file(data, filename):

    #print(f"Starting file: {filename}.")
    async with aiofile.async_open(filename, "w") as f:
        await f.write(data.__str__())
    #print(f"Done file: {filename}.")


async def async_write_file_small(filename):
    size = 100 * 1024
    #print(f"Starting file: {filename}.")
    async with aiofile.async_open(filename, "w") as f:
        for x in range(size):
            await f.write("A")
    #print(f"Done file: {filename}.")


if __name__ == "__main__":
    normal_main()
    asyncio.run(async_main())
