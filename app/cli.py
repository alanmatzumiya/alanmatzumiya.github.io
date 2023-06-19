import asyncio
from asyncio import (
    create_subprocess_shell, wait_for,
    TimeoutError, CancelledError
)
from sys import exit


async def write_command():
    try:
        proc = await create_subprocess_shell(
            input("write command to run: "),
            shell=True
        )
        await proc.communicate()
    except CancelledError:
        proc.terminate()


async def run_command(cmd):
    return await create_subprocess_shell(cmd)


async def wait():
    try:
        await wait_for(write_command(), 15)
    except (TimeoutError, KeyboardInterrupt):
        print("Process Terminated")
    await wait()


async def send(cmd):
    return await wait_for(run_command(cmd), 2)


def start():
    return asyncio.run(send("ls"))
