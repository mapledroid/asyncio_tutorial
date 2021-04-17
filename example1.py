# example1.py

import time
import asyncio

def normal_task():
    time.sleep(1)

def normal_main():
    start = time.perf_counter()
    for x in range(10):
        normal_task()
    total_time = time.perf_counter() - start
    print(f"It took a total of {total_time}s to complete without async.")


async def async_task():
    await asyncio.sleep(1)

async def async_main():
    start = time.perf_counter()
    tasks = []
    for x in range(10):
        new_task = asyncio.create_task(async_task())
        tasks.append(new_task)
    for x in range(10):
        await tasks[x]
    total_time = time.perf_counter() - start
    print(f"It took a total of {total_time}s to complete with async.")


async def async_main_nowait():
    start = time.perf_counter()
    for x in range(10):
        asyncio.create_task(async_task())

    total_time = time.perf_counter() - start
    print(f"It took a total of {total_time}s to complete with async but no await for each task.")


if __name__ == "__main__":
    # Simulate 10 disk writes that take 1 second each without async
    normal_main()

    # Simulate 10 disk writes that take 1 second each with async
    asyncio.run(async_main())
    asyncio.run(async_main_nowait())