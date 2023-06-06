# -*- coding: utf-8 -*-

from flask import Blueprint, Flask, request, abort
from .build import Template, path
from os import system
home = Blueprint("home", __name__)


@home.route("/", methods=["GET"])
def home_view():
    return Template.send_json(dict(response_from="home"))    
    

@home.route("/get-update/", methods=["POST"])
def git_view():
    req = request.form.to_dict()
    if req.get("token") == "TOKEN":    
        system(f"cd {str(path.parent)} && python3 -m main update")
        return Template.send_json(dict(response_from="repository updated successfully"))    
    else:
        return Template.send_json(req)
