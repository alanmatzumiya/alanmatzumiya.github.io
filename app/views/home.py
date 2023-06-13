# -*- coding: utf-8 -*-

from flask import Blueprint, request, render_template, jsonify, abort
from .build import Template, path
from os import system
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


@home.route("/api/post/", methods=["GET"])
@home.route("/api/post/<opt>", methods=["POST"])
def api_post(opt=None):
    print(opt)
    if opt == "update":
        return git_update()
    else:
        return abort(404)


def git_update():
    system(f"cd {str(path.parent)} && python3 -m main update")
    return jsonify(response="repository updated successfully")
