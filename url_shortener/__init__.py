from flask import Flask

from .extensions import db, migrate, manager
from .routes import short
from .models import Link
from flask_migrate import MigrateCommand

def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    db.init_app(app)
    migrate.init_app(app, db)
    manager(app)
    manager.add_command('db', MigrateCommand)

    app.register_blueprint(short)


    return app
