from flask import Flask

from .view.index import index_blueprint
from .view.rollDice import dice_blueprint
from .view.teamGenerator import generator_blueprint


__author__ = 'samsonwong'
app = Flask(__name__)
app.register_blueprint(index_blueprint)
app.register_blueprint(dice_blueprint)
app.register_blueprint(generator_blueprint)
