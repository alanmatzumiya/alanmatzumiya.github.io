from utils import path, shell
git_page = path.parent.joinpath("gh-pages")


def push():
    shell(" && ".join([
        f"cd {str(git_page)}", "bash push"
    ]))


def copy_data():
    for x in ["css", "img", "js", "favicon.ico"]:
        shell(
            f"cp -r -u {path.joinpath(f'./static/{x}')} {git_page}/static"
        )
    for x in [
        ("cv/cv.pdf", "cv.pdf"),
        ("bachelor/thesis.pdf", "bachelor-thesis.pdf"),
        ("master/thesis/thesis.pdf", "master-thesis.pdf")
    ]:
        shell(
            f"cp -r -u {path.joinpath(f'static/portfolio/{x[0]}')} {git_page}/static/portfolio/{x[1]}"
        )
