from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

@app.route('/')
@app.route('/boredgames')
def homepage():
    return render_template('index.html')

@app.route('/boredgames/rolldice', methods = ['GET', 'POST'])
def roll_dice(num_dice=1, num_sides=6):
    number = random.randint(1,num_sides)
    if request.method == 'GET':
        return render_template('roll_dice.html', number= number)
    elif request.method == 'POST':
        return redirect(url_for('roll_dice'))
    else:
        return redirect(url_for('homepage'))


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=8000)