from subprocess import getoutput as getout
host = getout("hostname -I").strip()
port = 8000
url = f"http://{host}:{port}"
import_name = "app"
static_folder = "./static"
template_folder = "./templates"
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
