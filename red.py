# pieces by height
raw = """
1   2   211 2   2  
11  21  1   11  1  
111  1  1       11 """.lstrip()

raw = """
1   111 112 11  21  112 2   1    1  111 121 11  1  
21    2 1    11  1    1 11  21  111  2  1    11 12 
1             1          1   1   1           1   * """.lstrip()
# yellow            red             blue


raw_pieces = ["\n".join(line[4*i:4*i+3] for line in raw.splitlines()) for i in range(13)]

import numpy
import random

def from_heights(s):
    """Construct 3d array from 2d string of heights"""
    lines = s.splitlines()
    shape = numpy.zeros((4,4,4), bool)
    for y, line in enumerate(lines):
        for x, h in enumerate(line):
            if h == ' ':
                continue
            elif h == '*':
                zs = [1]
            else:
                zs = range(int(h))
            for z in zs:
                shape[x,y,z] = True
    return shape

pieces = [from_heights(s) for s in raw_pieces]
# to do: sort largest to smallest

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

def solve(progress, pieces, i=0):
    if i == len(pieces):
        # done
        return []

    if i == len(pieces)-1:
        print(progress)

    for possible in pieces[i]:
        if numpy.logical_and(progress, possible).any():
            continue
        attempt = solve(numpy.logical_or(progress, possible), pieces, i+1)
        if attempt != False:
            return [possible] + attempt
    return False

def transformations(polycube):
    """List all transformations (rotations and translations) of polycube"""
    transforms = list()

    for translation in translations(polycube):
        transforms.extend(rotations24(translation))

    return distinct(transforms)

def distinct(arrays):
    """Distinct elements from list of arrays"""
    distinct = list()
    for M in arrays:
        if any(numpy.array_equal(M, N) for N in distinct):
            continue
        distinct.append(M)
    random.shuffle(distinct)
    return distinct

def translations(polycube):
    """List all translation of given cube within 4x4x4 grid"""
    # assert polycube[0,0,0] != 0 # so don't have to bother with negative translations

    extents = tuple(coords.max() for coords in numpy.nonzero(polycube))
    for x in range(4-extents[0]):
        for y in range(4-extents[1]):
            for z in range(4-extents[2]):
                yield numpy.roll(numpy.roll(numpy.roll(polycube, x, 0), y, 1), z, 2)

def pretty(solution):
    return sum((i+1) * M for (i, M) in enumerate(solution))

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

    random.shuffle(pieces)
    print("Generating transformations...")
    transformations_by_piece = [transformations(piece) for piece in pieces]
    print("Exploring for solutions...")
    solution = solve(numpy.zeros((4,4,4),int), transformations_by_piece)
    print(pretty(solution))
