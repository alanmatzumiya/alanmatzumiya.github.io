# -*- coding: utf-8 -*-

from pathlib import Path
from os import system
path = Path(__file__).parent


class Main:
    folder = path.joinpath("docs")
    outfile = path.joinpath("main.tex")

    @classmethod
    def textfile(cls, full=True):
        tex = {            
            name: cls.folder.joinpath(f"{name}.tex").open().read()
            for name in (
                "config", "header", "content", "sidebar", "records"
            )
        }        
        tex["content"] = tex["content"].replace("<HEADER>", tex["header"])
        tex["content"] = tex["content"].replace("<SIDEBAR>", tex["sidebar"])
        tex["content"] = tex["content"].replace(
            "<PAGE-CONTENT>",
            tex["records"] if full else ""
        )
        return "\n\n".join([tex["config"], tex["content"]])

    @classmethod    
    def build(cls):
        fulltext, text = cls.textfile(), cls.textfile(full=False)
        cls.outfile.open("w").write(fulltext)
        system("bash make cv")
        pdf = path.parent.joinpath("cv.pdf")
        pdf.rename(pdf.parent.joinpath("cv-full.pdf"))
        cls.outfile.open("w").write(text)
        system("bash make cv")


if __name__ == "__main__":
    Main.build()
