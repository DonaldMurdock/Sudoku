#Donald Taylor
#CS325
#Portfolio Project
#2/27/2021

class Sudoku:
    def __init__(self, grid):
        self.grid = grid


    def __str__(self):
        output = ""

        for i in range(9):
            if i % 3 == 0:
                output += '_____________________' + '\n'
            for j in range(9):
                if j % 3 == 0:
                    output += '|'
                output += str(self.grid[i][j]) + ' '
            output += '|' + '\n'
        output += '_____________________'


        return output

    def get_segments(self):
        """returns a list of 9 'segments'. Each segment is a list containing the numbers in each segment
        """
        segments = []

        for i in range(3):
            for j in range(3):
                segments.append(self.get_segment(i,j))

        return segments

    def get_segment(self,row, col):
        """Returns a list containing the numbers in a single segment.
        The segment is provided by the row and col parameters
        """
        segment = []
        for i in range(3):
            for j in range(3):
                segment.append(self.grid[i+row * 3][j+col * 3])

        return segment

    def get_rows(self):
        """Returns a list containing all the rows in the puzzle
        """
        rows = []
        for i in range(9):
            rows.append(self.grid[i])

        return rows

    def get_cols(self):
        """Returns a list containing all the columns in the puzzle
        """
        cols = []
        for j in range(9):
            col = []
            for i in range(9):
                col.append(self.grid[i][j])
            cols.append(col)

        return cols


    def verify_puzzle(self):
        """Verifies the correctness of a given solution.
        Returns True or False.
        """
        rows = self.check_lists(self.get_rows())
        cols = self.check_lists(self.get_cols())
        segs = self.check_lists(self.get_segments())

        if rows and cols and segs:
            return 'SOLVED'
        else:
            return 'NOT SOLVED, TRY AGAIN'

    def check_lists(self, lst):
        """Takes a list of 9 lists, each containing 9 numbers.
        Returns True if every list contains 1 through 9
        """
        for i in range(9):
            if self.check_list(lst[i]) is False:
                return False

        return True

    def check_list(self,lst):
        """Takes a list of 9 numbers and determines if it contains 1 through 9.
        Returns True or False.
        """
        lst_copy = lst.copy()
        for i in range(1, 10):
            if i in lst_copy:
                lst_copy.remove(i)
            else:
                return False

        if len(lst_copy) == 0:
            return True
        else:
            return False

    def copy(self):
        """returns a copy of the puzzle"""
        new_grid = []
        for row in self.get_rows():
            new_grid.append(row.copy())

        new_sudoku = Sudoku(new_grid)
        return new_sudoku

