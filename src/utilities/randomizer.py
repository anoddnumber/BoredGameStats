import utilities.randomizer_implementations.randomizer_randomize_teams_implementations \
    as randomize_teams_implementations
import utilities.randomizer_implementations.randomizer_roll_dice_implementations \
    as roll_dice_implementations
import utilities.randomizer_implementations.randomizer_randomize_seating_implementations \
    as randomize_seating_implementations


def roll_dice(num_dice=1, num_sides=6):
    """
    Rolls dice

    :param num_dice: The number of dice that will be rolled
    :param num_sides: The number of sides that each die has
    :return: A list of integers representing each die result.
    """
    return roll_dice_implementations.roll_dice_colin_andy(num_dice, num_sides)


def randomize_teams(num_players, num_teams=2):
    """
    Randomizes teams - if there cannot be the same number of players on each team, then the additional
    players will be placed into random teams. No team can have more than 1 additional player.

    :param num_players: The number of players in total
    :param num_teams: The number of teams the players should be split into
    :return: a list of lists where each list represents a team
    """
    return randomize_teams_implementations.randomize_teams_colin(num_players, num_teams)


def randomize_seating(num_players):
    """
    Randomly assigns player seat order
    :param num_players: Total number of players
    :return: list of integers representing randomized player seating
    """
    return randomize_seating_implementations.randomize_seating_andy(num_players)
