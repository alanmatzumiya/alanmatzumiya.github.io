# -*- coding: utf-8 -*-
from build import create_app, run_server
app = create_app()
if __name__ == "__main__":
    run_server(app)
