def check_empty_string(value, default):
    if not value:
        return default
    else:
        return int(value)