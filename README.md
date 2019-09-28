# Sixteen-Puzzle-Solver
Naive puzzle solver for Simon Tatham's Sixteen puzzle for Python 3.6+.

## Background
The Sixteen puzzle challenges the user to sort a grid of numbers. Unlike the Fifteen puzzle there isn't an empty space. Instead the user must shift entire rows or columns. Every move shifts a number outside of the puzzle grid and it reappears on the other size of the corresponding row or column.
[https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/sixteen.html#3x3](https://www.chiark.greenend.org.uk/~sgtatham/puzzles/js/sixteen.html#3x3)

## Using the solver
The solver takes 3 kinds of command line arguments. The first argument provides the size of each row i.e. the number of columns. The remaining space seperated numbers represent the current state of the puzzle grid entered from left to right, and top to bottom. An optional argument of `-v` or `--verbose` will print the state of the grid after each step in the solver's solution.

Given a puzzle grid:
<pre>
1 4
3 5
6 2
</pre>
`python solver.py 2 -v 1 4 3 5 6 2`
would produce:
<pre>
Starting position.
[1, 4]
[3, 5]
[6, 2]
Column 2 down.
[1, 2]
[3, 4]
[6, 5]
Row 3 right.
[1, 2]
[3, 4]
[5, 6]
</pre>
However without the `-v` flag `python solver.py 2 1 4 3 5 6 2`
would produce:
<pre>
Starting position.
Column 2 down.
Row 3 right.
</pre>
