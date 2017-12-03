from flask import Flask, render_template, request, redirect, url_for
import random
import src.utilities.randomizer as randomizer

app = Flask(__name__)

@app.route('/')
@app.route('/boredgames')
def homepage():
    return render_template('index.html')

@app.route('/boredgames/rolldice', methods = ['GET', 'POST'])
def dice():
    if request.method == 'POST':
        dies = int(request.form['dies'])
        sides = int(request.form['sides'])
        result = randomizer.roll_dice(dies, sides)
        return render_template("roll_dice.html", result=result)
    else:
        return render_template('roll_dice.html')

@app.route('/boredgames/teams', methods = ['GET', 'POST'])
def teams():
    if request.method == 'POST':
        team = int(request.form['team'])
        players = int(request.form['players'])
        result = randomizer.randomize_teams(players, team)
        return render_template('teams.html', result = result)
    else:
        return render_template('teams.html')

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)