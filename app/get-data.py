from settings import dataset, getout
from sys import argv


def git_branch():
    return getout("git branch").split()[-1]


def login():
    return getout("echo $( head $HOME/login )")


def secret():
    return getout("echo $( head $HOME/secret )")


for arg in argv[1:]:
    if arg == "login":
        print(login())
    elif arg == "secret":
        print(secret())
    else:
        print(dataset.get(arg))
