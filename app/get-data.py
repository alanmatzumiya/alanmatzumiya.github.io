from settings import dataset
from utils import runcmd
from sys import argv


def git_branch():
    return runcmd("git branch").split()[-1]


def login():
    return runcmd("echo $( head $HOME/login )")


def secret():
    return runcmd("echo $( head $HOME/secret )")


for arg in argv[1:]:
    if arg == "login":
        print(login())
    elif arg == "secret":
        print(secret())
    elif arg == "git-branch":
        print(git_branch())
    else:
        print(dataset.get(arg))
