from pathlib import Path
path = Path(__file__).parent
static_path = path.parent.parent
config = path.joinpath("config.txt")
content = path.joinpath("content.txt")
outfile = path.joinpath("main.tex")


def record_files():
    data = []

    def box(size, file):
        return r"\parbox{<SIZE>\linewidth}".replace(
            "<SIZE>", str(size)
        ) + "{\n\t\t\t" + r"\includegraphics[width = 1.0\linewidth]{<FILE>}".replace(
            "<FILE>", str(file)
        ) + "\n}"
    for x in [
        (0.65, "astronomy.pdf"),
        (0.35, "laboratory.png"),
        (0.5, "nuclear-physics.png"),
        (0.5, "workshop-python-2017.pdf"),
        (0.5, "workshop-python-2018.pdf")
    ]:
        data.append(box(x[0], static_path.joinpath("docs", x[1])))
    return "\n".join(data)

cont = content.open().read()
cont = cont.replace("<record-files>", record_files())
print(cont)

r"""

from json import load
from os import listdir, system
from os.path import join





def getfiles(dpath):
    files = {}
    for i in Path(str(dpath)).iterdir():
        if i.is_file():
            files[i.name.split(".")[0]] = str(i)
    return files


class Portfolio:
    path = base_path.joinpath("static/portfolio")
    files = dict()

    def __init__(self):
        self.files["img"] = getfiles(base_path.joinpath("static/img"))
        self.files["cv"] = self.path.joinpath("cv.pdf")
        self.files["docs"] = getfiles(self.path.joinpath("docs"))
        self.files["docs"]["records"] = getfiles(self.path.joinpath("docs/records"))
        self.files["bachelor-degree"] = getfiles(self.path.joinpath("bachelor"))
        self.files["master-degree"] = getfiles(self.path.joinpath("master"))    


class Resume:
    path = base_path.joinpath("resume")
    templates_path = path.joinpath("template")
    
    def __init__(self, template="rows"):
        self.folder = self.templates_path.joinpath(template)
        self.data = load(self.folder.joinpath("data.json").open())
        self.template = dict(
            main="\n".join([
                self.folder.joinpath("config.txt").open().read(),
                self.folder.joinpath("content.txt").open().read()
            ]),
            path=self.path.joinpath("main.tex")                
        )

    def build(self):
        outfile = self.template["main"]
        for i in (
            "name", "formal-photo", "residency", "cell-phone", "email", "presentation"
        ):
            outfile = outfile.replace(f"<{i}>", self.data[i])
        for i in ("skills", "activities"):
            outfile = outfile.replace(f"<{i}>", ", ".join(self.data[i]))
        for i in ("header", "body"):
            outfile = outfile.replace(f"<presentation-{i}>", self.data["presentation"][i])
        
        def add_event(data):
            text = '\cvevent{ <period> }{ <name> }{ <place> }{ <description> } \\ '            
            for i in ("period", "name", "place", "description"):
                text = text.replace(f"<{i}>", data[i])
            return text
        outfile = outfile.replace(
            "<experience>", "\n\n".join([add_event(x) for x in self.data["experience"]])
        )
        outfile = outfile.replace(
            "<education>", "\n\n".join([add_event(x) for x in self.data["education"]])
        )
        self.template["path"].open("w").write(outfile)
        system("bash make")



class Template:
    path = "./template/"
    data = dict(
        docs={i.split(".")[0]: join("./templates", i) for i in listdir("./docs")},
        img={i.split(".")[0]: join("./templates", i) for i in listdir("./img")},
        template="./template/main.json"
    )
    cfg = load(open("data.json"))

    def get(self, name):
        print(self.data)
        data = open(self.data["templates"][name]).read()
        for key, value in self.cfg.items():
            if type(value) == str:
                data = data.replace(f"<{key.upper()}>", value)
        data = data.replace(
            "<APTITUDES>", "\cvtext{" + "".join([
                r'\textbf{- ' + i + r'}\\' for i in self.cfg["aptitudes"]
            ]) + "}"
        )
        data = data.replace(
            "<SKILLS>", "\n".join([
                '\cvskill{' + f'{x["name"]}' + "}{" + x["years"] + "+ yrs}{" + x["scale"] + r'} \\[-2pt]'
                for x in self.cfg["skills"]
            ])
        )
        data = data.replace(
            "<EDUCATION>", "\n".join(
                "".join([r"\cvmetaevent",
                "{" + x["period"] + "}",
                "{" + x["name"] + "}",
                r"{\textbf{" + x["institution"] + "}}",
                "{\cvlist{\item " + x["description"],
                " \href{" + x["href"] + r"}{\textbf{Informacion Aqui}}.}" if x["href"] else ".}",
                "}"
                ]) for x in self.cfg["education"]
            )
        )
        data = data.replace(
            "<EXPERIENCE>", "\n\n".join(
                "".join([
                    r"\cvevent",
                    "{" + x["period"] + "}",
                    "{" + x["name"] + "}",
                    "{" + x["place"] + "}",
                    "{\cvlist{\item " + x["description"],
                    " \href{" + x["href"] + r"}{\textbf{Informacion Aqui}}.}" if x["href"] else r".}",
                    "}"
                ]) for x in self.cfg["experience"]
            )
        )
        with open("cv.tex", "w") as f:
            f.write(data)
        system("bash make")

Resume().build()
"""
