import utilities.form_checker_implementations.intCheck as checker


def intChecker(input):
    """
    Checks form input for invalid entries for integers

    :param input: The inputs from the form
    :return: Input that are valid, 0 for empty string, -1 for anything else
    """
    return checker.checkValidInt(input)
