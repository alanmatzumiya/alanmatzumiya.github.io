# -*- coding: utf-8 -*-

from flask import Blueprint, Flask
from .build import Template, path
from os import system
home = Blueprint("home", __name__)
    

@home.route("/", methods=["GET", "POST"])
def home_view():
    return Template.send_json(dict(response_from="home"))    
    

@home.route("/get-update/")
def git_view():
    system(f"cd {str(path.parent)} && python3 -m main update")
    return Template.send_json(dict(response_from="repository updated successfully"))    
