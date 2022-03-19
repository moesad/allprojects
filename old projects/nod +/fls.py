
from flask import Flask, render_template

sk = Flask(__name__)


@sk.route("/")
def ss():
    return "hello"


@sk.route("/nn")
def sb():
    return "moh"


if __name__ == "__main__":
    sk.run(port=4555)
