from build import path, getconfig, create_app, run_server
from flask import render_template, redirect
from datetime import datetime
app = create_app()


@app.route("/", methods=["GET", "POST"])
def home():
    return render_template(
        "index.html",
        cv=getconfig("cv"),
        template=getconfig("template"),
        datetime=datetime.now().strftime("%Y")
    )


@app.route("/update-template/")
def write_template():
    files = {"index": home(), "404": error404(404)}
    for name, file in files.items():
        path.joinpath(f"./{name}.html").open("w").write(file)
    return redirect("/")


@app.errorhandler(404)
def error404(error):
    return render_template(
        "404.html",
        error_message=error.__str__(),
        template=getconfig("template"),
        datetime=datetime.now().strftime("%Y")
    )


if __name__ == "__main__":
    run_server(app)
