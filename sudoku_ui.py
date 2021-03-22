#Donald Taylor
#CS325
#Portfolio Project
#2/27/2021

from tkinter import *
from sudoku import *
from sudoku_solver import *

class sudoku_ui:
    def __init__(self):
        self.grids = {
        'easy' : [[9,6,4,2,5,7,8,3,1],
                 [1,5,3,9,8,4,6,7,2],
                 [7,8,2,6,1,3,5,4,9],
                 [2,9,6,3,'',8,4,1,5],
                 [5,1,8,4,2,9,7,'',3],
                 [4,3,7,5,6,1,9,2,8],
                 [6,4,9,8,3,2,1,5,7],
                 ['',2,1,7,4,5,3,9,6],
                 [3,7,5,1,9,6,'',8,4]],

        'medium' : [['',7,2,'','',9,3,1,''],
                 [5,1,'','','',2,'',8,9],
                 ['',9,4,'',3,1,7,5,''],
                 ['',6,'','',5,'',2,3,''],
                 [2,'',1,'','','',5,'',''],
                 ['',3,'',2,8,4,'','',1],
                 ['',2,'',4,1,'','','',''],
                 ['','',7,'',2,8,1,'',5],
                 ['','','','',6,'',9,'','']],

        'hard' : [['','',8,'','','','',5,''],
                ['','','','','','','','',''],
                ['','','','','','','','',''],
                ['',2,'','','',6,'','',''],
                ['','','','','','','','',''],
                ['','','','','','','','',''],
                [9,'','','',5,'','','',''],
                ['','','','','','','','',''],
                ['','','','','','','','','']]}


        self.puzzle = None
        self.entries = []
        self.window = Tk()

        self.output = None
        self.output_frame = None
        self.puzzle_frame = None
        self.button_frame = None
        self.options_frame = None

    def launch_GUI(self):
        """Launches the inital GUI with difficulty options
        """
        self.display_window()
        self.display_header()
        self.display_options()

        self.window.mainloop()

    def create_everything(self, difficulty):
        """Takes the difficulty ('easy', 'medium', or 'hard') as a parameter
        and displays the corresponding puzzle
        """
        self.puzzle = Sudoku(self.grids[difficulty])
        self.options_frame.pack_forget()

        self.generate_text_entries()
        self.display_puzzle()
        self.display_done_button()
        self.create_submission_text()
        self.display_new_puzzle_button()
        self.display_solve_button()

    def hide_everything(self):
        """Hides the puzzle in order to re-display difficulty options
        """
        self.puzzle_frame.pack_forget()
        self.button_frame.pack_forget()
        self.output_frame.pack_forget()

    def display_window(self):
        self.window.title("Sudoku")
        self.window.geometry("500x500")

    def display_header(self):
        header_frame = Frame(master=self.window)
        header_frame.pack()

        header = Label(master = header_frame, text="SUDOKU")
        header.config(font=("Arial Black", 40))
        header.grid(row=0, column=0, sticky = 'w')

    def display_options(self):
        """Displays buttons for Easy, Medium, or Hard puzzle
        """
        self.options_frame = Frame(master=self.window)
        self.options_frame.pack()

        easy_button = Button(self.options_frame, text = 'Easy', height = 3, width = 10, command= lambda : self.create_everything('easy'))
        easy_button.pack(side = LEFT)

        med_button = Button(self.options_frame, text = 'Medium', height = 3, width = 10, command= lambda : self.create_everything('medium'))
        med_button.pack(side = LEFT)

        hard_button = Button(self.options_frame, text = 'Hard', height = 3, width = 10, command= lambda : self.create_everything('hard'))
        hard_button.pack(side = LEFT)

    def generate_text_entries(self):
        """Creates text boxes for all entries
        """
        self.puzzle_frame = Frame(master=self.window)
        self.puzzle_frame.pack()

        self.entries = []
        for i in range(9):
            self.entries.append([])
            for j in range(9):
                entryFrame = Frame(self.puzzle_frame)
                entryFrame.grid(row = i, column = j)
                if j % 3 == 0 and j != 0:
                    vert_line = Label(entryFrame, text = '|')
                    vert_line.pack(side = LEFT)
                if i % 3 == 0 and i != 0:
                    hor_line = Label(entryFrame, text='___')
                    hor_line.pack(side=TOP)
                entry = Entry(entryFrame, width = 2)
                entry.pack(side = LEFT)
                self.entries[i].append(entry)

    def display_puzzle(self):
        """Inserts starting numbers into text boxes
        """
        for i in range(9):
            for j in range(9):
                self.entries[i][j].insert(0,str(self.puzzle.grid[i][j]))


    def display_done_button(self):
        self.button_frame = Frame(master=self.window)
        self.button_frame.pack()

        button = Button(self.button_frame, text = 'Done', height = 3, width = 10, command=self.submit_puzzle)
        button.pack(side = LEFT)

    def create_submission_text(self):
        self.output_frame = Frame(master=self.window)
        self.output_frame.pack()

        self.output = Label(master = self.output_frame, text='')
        self.output.pack()
        self.output.config(font=("Arial Black", 20))

    def submit_puzzle(self):
        """Accepts puzzle as is for submission and displays results
        """
        submission = []
        for i in range(9):
            submission.append([])
            for j in range(9):
                if self.entries[i][j].get() in ['1','2','3','4','5','6','7','8','9']:
                    submission[i].append(int(self.entries[i][j].get()))
                else:
                    submission[i].append('')

        sub_puz = Sudoku(submission)
        output_text = sub_puz.verify_puzzle()

        self.output.config(text=output_text)

    def display_new_puzzle_button(self):
        new_puzzle_button = Button(self.button_frame, text = 'New Puzzle', height = 3, width = 10, command=self.start_over)
        new_puzzle_button.pack(side=LEFT)

    def display_solve_button(self):
        new_puzzle_button = Button(self.button_frame, text = "Solve For Me", height = 3, width = 10, command=self.solve)
        new_puzzle_button.pack(side=LEFT)


    def start_over(self):
        self.hide_everything()

        self.display_options()

    def clear_puzzle(self):
        """Clears text from text boxes
        """
        for i in range(9):
            for j in range(9):
                length = len(self.entries[i][j].get())
                self.entries[i][j].delete(0, length)

        self.output.config(text='')

    def solve(self):
        """Solves the current puzzle
        """
        solved_puzzle = SudokuSolver(self.puzzle)
        if solved_puzzle.solve():
            self.puzzle = solved_puzzle.get_solved_puzzle()
            self.clear_puzzle()
            self.display_puzzle()
        else:
            output_text = "This puzzle cannot be solved!"

            self.output.config(text=output_text)

def main():
    GUI = sudoku_ui()
    GUI.launch_GUI()

if __name__ == '__main__':
    main()
