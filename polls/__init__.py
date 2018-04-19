from flask import Blueprint

blueprint = Blueprint('polls', __name__, template_folder='templates')

from . import views
