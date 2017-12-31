from flask import Flask

from .view.index import index_blueprint
from .view.roll_dice import dice_blueprint
from .view.team_generator import generator_blueprint


__author__ = 'samsonwong'
app = Flask(__name__)
app.register_blueprint(index_blueprint)
app.register_blueprint(dice_blueprint)
app.register_blueprint(generator_blueprint)
