from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from url_shortener import db, create_app

app = create_app(config_file='settings.py')

from url_shortener.models import Link
migrate = Migrate(app, db)


manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()