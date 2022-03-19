from flask import Flask, render_template

sd = Flask(__name__)


@sd.route("/")
def oo():
    return render_template("fir.html", namey="moe")


if __name__ == "__main__":
    sd.run(port=5555)
