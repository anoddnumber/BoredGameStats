from flask import Blueprint, render_template, request, flash
import src.utilities.randomizer as randomizer
import src.utilities.checker as check

dice_blueprint = Blueprint('dice', __name__)

# Roll dice function
@dice_blueprint.route('/boredgames/rolldice', methods = ['GET', 'POST'])
def dice():
    if request.method == 'POST':
        dice = request.form['dice']
        sides = request.form['sides']

        diceChecked = check.intChecker(dice)
        sidesChecked = check.intChecker(sides)

        if diceChecked > 0:
            if sidesChecked > 0:
                result = randomizer.roll_dice(diceChecked, sidesChecked)
                return render_template('roll_dice.html', result = result,
                                       dice_response = dice,
                                       sides_response = sides)
            if sidesChecked == 0:
                flash('Defaulting to 6 sides')
                result = randomizer.roll_dice(diceChecked, sidesChecked)
                return render_template('roll_dice.html', result = result,
                                       dice_response = dice,
                                       sides_response = sides)
            if sidesChecked < 0:
                flash('Enter whole positive integers only')
                return render_template('roll_dice.html', dice_response = dice,
                                       sides_response = sides)
        elif diceChecked == 0:
            if sidesChecked > 0:
                flash('Defaulting to 1 dice')
                result = randomizer.roll_dice(1, sidesChecked)
                return render_template('roll_dice.html', result = result,
                                       dice_response = dice,
                                       sides_response = sides)
            if sidesChecked == 0:
                flash('Defaulting to 1 dice with 6 sides')
                result = randomizer.roll_dice(1, 6)
                return render_template('roll_dice.html', result = result,
                                       dice_response = dice,
                                       sides_response = sides)
            if sidesChecked < 0:
                flash('Enter whole positive integers only')
                return render_template('roll_dice.html', dice_response = dice,
                                       sides_response = sides)
        elif diceChecked < 0:
            flash('Enter whole positive integers only')
            return render_template('roll_dice.html', dice_response = dice,
                                   sides_response = sides)

    return render_template('roll_dice.html')