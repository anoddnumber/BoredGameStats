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

        try:
            dice = check.empty_check(dice, 1)
            sides = check.empty_check(sides, 6)

            if dice < 0 or sides < 0:
                flash('Enter positive numbers only')
                return render_template('roll_dice.html', dice_response = dice,
                                       sides_response = sides)
            result = randomizer.roll_dice(dice, sides)
            return render_template('roll_dice.html', result = result,
                                   dice_response = dice,
                                   sides_response = sides)

        except ValueError:
            if type(dice) is not int or type(sides) is not int:
                flash('Enter whole positive integers only')
                return render_template('roll_dice.html', dice_response = dice,
                                       sides_response = sides)

    return render_template('roll_dice.html')