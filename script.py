from functions_sudoku import *

if __name__ == "__main__":
    # GENERATE SUDOKU
    sudoku = create_a_sudoku()
    # OUPUT
    print("------- SUDOKU ------", end="\n\n")
    print_sudoku(sudoku)