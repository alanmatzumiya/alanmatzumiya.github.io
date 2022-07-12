from pathlib import Path
from flask import Flask
from flask_cors import CORS
from subprocess import getoutput as prompt
from json import load
path = Path(__file__).parent


def getout(command):
    out = prompt(command).strip()
    print(out)
    return out


def getconfig(key):
    conf = load(path.joinpath("conf.json").open())
    return conf.get(key)


def create_app():
    cfg = getconfig("app")
    folders = dict(
        static_folder=cfg["static_folder"],
        template_folder=cfg["template_folder"]
    )
    app = Flask(__name__, **folders)
    app.env = cfg["env"]
    app.secret_key = cfg["secret_key"]
    CORS(app)
    return app


def run_server(app):
    settings = getconfig("app")["server"]
    settings["host"] = getout("hostname -I")
    app.run(**settings)
