from flask import render_template, Blueprint

BlueprintModule1 = Blueprint("BlueprintModule1", __name__)


@BlueprintModule1.route("/page1")
def page1():
    return render_template("page1.html")
