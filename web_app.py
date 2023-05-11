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
    st.set_page_config(page_title="Sudoku Streamlit", page_icon="🎮")
    # Import styles
    with open('style.css', encoding="utf-8") as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    # Create the complete sudoku and the sudoku to solve
    if "complete_sudoku" not in st.session_state:
        st.session_state["complete_sudoku"] = create_complete_sudoku()
    complete_sudoku = st.session_state["complete_sudoku"]
    if "sudoku_to_solve" not in st.session_state:
        st.session_state["sudoku_to_solve"] = \
            create_sudoku_to_solve(complete_sudoku)
    sudoku_to_solve = st.session_state["sudoku_to_solve"]
    rows = [f"row {i}" for i in range(1, 10)]
    cols = [f"col {i}" for i in range(1, 10)]
    complete_sudoku_df = pd.DataFrame(complete_sudoku,
                                      index=rows, columns=cols)
    sudoku_to_solve_df = pd.DataFrame(sudoku_to_solve,
                                      index=rows, columns=cols)
    # Title of web app
    st.markdown("<h1 style='text-align: center;'>Sudoku Streamlit</h1>",
                unsafe_allow_html=True)
    # Create two columns for each sudoku
    col1, col2 = st.columns(2)
    with col1:
        # Display the sudoku to solve
        st.markdown(
            sudoku_to_solve_df.style.hide(axis="index")
            .hide(axis="columns").to_html(),
            unsafe_allow_html=True)
        # Aditional space
        st.write("")
        # Display the complete sudoku
        if st.button('Show the solution'):
            with col2:
                st.markdown(
                    complete_sudoku_df.style.hide(axis="index")
                    .hide(axis="columns").to_html(),
                    unsafe_allow_html=True)
                # Aditional space and caption
                st.write("")
                st.caption('Solution')
