# pieces by height
raw = """
1   2  211 2   2
11  21 1   11  1
111  1 1       11""".lstrip()

import numpy

def from_heights(s):
    lines = s.splitlines()
    coords = list()
    for y, line in enumerate(lines):
        for x, h in enumerate(line):
            try:
                h = int(h)
            except ValueError:
                continue
            for z in range(h):
                coords.append(numpy.matrix([[x],[y],[z]]))
    return numpy.hstack(coords)

assert numpy.array_equal(from_heights("31\n2"), numpy.matrix(
    [[0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 1],
     [0, 1, 2, 0, 0, 1]]))

