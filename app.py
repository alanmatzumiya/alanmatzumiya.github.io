from pathlib import Path
from flask import Flask, redirect, render_template, request, jsonify, send_file
from flask_cors import CORS
from subprocess import getoutput as sh
from json import load
path = Path.cwd()
cfg = load(path.joinpath("conf.json").open())
appdata = cfg["app"]
app = Flask(
    __name__, 
    static_folder=appdata["static_folder"], 
    template_folder=appdata["template_folder"]
)
app.env = appdata["env"]
CORS(app)


@app.route("/", methods=["GET", "POST"])
def home():    
    return render_template("index.html", cv=cfg["cv"])


@app.route("/update-template/")
def write_template():
    index_file = Path("./index.html").open("w")
    index = home()    
    index_file.write(index)
    error_file = Path("./404.html").open("w")    
    error = erro404(404)
    error_file.write(error)
    resp = dict(response="template updated")
    return redirect("/")


@app.errorhandler(404)
def erro404(error):
    return render_template("404.html")


def run():
    server = appdata["server"]
    server["host"] = sh("hostname -I").strip()
    app.run(**server)


if __name__ == "__main__":
    run()

