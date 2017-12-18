def randomize_seating_jason(num_players):
    import random

    if num_players > 0:
        seating_order = [x for x in range(1, num_players+1)]
        random.shuffle(seating_order)
        return seating_order
    else:
        return []


def randomize_seating_caroline(num_players):  # shuffle
    """This function shuffles the list of players."""
    import random

    if num_players < 1: # validation
        return []

    players = list(range(1, num_players + 1))
    random.shuffle(players)
    return players


def randomize_seating_andy(num_players):
    from random import randint
    finalList = []
    if num_players > 0:
        players = list(range(num_players))
        while len(players) > 0:
            player = randint(0, len(players) - 1)
            finalList.append(players[player])
            players.remove(players[player])

    return finalList


def randomized_seating_colin(num_players):
    import random
    if num_players <= 0:
        return []
    seating_order = list(range(1, num_players + 1))
    random.shuffle(seating_order)

    return seating_order


def randomize_seating_samson(num_players):
    import random
    if num_players <= 0:
        return []
    return random.sample(range(1, num_players + 1), num_players)
