from flask import render_template, Blueprint

BlueprintModule2 = Blueprint("BlueprintModule2", __name__)


@BlueprintModule2.route("/page2")
def page2():
    return render_template("page2.html")
