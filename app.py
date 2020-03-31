import flask
from flask import request


app = flask.Flask(__name__)


@app.route("/")

def Home():
    return ("<h1>Hello<h1>")

if __name__=="__main__":
    app.run()

    