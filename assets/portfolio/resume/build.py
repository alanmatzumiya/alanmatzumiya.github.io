# -*- coding: utf-8 -*-

from pathlib import Path
from os import system
path = Path(__file__).parent


class Main:
    folder = path.joinpath("docs")
    outfile = path.joinpath("main.tex")

    @classmethod
    def texfile(self):
        tex = {            
            name: self.folder.joinpath(f"{name}.tex").open().read()
            for name in (
                "config", "header", "content", "sidebar", "records"
            )
        }        
        tex["content"] = tex["content"].replace("<HEADER>", tex["header"])
        tex["content"] = tex["content"].replace("<SIDEBAR>", tex["sidebar"])
        tex["content"] = tex["content"].replace("<RECORDS>", tex["records"])
        return "\n\n".join([tex["config"], tex["content"]])

    @classmethod    
    def build(cls):
        cls.outfile.open("w").write(cls.texfile())
        system("bash make")


if __name__ == "__main__":
    Main.build()
