import numpy

puzzle = [
    [0,0,0,0,1,0,0,7,0],
    [0,0,4,0,6,5,0,9,0],
    [8,0,6,0,0,0,0,0,0],
    [2,0,7,0,9,3,1,0,0],
    [0,9,0,8,0,1,0,4,0],
    [0,0,3,7,5,0,9,0,2],
    [0,0,0,0,0,0,8,0,7],
    [0,7,0,6,4,0,5,0,0],
    [0,3,0,0,8,0,0,0,0]
]


def checkcell(x,y,test_num):
    global puzzle
    # find which cell we are in
    cur_cell = {"x": (x//3) * 3, "y": (y//3) * 3}
    # check cells
    for row in range(cur_cell["y"], cur_cell["y"]+3):
        for col in range(cur_cell["x"], cur_cell["x"]+3):
            if puzzle[row][col] == test_num:
                return False

    # check row
    for i in range(9):
        # if puzzle row and column = testnum
        if puzzle[y][i] == test_num:
            return False

    # check column
    for i in range(9):
        if puzzle[i][x] == test_num:
            return False
    
    return True


def sudoku_backtrace():
    global puzzle
    for row in range(9):  # for every row
        for col in range(9):  # for every column
            cur_value = puzzle[row][col]  # current value of the selected cell
            if cur_value == 0:
                for canidate_number in range(1,10):  # test every possible number
                    if checkcell(col, row, canidate_number):  # if checkcell returns true
                        puzzle[row][col] = canidate_number  # apply the number to the cell
                        sudoku_backtrace()              # recursion!
                        puzzle[row][col] = 0            # if backtrace fails, reset and and go back a step
                return
    
    print(numpy.matrix(puzzle))
    input("Enter to try for another result ")


# print(checkcell(1,0,9))
sudoku_backtrace()
print("Finished!")

