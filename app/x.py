import asyncio
import threading


async def do_first():
    print("Running do_first block 1")
    ...
    # Release execution
    await asyncio.sleep(0)
    print("Running do_first block 2")
    ...


async def do_second():
    print("Running do_second block 1")
    ...
    # Release execution
    await asyncio.sleep(0)
    print("Running do_second block 2")
    ...


def first_thread():
    print("Running do_first line 1")
    print("Running do_first line 2")
    print("Running do_first line 3")
    ...


def second_thread():
    print("Running do_second line 1")
    print("Running do_second line 2")
    print("Running do_second line 3")
    ...


async def main_thread():
    await asyncio.sleep(1)
    t1 = threading.Thread(target=first_thread)
    t2 = threading.Thread(target=second_thread)
    # Start threads
    t1.start(), t2.start()
    # Wait threads to complete
    t1.join(), t2.join()


async def main():
    task_1 = asyncio.create_task(do_first())
    task_2 = asyncio.create_task(do_second())
    task_3 = asyncio.create_task(main_thread())
    await asyncio.wait([task_1, task_2, task_3])

if __name__ == "__main__":
    asyncio.run(main())