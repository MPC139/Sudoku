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
    if check_size(sudoku) and check_numbers(sudoku) and check_repetitions_row(sudoku) and check_repetitions_column(sudoku) and check_repetitions_block(sudoku):
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

def check_repetitions_row(sudoku):
    """Verify if there are repetitions in the row of the sudoku."""
    for row in sudoku:
        for value in row:
            if value != "":
                if row.count(value) != 1:
                    return False
    return True

def check_repetitions_column(sudoku):
    """Verify if there are repititions in the column of the sudoku"""
    column = []
    i = 0
    while i < 9:
        column = [value[i] for value in sudoku]
        for value in column:
            if value != "":
                if column.count(value) != 1:
                    return False
        column = []
        i += 1
    return True

def check_repetitions_block(sudoku):
    """Verify if there are repititions in each 3x3 block."""
    block = []
    i, j = (0, 3)
    x, y = (0, 3)
    for _ in range(9):
        for _ in range(3):
            for row in sudoku[x:y]:
                for value in row[i:j]:
                    block.append(value)
            for value in block:
                if value != "":
                    if block.count(value) != 1:
                        return False
            block = []
            i += 3
            j += 3
        i, j = (0, 3)
        x += 3
        y += 3
    return True

print(valid_sudoku(sudoku_1))

