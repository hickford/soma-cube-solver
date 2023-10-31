# Soma cube solver

Backtracking algorithm to solve Soma cube-style assembly puzzles. 

http://www.puzzle-place.com/wiki/Impuzzables

Code
----

Pieces are represented as a 3d array of bits. An interesting problem to solve was [How to calculate all 24 rotations of 3d array?](https://stackoverflow.com/questions/33190042/how-to-calculate-all-24-rotations-of-3d-array).

Example solution:

```
[[[1 4 5]
  [1 4 5]
  [2 2 2]]

 [[7 5 5]
  [1 4 3]
  [6 4 2]]

 [[7 7 3]
  [7 6 3]
  [6 6 3]]]```

Woodwork
--------

Inspired by the book *Creative Puzzles of the World*, I had fun making my own soma cubes. 

![Seven polycubes](https://i.imgur.com/rJm0Tqzl.jpg "Seven polycubes")

![Partially-assembled soma cube](https://i.imgur.com/aZv5gCOl.jpg "Partially-assembled soma cube")
