from functools import wraps
import re

from flask import (
    Flask,
    g,
    jsonify,
    redirect,
    render_template,
    request,
    send_from_directory,
)

from database import db, WORDPICKER_DB_URI
from handlers_html import *
from handlers_json import *
from logger import logger
from mlhtml import *
import search

BASE_DIR = os.path.dirname(__file__)

TEST = re.search("root", BASE_DIR) is not None


class MyFlask(Flask):
    def get_send_file_max_age(self, name):
        if re.search("\.(js|css|png|jpg|ico|woff|ttf|eof|svg)$", name.lower()):
            return 28 * 24 * 60 * 60  # 28 days
        return Flask.get_send_file_max_age(self, name)


# Jinja filters
def byte(a, b):
    return (a >> (8 * b)) & 0xFF


def char(a, b):
    return chr(ord(b) + a)


# Route decorators
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        g.entry = None  # Authenticate(request.cookies, request.remote_addr)
        return f(*args, **kwargs)

    return decorated_function


# Flask application
def create_app():
    app = MyFlask(__name__)
    app.config["DEBUG"] = TEST
    # Databases
    app.config["SQLALCHEMY_ECHO"] = TEST
    app.config["SQLALCHEMY_DATABASE_URI"] = WORDPICKER_DB_URI
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.jinja_env.filters["byte"] = byte
    app.jinja_env.filters["char"] = char

    db.init_app(app)

    logger.info(f"config: {app.config}")

    return app


app = create_app()

# Routes


@app.route("/")
def top():
    return redirect("/index")


@app.route("/what", methods=["GET", "POST"])
def logged_out_json():
    page = request.path[1:]
    values = dict([(x, "|".join(request.values.getlist(x))) for x in list(request.values.keys())])
    json = request.get_json()
    if json:
        values.update(json)

    logger.info(f"logged_out_json: page: {page}, values: {values}, json: {json}")

    func = globals().get("handle_%s" % page)
    data = func(None, values, request.files)
    return jsonify(data)


@app.route("/index")
@app.route("/about")
@app.route("/find", methods=["GET", "POST"])
def logged_out_html():
    page = request.path[1:]
    values = dict([(x, "|".join(request.values.getlist(x))) for x in list(request.values.keys())])

    logger.info(f"logged_out_html: page: {page}, values: {values}")

    attrs = html_defaults(request.host, request.user_agent.string)
    attrs.update(values)

    func = globals().get("handle_%s" % page)
    if func:
        attrs.update(func(None, values))
    html = render_template(page + ".html", **attrs)
    return html


@app.route("/game")
@login_required
def logged_in_html():
    page = request.path[1:]
    values = dict([(x, "|".join(request.values.getlist(x))) for x in list(request.values.keys())])

    logger.info(f"logged_in_html: page: {page}, values: {values}")

    attrs = html_defaults(request.host, request.user_agent.string)
    attrs.update(values)

    func = globals().get("handle_%s" % page)
    if func:
        attrs.update(func(g.entry, values))
    return render_template(page + ".html", **attrs)


@app.route("/<path:path>")
def the_rest(path):
    logger.info(f"the_rest: path: {path}")
    return send_from_directory(app.static_folder, path)


if __name__ == "__main__":
    app.run()
