from flask import render_template, Blueprint

BlueprintModule3 = Blueprint("BlueprintModule3", __name__)


@BlueprintModule3.route("/page3")
def page3():
    return render_template("page3.html")
