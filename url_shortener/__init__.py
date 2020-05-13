from flask import Flask

from .extensions import db, migrate
from .routes import short
from .models import Link

def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(short)


    return app
