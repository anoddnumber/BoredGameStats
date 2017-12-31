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

            if int(dice) < 1 or int(sides) < 1: # catch the negatives first
                flash("Fill in only positive integers")
                return redirect('boredgames/rolldice')
            else:
                result = randomizer.roll_dice(int(dice), int(sides))
                return render_template("roll_dice.html", result=result)

        except ValueError:
            if dice != "" or sides != "":
                flash("Fill in only integers")
                return redirect('boredgames/rolldice')

            if not dice and not sides:
                flash("Please at least input something")
                return redirect('boredgames/rolldice')

            if dice and not sides:
                if int(dice) < 1:
                    flash("Fill in only positive integers")
                    return redirect('boredgames/rolldice')
                elif sides == "":
                    flash("Defaulting to 6 sides")
                    result = randomizer.roll_dice(int(dice), 6)
                    return render_template("roll_dice.html", result=result)

            elif sides and not dice:
                if int(sides) < 1:
                    flash("Fill in only positive integers")
                    return redirect('boredgames/rolldice')
                elif dice == "":
                    flash('Defaulting to 1 dice')
                    result = randomizer.roll_dice(1, int(sides))
                    return render_template("roll_dice.html", result=result)

    else:
        return render_template('roll_dice.html')
