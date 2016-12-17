def read_msgs(filename):
    with open(filename) as lf:
        msgs = [line.split() for line in lf.readlines()]
    return msgs