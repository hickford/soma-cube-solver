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

def rotations(polycube):
    for i in range(3):
        # permute axes xyz, yzx, zxy
        polycube = numpy.transpose(polycube, (1, 2, 0))
        for turns in range(4):
            polycube = numpy.rot90(polycube)
            yield polycube

def more(polycube):
    # axes -xzy
    polycube = numpy.flipud(polycube)
    polycube = numpy.swapaxes(polycube, 1, 2)

def rot90(m, k=1, axis=2):
    """Rotate an array by 90 degrees in the counter-clockwise direction around the given axis"""
    return numpy.swapaxis(numpy.rot90(numpy.swapaxes(m, 2, axis), k), 2, axis)

def solve(pieces):
    # loop over possibles
    pass

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
