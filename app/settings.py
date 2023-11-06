# -*- coding: utf-8 -*-

from utils import runcmd
from pathlib import Path
apath = Path(__file__).parent
host = runcmd("hostname -I").split()[-1]
port = 5050
server_port = 5000
url = f"http://{host}:{port}"
app_settings = dict(
    import_name="app",
    template_folder="./templates",
    static_folder="./static"
)
config = dict(
    ENV="development",
    SECRET_KEY="alanmatzumiya",
    SESSION_TYPE="filesystem"
)
deployment_settings = dict(
    use_reloader=True,
    use_debugger=True,
    use_evalex=True
)
dataset = {
    x: globals().get(x)
    for x in dir()
    if not x.startswith("__")
}
