sudoku_1 = [[5, 3, "", "", 7, "", "", "", ""],
          [6, "", "", 1, 9, 5, "", "", ""],
          ["", 9, 8, "", "", "", "", 6, ""],
          [8, "", "", "", 6, "", "", "", 3],
          [4, "", "", 9, "", 3, "", "", 1],
          [7, "", "", "", 2, "", "", "", 6],
          ["", 6, "", "", "", "", 2, 8, ""],
          ["", "", "", 4, 1, 9, "", "", 5],
          ["", "", "", "", 8, "", "", 7, 9]]


def valid_sudoku(sudoku):
    """Verify if the sudoku is correct."""
    if check_size(sudoku) and check_numbers(sudoku):
        return True
    else:
        return False


def check_size(sudoku):
    """Verify if the sudoku is 9x9."""
    if len(sudoku)!=9:
        return False
    for x in sudoku:
        if len(x)!=9:
            return False
    return True


def check_numbers(sudoku):
    """Verify if the sudoku only has integers from 1 to 9."""
    possibilities = ["",1,2,3,4,5,6,7,8,9]
    for row in sudoku:
        for value in row:
            if value not in possibilities:
                return False
    return True


print(valid_sudoku(sudoku_1))
