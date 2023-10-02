# -*- coding: utf-8 -*-

from datetime import date
from pathlib import Path
from os import system
path = Path(__file__).parent


class Main:
    folder = path.joinpath("docs")
    outfile = path.joinpath("main.tex")
    birthday = date(1992, 9, 14)
    today = date.today()

    @classmethod
    def current_age(cls):
        yeardays = 365.2425
        age = int((cls.today - cls.birthday).days / yeardays)
        return age

    @classmethod
    def textfile(cls, full=True):
        tex = {            
            name: cls.folder.joinpath(f"{name}.tex").open().read()
            for name in (
                "config", "header", "content", "sidebar", "records"
            )
        }
        current_age = str(cls.current_age())
        current_year = str(cls.today.year)
        tex["records"] = tex["records"].replace("<CURRENT-YEAR>", current_year)
        tex["content"] = tex["content"].replace("<AGE>", current_age)
        tex["content"] = tex["content"].replace("<CURRENT-YEAR>", current_year)
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
