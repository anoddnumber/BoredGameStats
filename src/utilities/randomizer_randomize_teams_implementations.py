def randomize_teams_samson(num_players, num_teams=2):
    """
    Randomizes teams - if there cannot be the same number of players on each team, then the additional
    players will be placed into random teams. No team can have more than 1 additional player.

    :param num_players: The number of players in total
    :param num_teams: The number of teams the players should be split into
    :return: a list of lists where each list represents a team
    """
    import random
    shuffled_list = random.sample(range(1, num_players + 1), num_players)
    num_players_per_team = int(num_players / num_teams)
    num_teams_with_additional_player = num_players % num_teams
    num_players_in_teams_with_additional_player = (num_players_per_team + 1) * num_teams_with_additional_player

    # Create teams that have an additional player first
    randomized_teams = _partition_samson(shuffled_list[:num_players_in_teams_with_additional_player],
                                  num_players_per_team + 1)

    # Add in teams that have no additional player
    randomized_teams += _partition_samson(shuffled_list[num_players_in_teams_with_additional_player:], num_players_per_team)

    return randomized_teams


def _partition_samson(input_list, partition_len):
    """
    Given a list, return a list of lists where each list is a partition of length partition_len
    For example, if input_list = [1, 2, 3, 4, 5, 6] and partition_len = 2, the output will be
    [[1, 2], [3, 4], [5, 6]]
    """
    partitions = []
    index = 0
    num_partitions = int(len(input_list) / partition_len)

    for i in range(num_partitions):
        partitions.append(input_list[index: index + partition_len])
        index += partition_len

    return partitions
