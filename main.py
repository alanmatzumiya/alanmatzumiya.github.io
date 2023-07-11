from pathlib import Path
from sys import argv
from os import environ, system
from time import ctime
from subprocess import getoutput as output
from multiprocessing import Pool
processes = ("serve", "app", "copy")
installers = ("serve", "app")
root = Path(__file__).parent
app_home = root.joinpath("app")
envfile = root.joinpath(".env")
url = f'http://{output("hostname -I").split()[-1]}'


global dotenv, load_dotenv
try:
    from dotenv import load_dotenv
except ModuleNotFoundError:
    system("pip install python-dotenv")
    from dotenv import load_dotenv


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


def run(option):
    system(f"bash make run-{option}")


def run_option():
    cfg = root.joinpath("_data/config-dev.yml").open().read()
    cfg = cfg.replace("<URL>", url)
    root.joinpath("_config.yml").open("w").write(cfg)
    system("clear")
    with Pool(len(processes)) as p:
        try:
            p.map(run, processes)
        except KeyboardInterrupt:
            print("Shutdown ...")


def install_option():
    system("clear")
    system(f"bash install app")
    system(f"bash install serve")


def read_input():
    opt, args = argv[1] if argv[1:] else "", argv[2:]
    if not opt:
        opt = input("Input option not given. Write option: ")
    if opt == "get":
        if args:
            for arg in args:
                getenv(arg)
        else:
            print("key argument not given")
    elif opt == "set":
        if len(args) % 2 == 0:
            for i in range(len(args) - 1):
                setenv(args[i], args[i + 1])
        else:
            print("key-value data invalid")
    elif opt == "run":
        run_option()
    elif opt == "update":
        setenv("allow-push", "true")
        system("bash push")
    elif opt == "install":
        install_option()
    else:
        print("Invalid option")


if __name__ == "__main__":
    if getenv("allow-push"):
        root.joinpath("_config.yml").open("w").write(
            root.joinpath(
                "_data/config-production.yml"
            ).open().read()
        )
    read_input()
