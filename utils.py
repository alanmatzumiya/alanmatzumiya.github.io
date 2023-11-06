# -*- coding: utf-8 -*-

from pathlib import Path
from os import environ, system as sh
from time import ctime
from subprocess import getoutput
root = Path(__file__).parent
envfile = root.joinpath(".env")
global dotenv, load_dotenv
try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    sh("pip install python-dotenv")
    from dotenv import load_dotenv


def gout(cmd, *cmds):
    inline = " && ".join((cmd,) + cmds)
    outline = getoutput(inline)
    print(*[
        f"Input: {inline}",
        f"Output: {outline}"
    ], sep="\n")
    return outline


def shrun(cmd, *cmds):
    inline = " && ".join((cmd,) + cmds)
    print(f"Input: {inline}")
    sh(inline)


def getdate():
    dt = ctime()
    date = list(filter(lambda e: e != "", dt.split()))
    t = date[3].split(":")
    today = dict(
        day=int(date[2]), month=date[1], year=int(date[4]),
        hours=int(t[0]), minutes=int(t[1]), seconds=int(t[2])        
    )
    for i in ("hours", "minutes", "seconds"):
        s = str(today[i])
        if len(s) == 1:
            today[i] = f"0{s}"
    return "{day}-{month}-{year}, {hours}:{minutes}:{seconds}".format(**today)


def getenv(key):
    load_dotenv(envfile)
    value = environ.get(key)
    return value


def setenv(key, value, **data):
    for line in envfile.open().readlines():
        if line.endswith("\n"):
            line = line[:-1]
        x = line.split("=")
        data[x[0]] = x[1]
    data["last-update"] = getdate()
    data[key] = value
    envfile.open("w").write("\n".join([
        f"{k}={v}" for k, v in data.items()
    ]))
    load_dotenv(envfile)
