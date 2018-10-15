# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 96
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions



"""

import numpy as np
from itertools import product
from copy import deepcopy

def solve(X, verbose=False, moves = []):
    # Recusrive function that solves sudoku puzzles. deduces the next best move
    # and enters the function again. Returns the complete puzzle, or None if no
    # solution can be found.
    X = deepcopy(X)
    # [list/set of possible entries, y position, x position, if it was guessed]
    best_guess = [[None]*100, 0, 0, False]
    for i, j in product(range(9), range(9)):
        if X[i, j] != 0:
            continue
        possibilities = set(range(1, 10))
        possibilities -= set(X[i, :]) # eliminate values in same row
        possibilities -= set(X[:, j]) # eliminate values in same column
        # Eliminate values in same 3x3 square
        possibilities -= set(X[i//3*3:(i//3 + 1)*3, j//3*3:(j//3 + 1)*3].ravel())

        if len(possibilities) == 0:
            # if there are no possible entries in an empty square,
            # the puzzle is invalid.
            return None, None
        elif len(possibilities) < len(best_guess[0]):
            # keep the value and position of the square with the least possible
            # entries
            best_guess = [possibilities, i, j]

    if None in best_guess[0]:
        # The puzzle is solved if no more guesses are made.
        return X, moves
    for entry in best_guess[0]:
        # make one move and recurse.
        X[best_guess[1], best_guess[2]] = entry
        guessed = len(best_guess[0]) > 1
        XX, theseMoves = solve(X, moves=moves + [[entry, best_guess[1], best_guess[2], guessed]])
        if XX is not None:
            # If a valid solution is returned, close the recursive loop
            return XX, theseMoves
    # if none of the guesses yielded a solution, yield nothing.
    return None, None

def run():
    eulersum = 0
    with open('Data/p096_sudoku.txt') as f:
        for i in range(50):
            f.readline()
            X = []
            for _ in range(9):
                X.append([int(val) for val in f.readline().strip()])
            XX, moves = solve(np.array(X))
            eulersum += int(''.join(str(x) for x in np.array(XX)[0, :3]))
    return eulersum


if __name__ == "__main__":
    print(run())























