# -*- coding: utf-8 -*-

"""
This script show sudoku functions in action
Author: Andres Felipe Forero Correa
Date: 2023-05-03
"""

from functions import create_complete_sudoku,\
    create_sudoku_to_solve, print_sudoku


if __name__ == "__main__":
    # GENERATE SUDOKU
    complete_sudoku = create_complete_sudoku()
    sudoku_to_solve = create_sudoku_to_solve(complete_sudoku)
    # OUPUT
    print("------- SUDOKU ------")
    print()
    print("1. Sudoku to solve")
    print_sudoku(sudoku_to_solve)
    print()
    print("2. Complete Sudoku")
    print_sudoku(complete_sudoku)
