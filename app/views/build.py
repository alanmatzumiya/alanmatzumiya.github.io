# -*- coding: utf-8 -*-

from flask import json, jsonify, request
from .utils import getdate
from pathlib import Path
from subprocess import getoutput as gout
path = Path(__file__).parent.parent
host = gout("hostname - I").split()[-1]
port = 5000
url = f"http://{host}:{port}"


class Template:
    folder = path.joinpath("templates")
    static = path.joinpath("static")

    @staticmethod
    def get_request():
        datajson = dict()
        for q in request.query_string.decode("utf-8").split("&"):
            t = q.split("=")
            if len(t) == 2:
                datajson[t[0]] = t[-1]
        return datajson

    def error404(self, error=None):
        return self.response(error)

    @staticmethod
    def response(info, **params):
        keys = ("code", "name", "description")
        response = info.get_response()
        response.data = json.dumps(dict(
            {k: getattr(info, k, None) for k in keys},
            date=getdate(), **params
        ))
        response.content_type = "application/json"
        return response

    @staticmethod
    def getdata():
        headers = request.headers
        if headers.get("Content-Type") == "application/json":
            return request.json
        else:
            datajson = dict(date=getdate())
            for q in request.query_string.decode("utf-8").split("&"):
                t = q.split("=")
                if len(t) == 2:
                    datajson[t[0]] = t[-1]
            return jsonify(datajson)

    @staticmethod
    def send_json(sdata: dict, **kwargs):
        sdata.update(kwargs, date=getdate())
        return jsonify(sdata)
