from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from .extensions import db
from .routes import short
from .models import Link


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)
    
    db.init_app(app)
    app.register_blueprint(short)
    migrate = Migrate(app, db)

    manager = Manager(app)
    manager.add_command('db', MigrateCommand)
    return app
