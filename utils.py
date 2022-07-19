# -*- coding: utf-8 -*-
from json import load
from pathlib import Path
from os import system as sh, listdir as ls
from os.path import join
from subprocess import getoutput as prompt
path = Path(__file__).parent


def input_parser(command, *args):
    cmd = ""
    if type(command) == list:
        cmd += " ".join(command)
    elif type(command) == str:
        cmd += command
    if args:
        cmd += " " + " ".join(args)
    return cmd


def shell(command, *args):
    sh(input_parser(command, *args))


def getout(command, *args):
    return prompt(input_parser(command, *args)).strip()


def get_host(with_scheme=False, default_scheme=True, full_host=True):
    if full_host:
        host = getout("hostname", "-I")
        if with_scheme:
            host = f"http://{host}" if default_scheme else f"https://{host}"
        return host
    else:
        return getout("hostname")


def getdirs(folder):
    return [
        join(folder, i) for i in ls(folder)
    ]


def getconfig(key=None):
    conf = load(path.joinpath("conf.json").open())
    if key:
        return conf.get(key)
    else:
        return conf
