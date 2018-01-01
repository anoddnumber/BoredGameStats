def write_player_scores_from_file_samson(file_name):
    pass

def write_new_score_into_same_file_caroline(new_score, input_file): # Append new scores into the file
    """
    This function will write the new scores into the file.
    """
    from .read_player_scores_from_file_implementations import read_player_score_from_file_caroline  
    player_score = read_player_score_from_file_caroline(input_file) # Import score from file
    player_score.append(new_score) # Append new scores as a new object in list

    num_round = len(player_score)
    num_player = len(player_score[0])

    with open(input_file, 'w') as output_f:
        for i in range(num_round):
            for j in range(num_player):
                output_f.write(str(player_score[i][j]))
                if j != num_player - 1: # Do not put a comma at the end of line or the reading function will think it's reading an empty string
                    output_f.write(",")
            output_f.write("\n")
