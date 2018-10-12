# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 96
Su Doku (Japanese meaning number place) is the name given to a popular puzzle concept. Its origin is unclear, but credit must be attributed to Leonhard Euler who invented a similar, and much more difficult, puzzle idea called Latin Squares. The objective of Su Doku puzzles, however, is to replace the blanks (or zeros) in a 9 by 9 grid in such that each row, column, and 3 by 3 box contains each of the digits 1 to 9. Below is an example of a typical starting puzzle grid and its solution grid.

A well constructed Su Doku puzzle has a unique solution and can be solved by logic, although it may be necessary to employ "guess and test" methods in order to eliminate options (there is much contested opinion over this). The complexity of the search determines the difficulty of the puzzle; the example above is considered easy because it can be solved by straight forward direct deduction.

The 6K text file, sudoku.txt (right click and 'Save Link/Target As...'), contains fifty different Su Doku puzzles ranging in difficulty, but all with unique solutions (the first puzzle in the file is the example above).

By solving all fifty puzzles find the sum of the 3-digit numbers found in the top left corner of each solution grid; for example, 483 is the 3-digit number found in the top left corner of the solution grid above.

Author: Jaime Liew
https://github.com/jaimeliew1/Project_Euler_Solutions


TODO - work out how to duplicate a sudoku class
TODO - more advanced valid_move function (eg. look at the entire column, row, square)
TODO - a better checker for solved
"""

import numpy as np
from itertools import product

class Sudoku(object):
    def __init__(self, X, name=''):
        self.name = name
        self.values = np.array(X)
        self.solvable = True


    def __repr__(self):
        tmp = '{} {} {}|{} {} {}|{} {} {}\n'
        out = str(self.name) + '\n'
        for i, row in enumerate(self.values):
            out += tmp.format(*[str(x) for x in row])
            if i in [2, 5]:
                out += '-'*17 + '\n'
        return out

    def square(self, X, Y):
        # returns the values in the 3x3 square encapsulating the value with
        # coordinates x, y
        squarex, squarey = X//3, Y//3
        out = np.zeros([3, 3], dtype=int)
        for i in [0, 1, 2]:
            for j in [0, 1, 2]:
                y = squarey*3 + i
                x = squarex*3 + j
                out[i, j] = self.values[y, x]
        return out.ravel()

    def valid_moves(self, x, y):
        # returns a list of all valid moves at position x, y.
        # returns None if already solved
        # todo: the criteria for a 'valid move' should be reassessed
        if self.values[y, x] != 0:
            return None
        poss = [1,2,3,4,5,6,7,8,9]
        #loop over rows
        for i in range(9):
            if self.values[i, x] in poss:
                poss.remove(self.values[i, x])
        #loop over columns
        for i in range(9):
            if self.values[y, i] in poss:
                poss.remove(self.values[y, i])

        # loop over values in square
        for val in self.square(x, y):
            if val in poss:
                poss.remove(val)

        return poss



    def solved(self):
    # Checks if sudoku puzzle, X, is successfully solved.
        if 0 in self.values:
            return False

        for row in self.values:
            if any(x not in row for x in [1,2,3,4,5,6,7,8,9]):
                return False

        for column in self.values.T:
            if any(x not in column for x in [1,2,3,4,5,6,7,8,9]):
                return False

        for xsquare, ysquare in product([0, 3, 6], [0, 3, 6]):
            if any(x not in self.square(xsquare, ysquare) for x in [1,2,3,4,5,6,7,8,9]):
                return False

        return True


def sudokuGenerator(filename):
    # returns a generator that yields sudoku puzzles from a file
    with open(filename) as f:
        header = f.readline()

        while header != '':
            values = []
            for i in range(9):
                line = f.readline().strip()
                values.append([int(x) for x in line])
            yield Sudoku(values, name=header[:-1])
            header = f.readline()


def basicSolver(X_, verbose=False):
    # Deduces solutions at positions based on surrounding row, column and
    # square values.
    if verbose:
        print(f'using basic solver on {X_.name}...')
    X = Sudoku(X_.values, X_.name)
    moreSolutions = True
    iteration = 1
    while moreSolutions:
        solutions = []
        for x, y in product([0,1,2,3,4,5,6,7,8], [0,1,2,3,4,5,6,7,8]):
            if X.values[y, x] == 0:
                valid_moves = X.valid_moves(x, y)
                if len(valid_moves) == 0:
                    #print('unsolvable!')
                    X.solvable = False
                    return X
                if len(valid_moves) == 1:
                    solutions.append([x, y, valid_moves[0]])


        for x_, y_, sol in solutions:
            X.values[y_, x_] = sol

        if len(solutions) == 0:
            moreSolutions = False
            if verbose:
                print(f'iteration {iteration}: no solutions')
        else:
            if verbose:
                print(f'iteration {iteration}:')
                print(X)
        iteration +=1
    return X


def guess_check(X_, verbose=False, guess=0):
    # tries to solve puzzle via deduction. If that doesnt work, make a single guess
    # and try by deduction again. This is a recursive function
    if guess > 1:
        return None
    X = Sudoku(X_.values, X_.name)
    X = basicSolver(X)
    if X.solved():
        if verbose:
            print(f'{X_.name} solved with {guess} guesses')
        return X
    elif not X.solvable:
        return None

    for x, y in product([0,1,2,3,4,5,6,7,8], [0,1,2,3,4,5,6,7,8]):
        if X.values[y, x] != 0:
            continue
        for move in X.valid_moves(x, y):
            Xtemp = Sudoku(X.values, X.name)
            Xtemp.values[y, x] = move
            Xtemp = guess_check(Xtemp, verbose=False, guess=guess+1)
            if not Xtemp:
                continue
            if Xtemp.solved():
                return Xtemp
    else:
        return X #I dont think it ever reaches here

if __name__ == "__main__":
    #print(run())
    filename = 'Data/p096_sudoku.txt'
    # basic deduction solver
#    n_solved = 0
#    for X in sudokuGenerator(filename):
#        if basicSolver(X, verbose=False).solved():
#            n_solved += 1
#    print(n_solved)

    # deduction + guessing solver
    n_solved = 0
    eulersum = 0
    for X in sudokuGenerator(filename):
        X_solve = guess_check(X)
        if X_solve.solved():
            eulersum += int(''.join(str(x) for x in X.values[0,0:3]))
            n_solved += 1

            print(X_solve)
    print(n_solved)

    print(eulersum)
















