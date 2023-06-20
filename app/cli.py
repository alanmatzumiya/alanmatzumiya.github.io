from wsgiref.util import setup_testing_defaults
from wsgiref.simple_server import make_server
import asyncio
from asyncio import (
    create_subprocess_shell, wait_for,
    TimeoutError, CancelledError
)


async def write_command():
    procs = None
    try:
        procs = await create_subprocess_shell(
            input("write command to run: "),
            shell=True
        )
        await procs.communicate()
    except CancelledError:
        procs.terminate()


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


def server_response(environ, start_response):
    setup_testing_defaults(environ)
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)
    ret = [("%s: %s\n" % (key, value)).encode("utf-8")
           for key, value in environ.items()]
    return ret


def init_server():
    with make_server('', 8000, server_response) as httpd:
        print("Serving on port 8000...")
        httpd.serve_forever()
