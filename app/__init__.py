from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
flask_bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config")
    db.init_app(app)
    flask_bcrypt.init_app(app)
    migrate.init_app(app, db)
    register_blueprints(app)

    return app

def register_blueprints(app):
    from app.api.user import user_blp
    from app.api.auth import auth_blp
    from app.views import web_blp
    
    app.register_blueprint(auth_blp)
    app.register_blueprint(user_blp)
    app.register_blueprint(web_blp)
