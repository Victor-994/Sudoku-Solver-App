def find_next_empty(puzzle):
    # finds the next row, col on the puzzle that's not filled yet --> rep with -1
    # return row, col tuple (or (None, None) if there is none)

    #keep in mind that we are using 0-8 for our indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    
    return None, None #if no spaces in the puzzle are empty (-1)

def is_valid(puzzle, guess, row, column): #figures whether a guess is valid
    #returns True if is valid, otherwise False

    #for row
    row_vals =puzzle[row]
    if guess in row_vals:
        return False
    
    #for column
    col_vals = [puzzle[i][column] for i in range(9)]
    if guess in col_vals:
        return False

    #We want to get where the 3x3 square starts and iterates over the 3 values in the row/column
    row_start = (row//3) * 3
    column_start = (column//3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(column_start, column_start + 3):
            if puzzle[r][c] == guess:
                return False
    
    return True

def solve_sudoku(puzzle):
    #solve sudoku using backtracking!
    #our puzzle is a list of lists, where each inner list is a row in our sudoku puzzle
    #return whether a solution exists
    #mutates puzzle to be the solution (if solution exists)

    #step 1: choose somewhere on the puzzle to make a guess
    row, column = find_next_empty(puzzle)

    if row is None:
        return True

    #step 2: for every space to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):
        #step 3: check if this is valid guess
        if is_valid(puzzle, guess, row, column):
            #3.1 if this is valid, then place that guess on the puzzle
            puzzle[row][column] = guess
            #step 4: recursive call our fuction
            if solve_sudoku(puzzle):
                return True
        
        #step 5: if not valid, backtrack and try a new number
        puzzle[row][column] = -1

    #step 6 if none of the numbers work
    return False

if __name__ == '__main__':
    example_board = [
        [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],

        [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],

        [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1,  -1, -1, -1],
        [-1, -1, -1,  -1, -1, -1,  -1, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)
