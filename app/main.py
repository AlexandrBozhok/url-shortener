from flask import Flask

from config.db import db_session, init_db
from routers.base import router as base_router

app = Flask(__name__)

app.config.from_object('config.settings.app_settings')

app.template_folder = 'templates'
app.static_folder = 'static'

app.register_blueprint(base_router)


init_db()


@app.errorhandler(404)
def page_not_found(e):
    return '', 404


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()
