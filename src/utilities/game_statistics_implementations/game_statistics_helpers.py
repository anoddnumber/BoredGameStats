def transpose_GameResult_caroline(game_results):
    """This function creats a transpost of the input."""
    num_of_rounds = len(game_results[0])
    num_of_players = len(game_results)

    t_game_results = [[] for i in range(num_of_rounds)] # creat a list of list by rounds
    t_game_results = [[game_results[j][i] for j in range(num_of_players)] for i in range(num_of_rounds)]
    ## put an output expression in a [] makes it the inner loop

    return t_game_results


def wins_jason(my_list, player_id):
    """returns a list of all games and shows if player won or lost.
    Draws count as wins"""
    num_of_players = len(my_list)
    num_of_games = len(my_list[player_id - 1])
    games_won = []
    games_list = []
    # goes through each game per player and compares to ascertain whether or not
    # specified player won that game.
    for i in range(num_of_games):
        for j in range(num_of_players):
            games_list.append(my_list[j][i])
        if my_list[player_id-1][i] == max(games_list):
            games_won.append(1)
        else:
            games_won.append(0)
        games_list = []
    return games_won