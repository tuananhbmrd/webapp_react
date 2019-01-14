from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()
flask_bcrypt = Bcrypt()

def create_app():
    app.config.from_object("app.config")
    db.init_app(app)
    flask_bcrypt.init_app(app)
    migrate.init_app(app, db)
    register_blueprints(app)

    return app

def register_blueprints(app):
    from app.api.user import user_blp
    app.register_blueprint(user_blp)

from app import views