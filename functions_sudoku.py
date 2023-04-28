"""
This module provides utility functions for working with sudokus
Author: Andres Felipe Forero Correa
Date: 2023-04-28
"""

import random
import time

def generate_a_empty_sudoku():
    """It generates a empyt sudoku with zeros."""
    sudoku = []
    for _ in range(9):
        sudoku.append(9 * [0])
    return sudoku


def print_sudoku(sudoku):
    """It prints a nice sudoku showing the boxes."""
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


def random_bag_of_numers():
    """It returns a randomized list of numbers from 1 to 9."""
    random_bag = [x for x in range(1, 9 + 1)]
    random.shuffle(random_bag)
    return random_bag


def put_one_number_in_sudoku(sudoku, number):
    """It tries to put one number into each box of the sudoku in randomly form.
        If it cant do it, the function stops and returns."""
    sudoku_copy = sudoku.copy()
    rows = []
    cols = []
    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            #print(f"i = {i}, j = {j}")
            counter_for_exit = 0
            while(True) :
                random_row = random.randint(row, row + 2)
                random_col = random.randint(col, col + 2)
                #print(f"randi = {randi}, randj = {randj}")
                if random_row not in rows and random_col not in cols and sudoku_copy[random_row][random_col] == 0:
                    break
                counter_for_exit += 1
                if (counter_for_exit >= 25):
                    return False
            sudoku_copy[random_row][random_col] = number
            rows.append(random_row)
            cols.append(random_col)
            #print_sudoku(sudoku_copy)
            #time.sleep(0.005)
    return sudoku_copy


def generate_a_random_sudoku_v1(sudoku):
    """Generate a random sudoku putting one number distribuing by boxes."""
    random_bag = random_bag_of_numers()
    for k in range(9):
        number = random_bag[k]
        sudoku = put_one_number_in_sudoku(sudoku, number)
        if (sudoku == False):
            return False
    return sudoku


def check_a_group_of_numbers(group_of_numbers):
    """It check that a group of numbers don't have repeated values and the values are the numbers in range(1, 10)."""
    if len(group_of_numbers) != len(set(group_of_numbers)) or set(group_of_numbers) != {1, 2, 3, 4, 5, 6, 7, 8, 9}:
        return False
    return True


def check_sudoku(sudoku):
    """It validates that a sudoku is valid."""
    # Check rows
    for i in range(9):
        row = sudoku[i]
        if not check_a_group_of_numbers(row):
            return False
    # Check columns
    for j in range(9):
        col = [row[j] for row in sudoku]
        if not check_a_group_of_numbers(col):
            return False
    # Check boxes
    for big_j in range(3):
        for big_i in range(3):
            box = []
            for i in range(3):
                mini_row = sudoku[3 * big_i + i][3 * big_j : 3 * big_j + 3]
                box = box + mini_row
            if not check_a_group_of_numbers(box):
                return False
    # If all is good!
    return True


def create_a_sudoku():
    while(True):
        sudoku = generate_a_empty_sudoku()
        sudoku = generate_a_random_sudoku_v1(sudoku)
        if (sudoku != False):
            return sudoku


def get_a_valid_sudoku():
    """It returns a valid sudoku that is not generated randomly form."""
    valid_sudoku = [
        [5, 4, 7, 6, 8, 2, 9, 1, 3],   
        [6, 8, 3, 1, 9, 4, 7, 2, 5],   
        [9, 2, 1, 5, 7, 3, 8, 4, 6],
        [4, 3, 5, 2, 1, 9, 6, 7, 8],
        [2, 7, 8, 3, 6, 5, 1, 9, 4],
        [1, 6, 9, 8, 4, 7, 3, 5, 2],
        [7, 1, 6, 4, 2, 8, 5, 3, 9],
        [8, 5, 2, 9, 3, 1, 4, 6, 7],
        [3, 9, 4, 7, 5, 6, 2, 8, 1]
        ]
    return valid_sudoku


def get_a_no_valid_sudoku():
    """It returns a valid sudoku that is not generated randomly form."""
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