def averageScore_caroline(game_results):
    """# This function will print out the average scores for each player in a list."""
    num_of_players = len(game_results) # identify how many players there are
    num_of_rounds = len(game_results[0]) # identify how many rounds there are

    avg_score = [float(sum(game_results[i]))/num_of_rounds for i in range(num_of_players)]
    ## sum(gameResults[i]): can sum the whole list

    for i in range(len(avg_score)):
        print "Player average score = ", avg_score[i]

def winPercentage_caroline(game_results):
    "This function will print out the win percentage for each player in a list."
    t_game_results = transpose_GameResult_caroline(game_results)
    num_of_rounds = len(t_game_results)
    num_of_players = len(game_results)
    win_percentage = []

    for j in range(num_of_players):
        cnt = 0
        for i in range(num_of_rounds):
            max_score = max(t_game_results[i])
            if t_game_results[i][j] == max_score:
                cnt += 1
        win_percentage.append(float(cnt)*100/num_of_rounds)

    for i in range(len(win_percentage)):
        print "Players win percentage = ", win_percentage[i], "%"

def winningStreak_caroline(game_results):
    """This function will print out the longest winning steak of each player in a list."""
    t_game_results = transpose_GameResult_caroline(game_results)
    num_of_players = len(game_results)
    num_of_rounds = len(t_game_results)
    winning_streak = []

    for j in range(num_of_players):
        cnt = 0
        for i in range(num_of_rounds):
            max_score = max(t_game_results[i])
            if t_game_results[i][j] == max_score:
                cnt += 1
        winning_streak.append(cnt)

    for i in range(len(winning_streak)):
        print "Player ", i + 1, "\'s winning streak = ", winning_streak[i]

def transpose_GameResult_caroline(game_results):
    """This function creats a transpost of the input."""
    num_of_rounds = len(game_results[0])
    num_of_players = len(game_results)

    t_game_results = [[] for i in range(num_of_rounds)] # creat a list of list by rounds
    t_game_results = [[game_results[j][i] for j in range(num_of_players)] for i in range(num_of_rounds)]
    ## put an output expression in a [] makes it the inner loop

    return t_game_results