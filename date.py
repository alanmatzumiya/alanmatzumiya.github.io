from os.path import getctime, getatime, getmtime
from time import ctime, asctime, mktime
from pathlib import Path


def getdate(filepath=None):
    gt = getctime(Path(str(filepath)))

    print(ctime(getmtime(Path(str(filepath)))))
    dtime = list(
        s for s in (
            ctime(gt).split()
            if filepath else ctime().split()
        ) if s
    )
    t = dtime[3].split(":")
    return "{day}-{month}-{year}, {hours}:{minutes}:{seconds}".format(
        day=dtime[2], month=dtime[1], year=dtime[4],
        **{
            s: f"0{t[i]}" if len(t[i]) == 1 else t[i]
            for i, s in enumerate(["hours", "minutes", "seconds"])
        }
    )

print(getdate("/home/alanmatzumiya/Pictures/containers/a/photos/2015/12/02-wa0003.jpg"))