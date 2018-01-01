def read_player_scores_from_file_samson(file_name):
    player_scores = []
    with open(file_name) as f:
        read_data = f.read()
        lines = read_data.split('\n')
        for line in lines:
            if len(line.strip()) > 0:
                player_scores.append([int(score) for score in line.split(',')])
    return player_scores

def read_player_scores_from_file_colin(file_name):
    with open(file_name) as f:
        lines = f.read().splitlines()
    empty_lists = [[] for x in range(len(lines))]
    for x in range(len(empty_lists)):
        empty_lists[x] = [int(x) for x in lines[x].split(',')] # appends each line in txt file as a comma-separated list
    return empty_lists
