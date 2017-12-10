from flask import Blueprint, render_template

index_blueprint = Blueprint('index', __name__)

# Homepage/Hub
@index_blueprint.route('/')
@index_blueprint.route('/boredgames')
def homepage():
    return render_template('index.html')