from flask import Blueprint

mechanic_bp = Blueprint("mechanic_bp", __name__, url_prefix = "/mechanics")

from . import routes