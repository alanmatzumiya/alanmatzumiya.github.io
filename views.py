# -*- coding: utf-8 -*-
from flask import render_template, redirect
from utils import getconfig, path
from update import copy_data
from datetime import datetime


def add_views(app):

    @app.route("/", methods=["GET", "POST"])
    def home():
        return render_template(
            "index.html",
            template=getconfig("template"),
            datetime=datetime.now().strftime("%Y")
        )

    @app.route("/update-template/")
    def write_template():
        copy_data()
        folder = path.parent.joinpath("gh-pages")
        files = {"index": home(), "404": error404(404)}
        x = getconfig("template")
        files["index"] = files["index"].replace(
            x["bachelor_degree"]["thesis"],
            "static/portfolio/bachelor-thesis.pdf"
        )
        files["index"] = files["index"].replace(
            x["master_degree"]["thesis"],
            "static/portfolio/master-thesis.pdf"
        )
        for name, file in files.items():
            folder.joinpath(f"{name}.html").open("w").write(file)
        return redirect("/")

    @app.errorhandler(404)
    def error404(error):
        return render_template(
            "404.html",
            error_message=error.__str__(),
            template=getconfig("template"),
            datetime=datetime.now().strftime("%Y")
        )
