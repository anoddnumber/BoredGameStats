def checkValidInt(args):
    try:
        args = int(args)
        if args < 0:
            return -1
        else:
            return args

    except ValueError:
        if not args:
            return 0
        if type(args) is not int:
            return -1