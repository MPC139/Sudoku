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
    result_1 = check_size(sudoku)
    result_2 = check_numbers(sudoku)
    if result_1 and result_2:
        result = True
    else:
        result = False
    return result


def check_size(sudoku):
    """Verify if the sudoku is 9x9."""
    # First let's check if the sudoku has the appropriate number of rows.
    rows = len(sudoku)
    if rows == 9:
        result = True
    else:
        result = False
    # If the rows is correct, we check the columns
    if result == True:
        for row in sudoku:
            items = len(row)
            if items == 9:
                result = True
            else:
                result = False
                break
    return result


def check_numbers(sudoku):
    """Verify if the sudoku only has integers from 1 to 9."""
    result = True
    for row in sudoku:
        for value in row:
            if result == True:
                if value in range(1,10):
                    result = True
                elif value == "":
                    result = True
                else:
                    result = False
            else:
                break
    return result


print(valid_sudoku(sudoku_1))
