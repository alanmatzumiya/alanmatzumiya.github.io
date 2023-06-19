from time import ctime
from pathlib import Path
from os import environ, system
from time import ctime
from subprocess import getoutput as output
path = Path(__file__).parent
    
    
    

def gout(cmd, *cmds):
    lines = list((cmd,) + cmds)
    for line in lines:
        output(line)




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
