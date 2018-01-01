def game_statistics_caroline(game_results):
    """
    This function will generate all the analysis results on mean,
    win precentage and winning streak.
    """
    player_average_score_caroline(game_results) # average score of each player
    player_win_percentage_caroline(game_results) # win percentage of players
    player_winning_streak_caroline(game_results) # longest winning streak of players

def player_average_score_caroline(game_results):
    """
    This function will print out the average scores for each player in a list.
    """
    num_players, num_rounds = check_input_legitmacy_caroline(game_results)
    if num_players is None and num_rounds is None:
        return -1
    if num_rounds == 0:
        return -1

    avg_score = [float(sum(game_results[i])) / num_rounds for i in range(num_players)]
    ## sum(gameResults[i]): can sum the whole list

    for i in range(len(avg_score)):
        return "Player average score = ", avg_score[i]

def player_win_percentage_caroline(game_results):
    """
    This function will print out the win percentage for each player in a list.
    """
    num_players, num_rounds = check_input_legitmacy_caroline(game_results)
    if num_players is None and num_rounds is None:
        return -1
    if num_rounds == 0:
        return -1

    t_game_results = transpose_game_result_caroline(game_results)
    num_rounds = len(t_game_results)
    num_players = len(game_results)
    win_percentage = []

    for i in range(num_players):
        num_wins = 0
        for j in range(num_rounds):
            max_score = max(t_game_results[j])
            if t_game_results[j][i] == max_score:
                num_wins += 1
        win_percentage.append(float(num_wins)*100 / num_rounds)

    for i in range(len(win_percentage)):
        return "Players win percentage = ", win_percentage[i], "%"

def player_winning_streak_caroline(game_results):
    """
    This function will print out the longest winning steak of each player in a list.
    """
    num_players, num_rounds = check_input_legitmacy_caroline(game_results)
    if num_players is None and num_rounds is None:
        return -1

    t_game_results = transpose_game_result_caroline(game_results)
    num_players = len(game_results)
    num_rounds = len(t_game_results)
    winning_streak = []

    for i in range(num_players):
        num_wins = 0
        for j in range(num_rounds):
            max_score = max(t_game_results[j])
            if t_game_results[j][i] == max_score:
                num_wins += 1
        winning_streak.append(num_wins)

    for i in range(len(winning_streak)):
        return "Player ", i + 1, "\'s winning streak = ", winning_streak[i]

def transpose_game_result_caroline(game_results):
    """
    This function creates a transpost of the input.
    """
    num_players = len(game_results) # identify how many players there are
    num_rounds = len(game_results[0])

    t_game_results = [[] for i in range(num_rounds)] # create a list of list by rounds
    t_game_results = [[game_results[j][i] for j in range(num_players)] for i in range(num_rounds)]
    ## put an output expression in a [] makes it the inner loop

    return t_game_results

def check_input_legitmacy_caroline(game_results):
    """
    This function helps check if the input list is legible for analysis.
    """
    try:
        num_players = len(game_results) # identify how many players there are
        num_rounds = len(game_results[0]) # identify how many rounds there are
        return num_players, num_rounds

    except IndexError: # If not enough rounds
        print "There are not sufficent information."
        return None, None

    except ValueError: # If not enough players
        print "There are not sufficent information."
        return None, None
