import file_accessor_implementations.read_player_scores_from_file_implementations \
    as read_implementations


def read_player_scores_from_file(file_name):
    """
    Reads the contents of file_name and stores each line as a list of integers.
    If the file does not exist, returns an empty list.
    Ignores any empty lines and whitespaces.

    Every row represents a player's scores.
    Every column represents a game's scores.

    Each line will have n number of scores that are separated by commas.
    Every line will be guaranteed to have the same number of scores.

    For example, a file that contains the following contents has 2 players, each with
    four scores:

    4, 3, 7, 8
    2, 4, 6, 5

    :param file_name: The file to read
    :return: A list of lists that contain the scores as integers
    """
    return read_implementations.read_player_scores_from_file_samson()


def write_player_scores_to_file(scores, file_name):
    """
    Writes the player scores to the file.
    If a file does not exist, creates the file and then writes the player scores into the file.

    Every row represents a player's scores.
    Every column represents a game's scores.

    For example, if a file called 'example.txt' exists and contains the following contents:

    4, 3, 7, 8
    2, 4, 6, 5

    and write_player_scores_to_file([7, 3], 'example.txt') is called,
    then the new file should contain the following:

    4, 3, 7, 8, 7
    2, 4, 6, 5, 3

    :param scores: A list of scores to be added to the file. This should be equal to the number
                    of existing rows in the file (which is the number of players)
    :param file_name: The file to write to
    :return: None (nothing to return)
    """
    pass
