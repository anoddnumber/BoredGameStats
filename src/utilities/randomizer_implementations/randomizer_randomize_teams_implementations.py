def randomize_teams_caroline_jeanette(num_of_players, num_of_teams = 2):  # randomize/separate players into teams
    """This function randomizes/separates players into teams."""
    import src.utilities.randomizer as randomizer

    if num_of_players < 1 or num_of_teams < 1:  # validation
        return []

    players = randomizer.randomize_seating(num_of_players)

    randomized_teams = [ [] for i in range(num_of_teams)] # generating empty team lists which is equal to num of teams
    ## randomized_teams = [[]] * 10

    i = 0
    for x in range(num_of_players):
        if i < num_of_teams:
            randomized_teams[i].append(players[x])
            i += 1
            if i == num_of_teams:
                i = 0  # returning to the start of the team list

    return randomized_teams


def randomize_teams_andy(num_players, num_teams=2):
    from random import randint
    finalTeams = [[] for i in range(num_teams)]
    if num_players >= num_teams > 0:
        teamRandomizer = list(range(num_teams))
        players = list(range(num_players))
        for i in range(len(players)):
            if not teamRandomizer:
                teamRandomizer = list(range(num_teams))
            rollRandomTeam = randint(0, len(teamRandomizer) - 1)
            team = teamRandomizer[rollRandomTeam]
            finalTeams[team].append(players[i])
            teamRandomizer.remove(team)

    return finalTeams


def randomize_teams_jason(num_players, num_teams=2):
    import random
    if num_players <= 0 or num_teams <= 0:
        return []
    else:
        pass

    num_equal_players = num_players // num_teams  # number of equal players per team
    remain_num_players = num_players % num_teams  # number of remaining players
    players = [i for i in range(1, num_players + 1)]  # initialize every player with an individual number
    random.shuffle(players)  # list of all players shuffled
    teams = [[] for _ in range(num_teams)]  # initialize list of teams

    # assign players to teams
    u = 0
    for i in range(num_equal_players):
        for j in range(num_teams):
            teams[j].append(players[u])
            u += 1

    # assign remaining players to teams
    u = 0
    for k in range(remain_num_players):
        teams[u].append(players[len(players) - remain_num_players])
        u += 1

    # print(players)
    return teams


def randomize_teams_colin(num_players, num_teams=2):
    import random
    if num_players < 0 or num_teams < 0:
        return []

    players = [i for i in range(1, num_players+1)]
    teams = [[] for i in range(num_teams)]
    even_num_per_team = num_players // num_teams

    for even_split in range(even_num_per_team):
        for t in range(num_teams):
            removed_player = random.choice(players)
            teams[t].append(removed_player)
            players.remove(removed_player)

    z = 0
    random.shuffle(players)
    for remaining_players in players:
        teams[z].append(remaining_players)
        z += 1
    return teams


def randomize_teams_samson(num_players, num_teams=2):
    import random
    if num_players <= 0 or num_teams <= 0:
        return []

    shuffled_list = random.sample(range(1, num_players + 1), num_players)
    num_players_per_team = int(num_players / num_teams)
    num_teams_with_additional_player = num_players % num_teams if num_players >= num_teams else num_players
    num_players_in_teams_with_additional_player = (num_players_per_team + 1) * num_teams_with_additional_player

    # Create teams that have an additional player first
    randomized_teams = _partition_samson(shuffled_list[:num_players_in_teams_with_additional_player],
                                         num_players_per_team + 1)

    # Add in teams that have no additional player
    randomized_teams += _partition_samson(shuffled_list[num_players_in_teams_with_additional_player:],
                                          num_players_per_team)

    # If there are more teams than there are players, add in teams with no players
    randomized_teams += (num_teams - len(randomized_teams)) * [[]]

    return randomized_teams


def _partition_samson(input_list, partition_len):
    if partition_len <= 0:
        return []
    partitions = []
    index = 0
    num_partitions = int(len(input_list) / partition_len)

    for i in range(num_partitions):
        partitions.append(input_list[index: index + partition_len])
        index += partition_len

    return partitions
