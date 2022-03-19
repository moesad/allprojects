from flask import Flask, render_template

mo = Flask(__name__)


@mo.route("/")
def one():
    return render_template("home.html", nome="home")


@mo.route("/new")
def two():
    return render_template("info.html", nome="info")


@mo.route("/about")
def thw():
    return render_template("about.html", nome="about")


if __name__ == "__main__":
    mo.run()
