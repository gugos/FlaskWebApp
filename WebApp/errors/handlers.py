from flask import render_template, Blueprint

errors_handler = Blueprint("errors_handler", __name__)


@errors_handler.app_errorhandler(404)
def error_404(error):
    return render_template("errors/404.html", error=error), 404


@errors_handler.app_errorhandler(403)
def error_403(error):
    return render_template("errors/403.html", error=error), 403


@errors_handler.app_errorhandler(500)
def error_500(error):
    return render_template("errors/500.html", error=error), 500
