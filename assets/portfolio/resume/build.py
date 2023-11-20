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
    files = (
        "config",
        "header",
        "content",
        "sidebar",
        "records"
    )

    @classmethod
    def current_age(cls):
        yeardays = 365.2425
        days = (cls.today - cls.birthday).days
        age = int(days / yeardays)
        return age

    @classmethod
    def textfile(cls, full=True):
        config, header, content, sidebar, records = (
            cls.folder.joinpath(f"{name}.tex").open().read() for name in cls.files
        )
        current_age = str(cls.current_age())
        current_year = str(cls.today.year)
        records = records.replace("<CURRENT-YEAR>", current_year)
        content = content.replace("<AGE>", current_age)
        content = content.replace("<CURRENT-YEAR>", current_year)
        content = content.replace("<HEADER>", header)
        content = content.replace("<SIDEBAR>", sidebar)
        content = content.replace(
            "<PAGE-CONTENT>", records if full else ""
        )
        return "\n\n".join([config, content])

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
