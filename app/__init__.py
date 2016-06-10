from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()  # uses db.init_app in the factory below

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # blueprints for each module
    from app.reports.controllers import reports as reports_module
    app.register_blueprint(reports_module)

    # db
    db.init_app(app)

    return app
