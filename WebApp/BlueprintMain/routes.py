from flask import render_template, Blueprint

BlueprintMain = Blueprint("BlueprintMain", __name__)


@BlueprintMain.route("/")
def home():
    return render_template("index.html")
