from flask import Blueprint, render_template, request, flash
import src.utilities.randomizer as randomizer

generator_blueprint = Blueprint('generator', __name__)

# Team assign
@generator_blueprint.route('/boredgames/teams', methods = ['GET', 'POST'])
def teams():
    if request.method == 'POST':
        players = request.form['players']
        teams = request.form['team']

        if not players:
            flash("Enter some amount of players at least")
            return render_template('teams.html')

        try:
            players = int(players)
            teams = int(teams)
            result = randomizer.randomize_teams(players, teams)
            if result:
                return render_template('teams.html', result = result)
            else:
                flash("Enter whole positive integers only")
                return render_template('teams.html')

        except ValueError:
            if players:
                if type(players) is not int or players < 0:
                    flash("Enter positive whole integers only")
                    return render_template('teams.html')
                if type(teams) is not int:
                    if not teams:
                        flash("Defaulting to 2 teams")
                        result = randomizer.randomize_teams(players)
                        return render_template('teams.html', result = result)
                    else:
                        flash('Enter positive whole integers only')
                        return render_template('teams.html')
            else:
                pass
    else:
        return render_template('teams.html')
