from flask import Blueprint, render_template, request, redirect, flash
import src.utilities.randomizer as randomizer

dice_blueprint = Blueprint('dice', __name__)

# Roll dice function
@dice_blueprint.route('/boredgames/rolldice', methods = ['GET', 'POST'])
def dice():
    if request.method == 'POST':
        dice = request.form['dice']
        sides = request.form['sides']

        try:
            dice = int(dice)
            sides = int(sides)
            result = randomizer.roll_dice(dice, sides)
            if result:
                return render_template("roll_dice.html", result=result)
            else:
                flash("Enter whole positive integers only")
                return render_template('roll_dice.html')

        except ValueError:
            if not dice and not sides:
                flash("Defaulting to 1 dice with 6 sides")
                result = randomizer.roll_dice(1, 6)
                return render_template("roll_dice.html", result=result)
            elif dice:
                if type(sides) is not int or type(dice) is not int:
                    flash("Enter positive whole integers only")
                    return render_template('roll_dice.html')
                if not sides:
                    flash("Defaulting to 6 sides")
                    result = randomizer.roll_dice(dice, 6)
                    return render_template("roll_dice.html", result=result)
            elif sides:
                if type(dice) is not int or type(sides) is not int:
                    flash("Enter positive whole integers only")
                    return render_template('roll_dice.html')
                if not dice:
                    flash("Defaulting to 1 dice")
                    result = randomizer.roll_dice(1, sides)
                    return render_template("roll_dice.html", result=result)
            return render_template('roll_dice.html')

    else:
        return render_template('roll_dice.html')