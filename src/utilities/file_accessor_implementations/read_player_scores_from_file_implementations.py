def read_player_scores_from_file_samson(file_name):
    player_scores = []
    with open(file_name) as f:
        read_data = f.read()
        lines = read_data.split('\n')
        for line in lines:
            if len(line.strip()) > 0:
                player_scores.append([int(score) for score in line.split(',')])
    return player_scores

