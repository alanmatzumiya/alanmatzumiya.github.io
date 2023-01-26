# -*- coding: utf-8 -*-

from werkzeug.exceptions import HTTPException
from build import Server
from views.build import Template
server = Server()
app = server.app


@app.errorhandler(HTTPException)
def handle_exception(error):
    return Template().error404(error)


if __name__ == "__main__":
    server.run()
