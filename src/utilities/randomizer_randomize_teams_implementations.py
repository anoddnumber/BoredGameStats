def randomize_teams_samson(num_players, num_teams=2):
    import random
    if num_players < num_teams:
        return []

    shuffled_list = random.sample(range(1, num_players + 1), num_players)
    num_players_per_team = int(num_players / num_teams)
    num_teams_with_additional_player = num_players % num_teams
    num_players_in_teams_with_additional_player = (num_players_per_team + 1) * num_teams_with_additional_player

    # Create teams that have an additional player first
    randomized_teams = _partition_samson(shuffled_list[:num_players_in_teams_with_additional_player],
                                         num_players_per_team + 1)

    # Add in teams that have no additional player
    randomized_teams += _partition_samson(shuffled_list[num_players_in_teams_with_additional_player:],
                                          num_players_per_team)

    return randomized_teams


def _partition_samson(input_list, partition_len):
    partitions = []
    index = 0
    num_partitions = int(len(input_list) / partition_len)

    for i in range(num_partitions):
        partitions.append(input_list[index: index + partition_len])
        index += partition_len

    return partitions
