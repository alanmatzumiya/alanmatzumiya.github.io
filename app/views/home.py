# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, jsonify, abort
from .build import Template
from .utils import portfolio_update, git_update
home = Blueprint("home", __name__, template_folder=Template.folder, static_folder=Template.static)


@home.route("/", methods=["GET"])
def home_view():
    return render_template("index.html", static=home.static_url_path)


@home.route("/api/get/", methods=["GET"])
@home.route("/api/get/<opt>/", methods=["GET"])
def api_get(opt=None):
    if opt:
        print(opt)
    return jsonify(Template.get_request())


@home.route("/api/post/", methods=["GET", "POST"])
@home.route("/api/post/<opt>/", methods=["GET", "POST"])
def api_post(opt=None):
    req = Template.get_request()
    if opt == "update":
        data = req.get("data")
        if not data:
            return Template.send_json(dict(message="data not found in requests"))
        if data == "portfolio":
            portfolio_update()
            return Template.send_json(dict(
                message="portfolio data has been updated successfully"
            ))
        elif data == "all":
            portfolio_update()
            git_update()
            return Template.send_json(dict(
                message="all data has been updated successfully"
            ))
        else:
            return Template.send_json(dict(message="data invalid"))
    else:
        return abort(404)
