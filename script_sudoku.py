from functions_sudoku import *

if __name__ == "__main__":
    # GENERATE SUDOKU
    sudoku = create_a_sudoku()
    #sudoku = get_a_valid_sudoku()
    # OUPUT
    print("------- SUDOKU ------")
    print_sudoku(sudoku)