def get_average_scores_caroline(game_results):
    num_of_players = len(game_results) # identify how many players there are
    num_of_rounds = len(game_results[0]) # identify how many rounds there are

    avg_score = [float(sum(game_results[i]))/num_of_rounds for i in range(num_of_players)]
    return avg_score


def get_average_scores_jason(my_list):
    return sum(my_list)/len(my_list)