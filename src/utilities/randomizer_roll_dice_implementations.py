def roll_dice_colin_andy(num_dice=1, num_sides=6):
    from random import randrange
    die_result = []
    if num_dice > 0 and num_sides > 0:
        for x in range(num_dice):
            die_result.append(randrange(1, num_sides + 1))
    return die_result


def roll_dice_caroline_jeanette(num_dice=1, num_sides=6):  # default provided
    import random

    if num_dice <= 0 or num_sides < 1:  # validation
        return []

    rolls_result = []
    for i in range(num_dice):  # generate random numbers within the range of sides
        rolls_result.append(random.randint(1, num_sides))

    return rolls_result


def roll_dice_jason(num_dice=1, num_sides=6):
    import random
    return [random.randint(1, num_sides) for _ in range(num_dice)]


def roll_dice_samson(num_dice=1, num_sides=6):
    import random
    if num_dice <= 0 or num_sides <= 0:
        return []

    dice_rolls = []
    for i in range(num_dice):
        dice_rolls.append(random.randint(1, num_sides))

    return dice_rolls
