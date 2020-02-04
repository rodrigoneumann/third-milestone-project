from flask import Flask
from seMgmtApp.ext.database import mongo


def create_app(config_object='seMgmtApp.config'):
    app = Flask(__name__)
    app.config.from_object(config_object)
    mongo.init_app(app)
    
    # Views
    from seMgmtApp.blueprints.reg_login.views import reg_login
    from seMgmtApp.blueprints.main.views import main
    from seMgmtApp.blueprints.properties.views import properties
    app.register_blueprint(reg_login)
    app.register_blueprint(main)
    app.register_blueprint(properties)

    return app