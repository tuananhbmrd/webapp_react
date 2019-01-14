from flask import Blueprint

user_blp = Blueprint("user", __name__)

from . import routes