import utilities.randomizer_roll_dice_implementations as roll_dice_implementations
import random


def roll_dice_colin_andy(num_dice=1, num_sides=6):
    """
    Rolls dice
    :param num_dice: The number of dice that will be rolled
    :param num_sides: The number of sides that each die has
    :return: A list of integers representing each die result.
    """
    return roll_dice_implementations.roll_dice_samson(num_dice, num_sides)


def randomize_teams(num_players, num_teams=2):
    shuffled_list = random.sample(range(1, num_players + 1), num_players)
    num_players_per_team = int(num_players / num_teams)
    num_teams_with_additional_player = num_players % num_teams
    num_teams_without_additional_player = num_teams - num_teams_with_additional_player

    randomized_teams = []
    index = 0
    for i in range(num_teams_with_additional_player):
        randomized_teams.append(shuffled_list[index:index + num_players_per_team + 1])
        index += num_players_per_team + 1

    for i in range(num_teams_without_additional_player):
        randomized_teams.append(shuffled_list[index:index + num_players_per_team])
        index += num_players_per_team

    return tuple(randomized_teams)


def randomize_seating(num_players):
    if num_players <= 0:
        return tuple([])
    return tuple(random.sample(range(1, num_players + 1), num_players))
