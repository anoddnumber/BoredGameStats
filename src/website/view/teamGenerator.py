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

        playersChecked = check.intChecker(players)
        teamsChecked = check.intChecker(teams)

        if playersChecked > 0:
            if teamsChecked > 0:
                result = randomizer.randomize_teams(playersChecked,
                                                    teamsChecked)
                return render_template('teams.html', result=result,
                                       player_response = players,
                                       team_response = teams)
            if teamsChecked == 0:
                flash('Defaulting to 2 teams')
                result = randomizer.randomize_teams(playersChecked, 2)
                return render_template('teams.html', result=result,
                                       player_response=players,
                                       team_response=teams)
            if teamsChecked < 0:
                flash('Enter whole positive integers only')
                return render_template('teams.html', player_response=players,
                                       team_response=teams)
        elif playersChecked == 0:
            flash('Enter some amount of players at least')
            return render_template('teams.html', player_response=players,
                                   team_response=teams)
        elif playersChecked < 0:
            flash('Enter whole positive integers only')
            return render_template('teams.html', player_response=players,
                                   team_response=teams)

    return render_template('teams.html')
