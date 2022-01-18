from flask import Flask
from WebApp.config import Config


def create_app(config_obj=Config):
    app = Flask(__name__)
    app.config.from_object(config_obj)
    from WebApp.BlueprintMain.routes import BlueprintMain
    from WebApp.BlueprintModule1.routes import BlueprintModule1
    from WebApp.BlueprintModule2.routes import BlueprintModule2
    from WebApp.BlueprintModule3.routes import BlueprintModule3
    from WebApp.errors.handlers import errors_handler
    app.register_blueprint(BlueprintMain)
    app.register_blueprint(BlueprintModule1)
    app.register_blueprint(BlueprintModule2)
    app.register_blueprint(BlueprintModule3)
    app.register_blueprint(errors_handler)
    return app
