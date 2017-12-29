def get_win_percentages_caroline(game_results):
    from game_statistics_helpers import transpose_GameResult_caroline

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

    return win_percentage


def get_win_percentages_jason(my_list, player_id):
    from game_statistics_helpers import wins_jason

    return sum(wins_jason(my_list, player_id))/len(my_list[player_id - 1])*100

def condense_winning_percentage(player_scores):
    from game_statistics_helpers import *
    game_scores = game_scores_matrix_colin(player_scores)
    max_scores = max_score_of_a_game_colin(len(player_scores[0]), game_scores)
    win_and_losses = win_and_losses_by_player_colin(len(player_scores), len(player_scores[0]), max_scores)
    return winning_percentage_colin(len(player_scores), len(player_scores[0]), win_and_losses)
