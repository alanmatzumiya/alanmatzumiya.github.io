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
    if opt == "update":
        portfolio_update()
        git_update()
        return Template.send_json(dict(
            response_from="all data has been updated successfully"
        ))
    else:
        return abort(404)
