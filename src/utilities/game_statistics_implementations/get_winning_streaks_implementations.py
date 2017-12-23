def get_winning_streaks_caroline(game_results):
    from game_statistics_helpers import transpose_GameResult_caroline

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

    return winning_streak


def get_winning_streaks_jason(my_list, player_id):
    from game_statistics_helpers import wins_jason

    wins_list = wins_jason(my_list, player_id)
    small_streak = 0
    big_streak = 0

    # if statements for determining longest streak
    for i in range(len(wins_list)-1):
        if wins_list[i] == 1 and small_streak ==0 :
            small_streak += 1
        if wins_list[i] == 1 and wins_list[i+1] == 1:
            small_streak +=1
            big_streak = max(big_streak, small_streak)
        else:
            small_streak = 0
    return big_streak

def get_winning_streaks_colin(player_scores):
    from game_statistics_helpers import *
    game_scores = game_scores_matrix(player_scores)
    max_scores = max_score_of_a_game(len(player_scores[0]), game_scores)
    win_and_losses = win_and_losses_by_player(len(player_scores), len(player_scores[0]), max_scores)
    
    winning_streak = [[] for player in range(len(player_scores)]
    for player in range(len(player_scores):
        master_counter = 0
        current_counter = 0
        for game in range(len(player_scores[0]):
            if win_and_losses[player][game] == 1:
                current_counter += 1
                if current_counter > master_counter:
                    master_counter = current_counter
            else:
                current_counter = 0
        winning_streak[player].append(master_counter)
    return winning_streak
