# -*- coding: utf-8 -*-

from os import system, environ
from subprocess import getoutput as getout
from time import sleep


def timeout():
    sleep(1)


def runcmd(arg, *args):
    command = " && ".join((arg,) + args)
    output = getout(command).strip()
    return output


def shrun(arg, *args):
    command = " && ".join((arg,) + args)
    return system(command)
