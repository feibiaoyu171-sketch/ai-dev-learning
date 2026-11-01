def read_first_line(filename):
    try:
        with open(filename) as f:
            return f.readline()

    except FileNotFoundError:
        return None

