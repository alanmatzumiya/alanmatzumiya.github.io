# -*- coding: utf-8 -*-

from werkzeug.serving import run_simple
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from flask import Flask
from flask_cors import CORS
from settings import (
    app_settings, config, host, port, url, deployment_settings
)
from views.home import home
from views.dispatcher import dispatcher


def init_app():
    app = Flask(**app_settings)
    app.config.update(config)
    CORS(app)
    app.register_blueprint(home)
    return app


def init_dispatcher():
    dispatch = Flask(
        import_name="dispatcher",
        template_folder=app_settings["template_folder"]
    )
    dispatch.config.update(config)
    CORS(dispatch)
    dispatch.register_blueprint(dispatcher)
    return dispatch


class Server:
    app = init_app()
    dispatcher = init_dispatcher()
    host = host
    port = port
    url = url
    settings = deployment_settings

    def run(self):
        application = DispatcherMiddleware(
            self.app, {"/dispatcher": self.dispatcher}
        )
        run_simple(
            self.host, self.port, application, **self.settings
        )
