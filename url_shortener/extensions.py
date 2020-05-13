from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()
manager = Manager()