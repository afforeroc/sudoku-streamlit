"""
This web app show a sudoku using Streamlit
Author: Andres Felipe Forero Correa
Date: 2023-05-03
"""

import streamlit as st
import pandas as pd
from helpers import create_complete_sudoku,\
    create_sudoku_to_solve


if __name__ == "__main__":
    # Constants
    N_ROWS = 3
    N_COLS = 3
    # Create the complete sudoku and the sudoku to solve
    if "complete_sudoku" not in st.session_state:
        st.session_state["complete_sudoku"] = create_complete_sudoku()
    complete_sudoku = st.session_state["complete_sudoku"]
    if "sudoku_to_solve" not in st.session_state:
        st.session_state["sudoku_to_solve"] = create_sudoku_to_solve(
            complete_sudoku)
    sudoku_to_solve = st.session_state["sudoku_to_solve"]
    rows = [f"row {i}" for i in range(1, 10)]
    cols = [f"col {i}" for i in range(1, 10)]
    complete_sudoku_df = pd.DataFrame(complete_sudoku,
                                      index=rows, columns=cols)
    sudoku_to_solve_df = pd.DataFrame(sudoku_to_solve,
                                      index=rows, columns=cols)
    # Display the sudoku to solve
    st.markdown("<h1 style='text-align: center;'>Sudoku to solve</h1>",
                unsafe_allow_html=True)
    rows = [st.container() for _ in range(N_ROWS)]
    cols_per_row = [r.columns(N_COLS) for r in rows]
    cols = [column for row in cols_per_row for column in row]
    for big_i in range(3):
        for big_j in range(3):
            box_number = 3 * big_i + big_j
            cols[box_number].dataframe(
                sudoku_to_solve_df.iloc[3 * big_i:3 * big_i + 3,
                                        3 * big_j:3 * big_j + 3])
    # Display the complete sudoku
    if st.button('Show the solution'):
        st.markdown("<h1 style='text-align: center;'>Complete sudoku</h1>",
                    unsafe_allow_html=True)
        rows_s = [st.container() for _ in range(N_ROWS)]
        cols_per_row_s = [r.columns(N_COLS) for r in rows_s]
        cols_s = [column for row in cols_per_row_s for column in row]
        for big_i in range(3):
            for big_j in range(3):
                box_number = 3 * big_i + big_j
                cols_s[box_number].dataframe(
                    complete_sudoku_df.iloc[3 * big_i:3 * big_i + 3,
                                            3 * big_j:3 * big_j + 3])
