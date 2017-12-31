import utilities.form_checker_implementations.empty_check as checker


def empty_check(input, default):
    """
    Checks form input for invalid entries for integers

    :param input: The inputs from the form
    :return: Input that are valid, 0 for empty string, -1 for anything else
    """
    return checker.check_empty_string(input, default)
