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

def read_player_score_from_file_caroline(input_file): # Read a file and turn it into a list of list
    """
    This function will read players scores from a file and convert it into a list of list containing player scores.
    """
    scores = []
    with open(input_file, 'r') as input_f: # This will make sure python will close the file
        for line in iter(input_f): # This function can iterate through the txt file line by line
            if line != "": # Checking for empty file
                new_list = turn_string_into_list_caroline(line)
                scores.append(new_list)
            else:
                return []
        return scores
    
def turn_string_into_list_caroline(line):
    """
    This function will turn the string into a list without characters you do not want.
    """
    line = line.rstrip().split(',')
    length = len(line)
    new_list = [int(line[i]) for i in range(length)]
    return new_list
