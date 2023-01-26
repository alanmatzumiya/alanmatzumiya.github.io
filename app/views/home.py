# -*- coding: utf-8 -*-

from flask import Blueprint
from .build import Template
home = Blueprint("home", __name__)


@home.route("/", methods=["GET", "POST"])
def home_view():
    return Template.send_json(dict(response_from="home"))
