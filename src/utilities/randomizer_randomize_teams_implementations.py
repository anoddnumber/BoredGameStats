def randomize_teams_caroline(num_players, num_teams=2): # randomize/separate players into teams
    import random

    if num_players <= 0 or num_teams < 2: # validation
        return []

    player_list = []
    for i in range(1, num_players+1): # iterating through players
        player_list.append(i)

    random.shuffle(player_list) # randomly iteration through player list
    # print player_list

    randomized_teams = []
    for i in range(0, num_teams): #generating empty team lists equal to num of teams
        team = []
        randomized_teams.append(team) # append new lists into a lists

    i = 0
    for x in range(num_players): # going through the shuffled player_list
        while i < num_teams: # this loop will distrube each player into a new team
            randomized_teams[i].append(player_list[x])
            i += 1
            if i == num_teams:
                i = 0 # returning to the start of the team list
            break # To stop the while loop for working but maintain the i value
        # print "i = ", i
    # print randomized_teams
    return randomized_teams


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
