# -*- coding: utf-8 -*-
from flask import Flask
from flask_cors import CORS
from views import add_views
from pathlib import Path
from utils import get_host, getconfig
path = Path(__file__).parent


def create_app():
    cfg = getconfig("app")
    folders = {i: cfg[i] for i in ("static_folder", "template_folder")}
    app = Flask(__name__, **folders)
    for i in ("env", "secret_key"):
        setattr(app, i, cfg[i])
    CORS(app)
    add_views(app)
    return app


def run_server(app):
    settings = getconfig("app")["server"]
    settings["host"] = get_host()
    app.run(**settings)
