from flask import Blueprint, render_template, request, flash
import src.utilities.randomizer as randomizer
import src.utilities.checker as check

generator_blueprint = Blueprint('generator', __name__)


# Team assign
@generator_blueprint.route('/boredgames/teams', methods=['GET', 'POST'])
def teams():
    if request.method == 'POST':
        players = request.form['players']
        teams = request.form['team']

        try:
            players = check.empty_check(players, "")
            teams = check.empty_check(teams, 2)

            if players < 0 or teams < 0:
                flash('Enter positive numbers only')
                return render_template('teams.html', player_response = players,
                                       team_response = teams)

            result = randomizer.randomize_teams(players, teams)
            return render_template('teams.html', result = result,
                                   player_response = players,
                                   team_response = players)

        except ValueError:
            if type(players) is not int:
                flash('Enter at least some players with whole integers')
                return render_template('teams.html', player_response = players,
                                       team_response = teams)
            elif type(teams) is not int:
                flash('Enter whole integers only')
                return render_template('teams.html', player_response = players,
                                       team_response = teams)

    return render_template('teams.html')
