import streamlit as st
import pandas as pd
import numpy as np
from functions_sudoku import *

if __name__ == "__main__":
    # GENERATE SUDOKU
    if "real_sudoku" not in st.session_state:
        st.session_state["real_sudoku"] = create_a_sudoku()
    sudoku = st.session_state["real_sudoku"]
    rows = [f"row {i}" for i in range(1, 10)]
    cols = [f"col {i}" for i in range(1, 10)]
    sudoku_df = pd.DataFrame(sudoku, index=rows, columns=cols)
    # OUTPUT SUDOKU AND PLAY (EDITING)
    st.markdown("<h1 style='text-align: center;'>Sudoku Streamlit</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 6, 1])
    with col2:
        edit_sudoku_df = st.experimental_data_editor(sudoku_df)