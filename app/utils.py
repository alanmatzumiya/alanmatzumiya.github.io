# -*- coding: utf-8 -*-

from os import system, environ
from subprocess import getoutput as getout


def runcmd(arg, *args):
    command = " && ".join((arg,) + args)
    output = getout(command).strip()
    return output


def shrun(arg, *args):
    command = " && ".join((arg,) + args)
    return system(command)
