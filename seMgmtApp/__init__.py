from flask import Flask
from seMgmtApp.ext.database import mongo
from seMgmtApp.config import Config


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    mongo.init_app(app)


    # Routes
    from seMgmtApp.blueprints.reg_login.routes import reg_login
    from seMgmtApp.blueprints.main.routes import main
    from seMgmtApp.blueprints.properties.routes import properties
    from seMgmtApp.blueprints.profile.routes import profile
    from seMgmtApp.blueprints.errors.routes import errors
    app.register_blueprint(reg_login)
    app.register_blueprint(main)
    app.register_blueprint(properties)
    app.register_blueprint(profile)
    app.register_blueprint(errors)

    return app
