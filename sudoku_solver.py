#Donald Taylor
#CS325
#Portfolio Project
#3/7/2021

#This program solves a Sudoku puzzle using the backtracking technique.
#The basic method for the algorithm came from the following article:
#https://en.wikipedia.org/wiki/Sudoku_solving_algorithms


from sudoku import *

class SudokuSolver:
    def __init__(self, puzzle):
        """puzzle is a Sudoku object
        """
        self.puzzle = puzzle.copy()

        #We assign each entry in the grid True or False. True means the entry already has a number and thus
        #cannot be changed on solving. False means the entry is currently blank, and must be filled out by
        #the solver.
        for i in range(9):
            for j in range(9):
                cur = self.puzzle.grid[i][j]
                if cur in [1,2,3,4,5,6,7,8,9]:
                    self.puzzle.grid[i][j] = [cur, True]
                else:
                    self.puzzle.grid[i][j] = [cur, False]

    def verify_puzzle_incomplete(self):
        """Verifies the correctness of a given solution regardless of its completeness.
      Returns True or False.
      """
        rows = self.check_lists_incomplete(self.puzzle.get_rows())
        cols = self.check_lists_incomplete(self.puzzle.get_cols())
        segs = self.check_lists_incomplete(self.puzzle.get_segments())

        if rows and cols and segs:
            return True
        else:
            return False


    def check_lists_incomplete(self, lst):
        """Takes a list of 9 lists (of size 9 or less).
      Returns True if every list contains only numbers 1 through 9 with no duplicates.
      """
        for i in range(9):
            if self.check_list_incomplete(lst[i]) is False:
                return False

        return True


    def check_list_incomplete(self, lst):
        """Takes a list of numbers and determines if it contains 1 through 9 with no duplicates. List doesn't need
        to include all 9 numbers. Returns True or False.
      """
        lst_copy = []
        for i in range(9):
            lst_copy.append(lst[i][0])


        for i in range(1, 10):
            if i in lst_copy:
                lst_copy.remove(i)
            elif '' in lst_copy:
                lst_copy.remove('')

        if len(lst_copy) == 0:
            return True
        else:
            return False

    def solve(self):
        """Solves the puzzle and returns True. If the puzzle is unsolveable returns False
        """
        i = 0
        j = 0

        #If the given puzzle is unsolvable
        if self.verify_puzzle_incomplete() == False:
            return False

        while i < 9 and j < 9:
            if i < 0:
                return False

            #If we are arriving at a cell for the first time, mark it 1, otherwise increment it
            if self.puzzle.grid[i][j][0] == '':
                self.puzzle.grid[i][j][0] = 1
            elif self.puzzle.grid[i][j][1] == False:
                self.puzzle.grid[i][j][0] += 1

            #If all entries are valid
            if self.verify_puzzle_incomplete():
                while True:
                    #keep moving to the next cell
                    if j < 8:
                        j += 1
                    elif j == 8:
                        i += 1
                        j = 0

                    #until we reach one that wasn't in the inital puzzle or we reach the last cell
                    if i == 9 or self.puzzle.grid[i][j][1] == False:
                        break
            else:
                #if we've tried every number in a cell, make it blank
                if self.puzzle.grid[i][j][0] >= 9:
                    self.puzzle.grid[i][j][0] = ''
                    #and keep moving to previous cells
                    while True:
                        if j > 0:
                            j -= 1
                        elif j == 0:
                            i -= 1
                            j = 8
                        #until we reach a cell that wasn't in the intial puzzle
                        if self.puzzle.grid[i][j][1] == False:
                            break

        return True


    def get_solved_puzzle(self):
        """Return a copy of the solved puzzle without the booleans
        """
        new_grid = []

        for i in range(9):
            new_grid.append([])
            for j in range(9):
                new_grid[i].append(self.puzzle.grid[i][j][0])


        new_puzzle = Sudoku(new_grid)
        return new_puzzle







