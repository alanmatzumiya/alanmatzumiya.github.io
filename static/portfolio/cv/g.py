from pathlib import Path
from json import load
path = Path(__file__).parent


def get_template(name):
    folder = path.joinpath(f"templates/{name}")
    data = load(folder.joinpath("data.json").open())
    config = folder.joinpath("config.txt").open().read()
    content = folder.joinpath("content.txt").open().read()
    for k, v in data.items():
        pattern = f"<{k}>"
        if type(v) in (str, int) and pattern in content:
            content = content.replace(pattern, str(v))
    print(content)


get_template("sidebar")