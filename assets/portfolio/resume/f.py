from utils import getconfig, path
img, docs = (path.joinpath(f"resume/{i}").iterdir() for i in ("img", "docs"))


class Template:
    path = path.joinpath("resume/template")
    config = path.joinpath("config.txt")
    content = path.joinpath("content.txt")
    main = path.joinpath("main.tex")
    data = getconfig("author.json")

    def build(self):
        self.main = "\n".join([
            self.config.open().read(),
            self.content.open().read()
        ])
        print(self.main)



from pathlib import Path
from json import load
path = Path(__file__).parent


def get_template():
    folder = path.joinpath(f"templates")
    document = []
    data = load(folder.joinpath("data.json").open())
    document.append(folder.joinpath("config.txt").open().read())
    content = folder.joinpath("content.txt").open().read()
    for k, v in data.items():
        pattern = f"<{k}>"
        if type(v) in (str, int) and pattern in content:
            print(k, v)
            content = content.replace(pattern, str(v))
    document.append(content)
    folder.joinpath("main.tex").open("w").write("\n".join(document))
    print(folder.joinpath("main.tex").open().read())

from pathlib import Path
from json import load, dumps
root_path = Path(__file__).parent
templates_path = root_path.joinpath("templates")


def save_json(filepath, data):
    jsonconfig = dict(
        indent=4,
        sort_keys=True,
        ensure_ascii=False
    )
    Path(str(filepath)).open("w").write(dumps(data, **jsonconfig))


def getjson(filepath):
    return load(Path(str(filepath)).open())


def get_directory():
    data = dict(docs=[], img=[])
    for i in data:
        data[i] = [
            str(j) for j in root_path.joinpath(i).iterdir()
        ]
    return data
get_template()