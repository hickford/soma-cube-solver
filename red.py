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

def solve(progress, pieces):
    if not pieces:
        # done
        return [True]

    for possible in pieces[0]:
        if numpy.max(progress + possible) > 1:
            continue
        attempt = solve(progress + possible, pieces[1:])
        if attempt:
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
    return distinct

def translations(polycube):
    """List all translation of given cube within 3x3x3 grid"""
    assert polycube[0,0,0] != 0 # so don't have to bother with negative translations

    extents = tuple(coords.max() for coords in numpy.nonzero(three))
    for x in range(3-extents[0]):
        for y in range(3-extents[1]):
            for z in range(3-extents[2]):
                yield numpy.roll(numpy.roll(numpy.roll(polycube, x, 0), y, 1), z, 2)

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

    transformations_by_piece = [transformations(piece) for piece in pieces]
    solution = solve(numpy.zeros((3,3,3),int), transformations_by_piece)
    print(solution)
