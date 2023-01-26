# -*- coding: utf-8 -*-

from pathlib import Path
from os import system
from subprocess import getoutput as getout
from dotenv import load_dotenv
from json import load
path = Path(__file__).parent
load_dotenv(path.joinpath(".env"))
host = getout("hostname -I").strip()
port = 5000
url = f"http://{host}:{port}"


def get_input(*args):
    command = " ".join(args)
    out = getout(command).strip()
    return out


def run_command(*args):
    command = " ".join(args)
    return system(command)


def getconfig(filename):
    return load(path.joinpath(f"config/{filename}").open())

