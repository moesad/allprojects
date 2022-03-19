from flask import Flask, render_template
sk = Flask(__name__)


@sk.route("/")
def s1():
    return render_template("one.html", pagetitle="lexus")


@sk.route("/sec")
def s2():
    return render_template("two.html", pagetitle="two")


# @sk.route(r"\the")
# def s3():
#     return render_template("one.html")


if __name__ == "__main__":
    sk.run(port=4555, debug=True)
