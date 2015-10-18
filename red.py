# pieces by height
raw = """
1   2   211 2   2  
11  21  1   11  1  
111  1  1       11 """.lstrip()

raw_pieces = ["\n".join(line[4*i:4*i+3] for line in raw.splitlines()) for i in range(5)]

import numpy

def from_heights(s):
    """Construct 3d array from 2d string of heights"""
    lines = s.splitlines()
    shape = numpy.zeros((3,3,3), int)
    for y, line in enumerate(lines):
        for x, h in enumerate(line):
            try:
                h = int(h)
            except ValueError:
                continue
            for z in range(h):
                shape[x,y,z] = 1
    return shape

pieces = [from_heights(s) for s in raw_pieces]

def rotations24(polycube):
    # imagine shape is pointing in axis 0 (up)

    # 4 rotations about axis 0
    yield from rotations4(polycube, 0)

    # rotate 180 about axis 1, now shape is pointing down in axis 0
    # 4 rotations about axis 0
    yield from rotations4(rot90(polycube, 2, axis=1), 0)

    # rotate 90 or 270 about axis 1, now shape is pointing in axis 2
    # 8 rotations about axis 2
    yield from rotations4(rot90(polycube, axis=1), 2)
    yield from rotations4(rot90(polycube, -1, axis=1), 2)

    # rotate about axis 2, now shape is pointing in axis 1
    # 8 rotations about axis 1
    yield from rotations4(rot90(polycube, axis=2), 1)
    yield from rotations4(rot90(polycube, -1, axis=2), 1)

def rotations4(polycube, axis):
    """List the four rotations of the given cube about the given axis."""
    for i in range(4):
        yield rot90(polycube, i, axis)

def rot90(m, k=1, axis=2):
    """Rotate an array by 90 degrees in the counter-clockwise direction around the given axis"""
    return numpy.swapaxes(numpy.rot90(numpy.swapaxes(m, 2, axis), k), 2, axis)

def solve(pieces):
    # loop over possibles
    pass

def distinct(arrays):
    """Count the number of distinct arrays in the given list of arrays"""
    return len(set(str(x) for x in arrays))

if __name__ == "__main__":
    two = numpy.array([[[1, 0],
        [1, 0]],

       [[1, 1],
        [0, 0]]])

    three = numpy.array([[[1, 1, 0],
        [1, 1, 0],
        [0, 0, 0]],

       [[0, 0, 0],
        [1, 0, 0],
        [1, 0, 0]],

       [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]])
