# -*- coding: utf-8 -*-

from os import system
from subprocess import getoutput as getout


def get_input(*args):
    command = " ".join(args)
    out = getout(command).strip()
    return out


def run_command(*args):
    command = " ".join(args)
    return system(command)
