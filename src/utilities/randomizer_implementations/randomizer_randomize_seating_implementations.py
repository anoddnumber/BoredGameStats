def randomize_seating_jason(num_players):
    import random

    if num_players > 0:
        seating_order = [x for x in range(1, num_players+1)]
        random.shuffle(seating_order)
        return tuple(seating_order)
    else:
        return tuple([])


def randomize_seating_caroline(num_players):  # shuffle
    import random

    if num_players > 0:  # validation
        players_list = [ i for i in range(1, num_players+1)] # iterating through players, starting from player 1
        random.shuffle(players_list)  # randomly iteration through player list
        return players_list
    else:
        return []


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


def randomize_seating_samson(num_players):
    import random
    if num_players <= 0:
        return tuple([])
    return random.sample(range(1, num_players + 1), num_players)
