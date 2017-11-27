import utilities.randomizer_roll_dice_implementations as roll_dice_implementations
import utilities.randomizer_randomize_teams_implementations as randomize_teams_implementations
import random


def roll_dice(num_dice=1, num_sides=6):
    """
    Rolls dice

    :param num_dice: The number of dice that will be rolled
    :param num_sides: The number of sides that each die has
    :return: A list of integers representing each die result.
    """
    return roll_dice_implementations.roll_dice_samson(num_dice, num_sides)


def randomize_teams(num_players, num_teams=2):
    """
    Randomizes teams - if there cannot be the same number of players on each team, then the additional
    players will be placed into random teams. No team can have more than 1 additional player.

    :param num_players: The number of players in total
    :param num_teams: The number of teams the players should be split into
    :return: a list of lists where each list represents a team
    """
    return randomize_teams_implementations.randomize_teams_samson(num_players, num_teams)


def randomize_seating(num_players):
    if num_players <= 0:
        return tuple([])
    return random.sample(range(1, num_players + 1), num_players)
