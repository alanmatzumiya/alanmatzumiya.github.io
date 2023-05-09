# -*- coding: utf-8 -*-

from flask import Blueprint, redirect, abort, request
from .build import Template, static_url, path
from os import system
portfolio = Blueprint("portfolio", __name__)


@portfolio.route("/portfolio/<opt>/")
def portfolio_view(opt=None):
    if opt == "resume-update":
        return portfolio_update()
    elif opt == "thesis-update":
        return Template.send_json(dict(response="thesis updated successfully"))
    else:
        abort(404)


def portfolio_update():
    fpath = path.parent.joinpath("assets/portfolio/resume")
    system(f'cd {str(fpath)} && python3 build.py')
    return Template.send_json(dict(response="resume updated successfully"))
