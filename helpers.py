"""
This module provides utility functions for working with sudokus
Author: Andres Felipe Forero Correa
Date: 2023-04-28
"""

import random


def generate_a_empty_sudoku():
    """It generates a empyt sudoku with zeros"""
    sudoku = []
    for _ in range(9):
        sudoku.append(9 * [0])
    return sudoku


def put_one_number_across_all_boxes(sudoku, number):
    """It tries to put one number into each box of the sudoku with
        random row and random colum that are free (with value = 0).
        If it cant do it, the function stops and returns"""
    sudoku_copy = sudoku.copy()
    rows = []
    cols = []
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            # print(f"i = {i}, j = {j}")
            counter_for_exit = 0
            while True:
                random_row = random.randint(row, row + 2)
                random_col = random.randint(col, col + 2)
                # print(f"randi = {randi}, randj = {randj}")
                if random_row not in rows and\
                        random_col not in cols and\
                        sudoku_copy[random_row][random_col] == 0:
                    break
                counter_for_exit += 1
                if counter_for_exit >= 25:
                    return None, False
            sudoku_copy[random_row][random_col] = number
            rows.append(random_row)
            cols.append(random_col)
            # print_sudoku(sudoku_copy)
            # time.sleep(0.005)
    return sudoku_copy, True


def generate_random_sudoku(sudoku):
    """Generate a random sudoku putting random numbers across all the boxes"""
    random_bag = list(range(1, 9 + 1))
    random.shuffle(random_bag)
    for _ in range(9):
        number = random_bag.pop()
        sudoku, status = put_one_number_across_all_boxes(sudoku, number)
        if not status:
            return sudoku, False
    return sudoku, True


def create_empty_random_spaces(sudoku, mode="easy"):
    mode_spaces = {"easy": 81-38, "medium": 81-32, "hard": 81-25, "expert": 81-17}
    spaces = mode_spaces[mode]
    positions = set()
    while True:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        sudoku[row][col] = '-'
        positions.add((row, col))
        if len(positions) == spaces:
            break
    return sudoku


def create_sudoku_to_solve():
    """Create a sudoku using the core function generate a random sudoku"""
    while True:
        sudoku = generate_a_empty_sudoku()
        sudoku, status = generate_random_sudoku(sudoku)
        if status and check_sudoku(sudoku):
            sudoku = create_empty_random_spaces(sudoku, "expert")
            return sudoku


def check_group_of_numbers(group_of_numbers):
    """It check that a group of numbers don't have repeated values
        and the values are the numbers in range(1, 10)"""
    if len(group_of_numbers) != len(set(group_of_numbers)) or \
            set(group_of_numbers) != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
        return False
    return True


def check_sudoku(sudoku):
    """It validates that a sudoku is valid"""
    # Check rows
    for i in range(9):
        row = sudoku[i]
        if not check_group_of_numbers(row):
            print(f"Error in row {i + 1}: {row}", end='')
            return False
    # Check columns
    for j in range(9):
        col = [row[j] for row in sudoku]
        if not check_group_of_numbers(col):
            print(f"Error in column {j + 1}: {col}", end='')
            print()
            return False
    # Check boxes
    for big_j in range(3):
        for big_i in range(3):
            box = []
            for i in range(3):
                mini_row = sudoku[3 * big_i + i][3 * big_j: 3 * big_j + 3]
                box = box + mini_row
            if not check_group_of_numbers(box):
                box_num = 3 * big_i + big_j
                print(f"Error in box {box_num}: {box}")
                return False
    # If all is good!
    return True


def print_sudoku(sudoku):
    """It prints a nice sudoku showing the boxes"""
    print(21 * ">")
    for i in range(9):
        line = ''
        for j in range(9):
            line += f"{sudoku[i][j]}" + ' '
            if (j + 1) % 3 == 0:
                line += 2 * ' '
        print(line)
        if (i + 1) % 3 == 0 and i != 8:
            print()
        else:
            pass
    # Last line
    print(21 * "<")


def get_valid_sudoku():
    """It returns a valid sudoku"""
    valid_sudoku = [
        [1, 7, 5, 8, 4, 2, 6, 9, 3],
        [9, 2, 4, 1, 6, 3, 7, 5, 8],
        [8, 6, 3, 5, 9, 7, 2, 1, 4],
        [2, 1, 6, 4, 8, 5, 3, 7, 9],
        [4, 3, 7, 9, 2, 1, 8, 6, 5],
        [5, 9, 8, 7, 3, 6, 1, 4, 2],
        [6, 4, 1, 2, 5, 8, 9, 3, 7],
        [7, 8, 2, 3, 1, 9, 4, 5, 6],
        [3, 5, 9, 6, 7, 4, 1, 2, 8]
    ]
    return valid_sudoku


def get_not_valid_sudoku():
    """It returns a not valid sudoku"""
    no_valid_sudoku = [
        [5, 4, 7, 6, 8, 2, 9, 1, 3],
        [6, 8, 3, 1, 9, 4, 7, 2, 5],
        [9, 2, 0, 5, 7, 3, 8, 4, 6],
        [4, 3, 5, 2, 1, 9, 6, 7, 8],
        [2, 7, 8, 3, 6, 5, 1, 9, 4],
        [1, 6, 9, 8, 9, 7, 3, 5, 2],
        [7, 1, 6, 4, 2, 8, 5, 3, 9],
        [8, 5, 2, 9, 3, 1, 4, 6, 7],
        [3, 9, 4, 7, 5, 6, 2, 8, 1]
    ]
    return no_valid_sudoku
