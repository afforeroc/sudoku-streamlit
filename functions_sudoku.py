import random

def gen_empty_sudoku():
    sudoku = []
    for _ in range(9):
        sudoku.append(9 * [0])
    return sudoku


def print_sudoku(sudoku):
    for i in range(9):
        line = ''
        for j in range(9):
            line += f"{sudoku[i][j]}" + ' '
            if (j + 1) % 3 == 0:
                line += 2 * ' '  
        print(line)
        if (i + 1) % 3 == 0:
            print()


def random_bag_of_numers():
    random_bag = [x for x in range(1, 9 + 1)]
    random.shuffle(random_bag)
    return random_bag


def put_one_number_in_sudoku(sudoku, number):
    copy_sudoku = sudoku.copy()
    randi, randj = None, None
    rows = []
    cols = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            counter_for_exit = 0
            #print(f"i = {i}, j = {j}")
            while(True) :
                randi = random.randint(i, i + 2)
                randj = random.randint(j, j + 2)
                #print(f"randi = {randi}, randj = {randj}")
                if randi not in rows and randj not in cols and copy_sudoku[randi][randj] == 0:
                    break
                counter_for_exit += 1
                if (counter_for_exit >= 25):
                    return False
            copy_sudoku[randi][randj] = number
            rows.append(randi)
            cols.append(randj)
    return copy_sudoku


def gen_random_sudoku_v1(sudoku):
    random_bag = random_bag_of_numers()
    for k in range(9):
        number = random_bag[k]
        sudoku = put_one_number_in_sudoku(sudoku, number)
        if (sudoku == False):
            return False
    return sudoku


def check_block_number(block_number):
    if len(block_number) != len(set(block_number)) or set(block_number)!= {1, 2, 3, 4, 5, 6, 7, 8, 9}:
        return False
    return True


def check_sudoku(sudoku):
    # Check rows
    for i in range(9):
        row = sudoku[i]
        if not check_block_number(row):
            return False
    # Check columns
    for j in range(9):
        col = [row[j] for row in sudoku]
        if not check_block_number(col):
            return False
    # Check boxes
    for big_j in range(3):
        for big_i in range(3):
            box = []
            for i in range(3):
                mini_row = sudoku[3 * big_i + i][3 * big_j : 3 * big_j + 3]
                box = box + mini_row
            if not check_block_number(box):
                return False
    # If all is good!
    return True


def create_a_sudoku():
    while(True):
        sudoku = gen_empty_sudoku()
        sudoku = gen_random_sudoku_v1(sudoku)
        if (sudoku != False):
            return sudoku


def get_fake_sudoku():
    fake = [
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
    return fake