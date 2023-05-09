# -*- coding: utf-8 -*-

from flask import json, jsonify, request
from time import ctime
from pathlib import Path
from subprocess import getoutput as gout
path = Path(__file__).parent.parent
static_url = f'http://{gout("hostname -I").split()[0]}:5000/assets'


def getdate():
    dt = ctime()
    date = list(filter(lambda e: e != "", dt.split()))
    t = date[3].split(":")
    today = dict(
        day=int(date[2]), month=date[1], year=int(date[4]),
        hours=int(t[0]), minutes=int(t[1]), seconds=int(t[2])
    )
    for i in ("hours", "minutes", "seconds"):
        s = str(today[i])
        if len(s) == 1:
            today[i] = f"0{s}"
    return "{day}-{month}-{year}, {hours}:{minutes}:{seconds}".format(**today)


class Template:

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
