from flask import Flask
from semgmtapp.ext.database import mongo
from semgmtapp.config import Config

# Create APP
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    mongo.init_app(app)

    # Routes
    from semgmtapp.blueprints.reg_login.routes import reg_login
    from semgmtapp.blueprints.main.routes import main
    from semgmtapp.blueprints.properties.routes import properties
    from semgmtapp.blueprints.profile.routes import profile
    from semgmtapp.blueprints.errors.routes import errors

    app.register_blueprint(reg_login)
    app.register_blueprint(main)
    app.register_blueprint(properties)
    app.register_blueprint(profile)
    app.register_blueprint(errors)

    return app
