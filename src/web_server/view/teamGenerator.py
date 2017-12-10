from flask import Blueprint, render_template, request, redirect, flash
import src.utilities.randomizer as randomizer

generator_blueprint = Blueprint('generator', __name__)

# Team assign
@generator_blueprint.route('/boredgames/teams', methods = ['GET', 'POST'])
def teams():
    if request.method == 'POST':
        players = request.form['players']
        if not players or type(players) is not int:
            flash("Fill in an actual number for players first")
            return redirect("/boredgames/teams")
        team = request.form['team']
        if not team:
            result = randomizer.randomize_teams(int(players))
        else:
            result = randomizer.randomize_teams(int(players), int(team))
        return render_template('teams.html', result = result)
    else:
        return render_template('teams.html')