from flask import Blueprint, render_template, request, redirect, flash
import src.utilities.randomizer as randomizer

dice_blueprint = Blueprint('dice', __name__)

# Roll dice function
@dice_blueprint.route('/boredgames/rolldice', methods = ['GET', 'POST'])
def dice():
    if request.method == 'POST':
        dice = request.form['dice']
        sides = request.form['sides']

        if dice:
            if type(sides) is not int and sides:
                flash("Fill in with actual whole integers")
                return redirect('boredgames/rolldice')
            else:
                flash("Defaulting to 6 sides")
                result = randomizer.roll_dice(int(dice), 6)
        elif sides:
            if type(dice) is not int and dice:
                flash('Fill in with actual whole integers')
                return redirect('boredgames/rolldice')
            else:
                flash('Defaulting to 1 dice')
                result = randomizer.roll_dice(1, int(sides))
        else:
            result = randomizer.roll_dice(int(dice), int(sides))
        return render_template("roll_dice.html", result=result)
    else:
        return render_template('roll_dice.html')
