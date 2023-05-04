"""
This script show sudoku functions in action
Author: Andres Felipe Forero Correa
Date: 2023-05-03
"""

from helpers import create_sudoku_to_solve, get_valid_sudoku,\
    get_not_valid_sudoku, print_sudoku, check_sudoku


if __name__ == "__main__":
    # GENERATE SUDOKU
    sudokus = {
        '1': create_sudoku_to_solve(),
        '2': get_valid_sudoku(),
        '3': get_not_valid_sudoku()
    }
    sudoku = sudokus['2']
    # OUPUT
    print("------- SUDOKU ------")
    print_sudoku(sudoku)
    if check_sudoku(sudoku):
        print("It is a valid sudoku!")
    else:
        print("It is not a valid sudoku!")
