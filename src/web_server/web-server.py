from flask import Flask, render_template, request, \
    redirect, url_for, flash
import src.utilities.randomizer as randomizer

app = Flask(__name__)

# Homepage/Hub
@app.route('/')
@app.route('/boredgames')
def homepage():
    return render_template('index.html')

# Roll dice function
@app.route('/boredgames/rolldice', methods = ['GET', 'POST'])
def dice():
    if request.method == 'POST':
        dies = request.form['dies']
        sides = request.form['sides']
        if not dies or not sides:
            flash("If dies and sides are left empty, we rolled to 1 dice with 6 sides beches~")
            result = randomizer.roll_dice()
        else:
            result = randomizer.roll_dice(int(dies), int(sides))
        return render_template("roll_dice.html", result=result)
    else:
        return render_template('roll_dice.html')

# Team assign
@app.route('/boredgames/teams', methods = ['GET', 'POST'])
def teams():
    if request.method == 'POST':
        players = request.form['players']
        if not players:
            flash("Fill in the number of players first")
            return redirect("/boredgames/teams")
        team = request.form['team']
        if not team:
            result = randomizer.randomize_teams(int(players))
        else:
            result = randomizer.randomize_teams(int(players), int(team))
        return render_template('teams.html', result = result)
    else:
        return render_template('teams.html')

if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)