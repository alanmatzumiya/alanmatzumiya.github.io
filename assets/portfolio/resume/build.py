# -*- coding: utf-8 -*-

from pathlib import Path
from os import system
path = Path(__file__).parent
docs = path.joinpath("docs")
config = docs.joinpath("config.tex").open().read()
main = path.joinpath("main.tex").open("w")
content = docs.joinpath("content.tex").open().read()

for tag in ("header", "sidebar", "records"):
    content = content.replace(
        f"<{tag.upper()}>",
        docs.joinpath(f"{tag}.tex").open().read()
    )

main.write(
    "\n\n".join([config, content])
)
system("bash make")
