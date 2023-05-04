"""
This web app show a sudoku using Streamlit
Author: Andres Felipe Forero Correa
Date: 2023-05-03
"""

import streamlit as st
import pandas as pd
from helpers import create_sudoku_to_solve


def light_gray_color(_):
    """It returns light gray for dataframe cells"""
    return 'background-color: #d3d3d3'


def color_sudoku(sudoku_df):
    """It colors the sudoku"""
    for big_i in range(3):
        for big_j in range(3):
            box_number = 3 * big_i + big_j
            if box_number % 2 == 0:
                rows = [f"row {ki}" for ki in range(3 * big_i + 1, 3 * big_i + 3 + 1)]
                cols = [f"col {kj}" for kj in range(3 * big_j + 1, 3 * big_j + 3 + 1)]
                st.text(rows)
                st.text(cols)
                sudoku_df.style.applymap(light_gray_color,
                                         subset=pd.IndexSlice[rows, cols])
                return sudoku_df


if __name__ == "__main__":
    # GENERATE SUDOKU
    # if "real_sudoku" not in st.session_state:
    #     st.session_state["real_sudoku"] = create_sudoku()
    # sudoku = st.session_state["real_sudoku"]
    rows = [f"row {i}" for i in range(1, 10)]
    cols = [f"col {i}" for i in range(1, 10)]
    sudoku = create_sudoku_to_solve()
    sudoku_df = pd.DataFrame(sudoku, index=rows, columns=cols)
    # OUTPUT SUDOKU AND PLAY (EDITING)
    st.markdown("<h1 style='text-align: center;'>Sudoku Streamlit</h1>",
                unsafe_allow_html=True)
    n_rows = 3
    n_cols = 3
    rows = [st.container() for _ in range(n_rows)]
    cols_per_row = [r.columns(n_cols) for r in rows]
    cols = [column for row in cols_per_row for column in row]
    #for image_index, cat_image in enumerate(cat_images):
    #    cols[image_index].image(cat_image)

    for big_i in range(3):
        for big_j in range(3):
            box_number = 3 * big_i + big_j
            cols[box_number].dataframe(sudoku_df.iloc[0:3, 0:3])
    """
    box1, box2, box3 = st.columns([1, 1, 1])
    with box1:
        st.markdown((sudoku_df.iloc[0:3, 0:3]).style.hide(axis="index").hide(axis="columns").to_html(), unsafe_allow_html=True)
        #st.experimental_data_editor(sudoku_df.iloc[0:3, 0:3])
    with box2:
        st.markdown((sudoku_df.iloc[0:3, 3:6]).style.hide(axis="index").hide(axis="columns").to_html(), unsafe_allow_html=True)
    with box3:
        st.markdown((sudoku_df.iloc[0:3, 6:9]).style.hide(axis="index").hide(axis="columns").to_html(), unsafe_allow_html=True)
    st.text("\n")
    st.text("\n")
    box4, box5, box6 = st.columns([1, 1, 1])
    with box4:
        st.markdown((sudoku_df.iloc[3:6, 0:3]).style.hide(axis="index").hide(axis="columns").to_html(), unsafe_allow_html=True)
    with box5:
        st.markdown((sudoku_df.iloc[3:6, 3:6]).style.hide(axis="index").hide(axis="columns").to_html(), unsafe_allow_html=True)
    with box6:
        st.markdown((sudoku_df.iloc[3:6, 6:9]).style.hide(axis="index").hide(axis="columns").to_html(), unsafe_allow_html=True)
    st.text("\n")
    st.text("\n")
    box7, box8, box9 = st.columns([1, 1, 1])
    with box7:
        st.markdown((sudoku_df.iloc[6:9, 0:3]).style.hide(axis="index").hide(axis="columns").to_html(), unsafe_allow_html=True)
    with box8:
        st.markdown((sudoku_df.iloc[6:9, 3:6]).style.hide(axis="index").hide(axis="columns").to_html(), unsafe_allow_html=True)
    with box9:
        st.markdown((sudoku_df.iloc[6:9, 6:9]).style.hide(axis="index").hide(axis="columns").to_html(), unsafe_allow_html=True)
    """
