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

# transposes the matrix from by player to by games
def game_scores_matrix_colin(player_scores):
    num_players = len(player_scores)
    num_games = len(player_scores[1])
    game_scores = [[] for game in range(num_games)]
    for x in range(num_games):
        game_scores[x] = [i[x] for i in player_scores]
    return game_scores

# creates a list of max score per game
def max_score_of_a_game_colin(num_games, game_scores):
    max_scores = [[] for game in range(num_games)]
    for x in range(num_games):
        max_scores[x] = max(game_scores[x])
    return max_scores

# compares each player's game score to the max score per game
def win_and_losses_by_player_colin(num_players, num_games, max_scores):
    win_and_losses = [[] for player in range(num_players)]
    for player in range(num_players):
        for game in range(num_games):
            if player_scores[player][game] == max_scores[game]:
                win_and_losses[player].append(1)
            else:
                win_and_losses[player].append(0)
    return win_and_losses

# calculates the percentage of wins
def winning_percentage_colin(num_players, num_games, win_and_losses):
    winning_percentage = []
    for results in range(num_players):
        winning_percentage.append(sum(win_and_losses[results])/num_games)
    return winning_percentage

