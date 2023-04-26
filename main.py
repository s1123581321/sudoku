import copy

example_board = [
    [5, 0, 0, 6, 0, 7, 0, 9, 0],
    [1, 2, 6, 0, 0, 0, 0, 4, 0],
    [0, 9, 0, 0, 0, 0, 6, 0, 0],
    [6, 0, 0, 0, 0, 0, 0, 2, 4],
    [9, 3, 1, 0, 7, 4, 0, 0, 0],
    [0, 4, 5, 8, 3, 6, 0, 7, 9],
    [3, 5, 0, 7, 1, 0, 0, 6, 0],
    [0, 0, 2, 0, 0, 3, 8, 1, 5],
    [0, 0, 0, 0, 0, 2, 4, 0, 0]
    ]

example_board_2 = [
    [0, 7, 0, 9, 0, 0, 0, 4, 5],
    [0, 0, 0, 0, 0, 5, 7, 0, 0],
    [2, 0, 6, 4, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 9, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 6, 0, 7],
    [4, 0, 0, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 7, 0, 0, 1, 6, 0],
    [1, 3, 2, 6, 0, 0, 0, 0, 9],
    [0, 0, 0, 2, 9, 1, 0, 3, 0]
    ]

def print_board(board):
    for row_idx in range(9):
        if0 == row_idx%3:
            print("-------------")
        for col_idx in range(9):
            if col_idx in [0, 3, 6]:
                print("|", end="")
            if board[row_idx][col_idx] == 0:
                print(" ", end="")
            else:
                print(board[row_idx][col_idx], end="")
            if col_idx == 8:
                print("|")
        if row_idx == 8:
            print("-------------")

def simple_solve(board):
    exit_loop = False
    board = copy.deepcopy(board)
    while(not exit_loop):
        exit_loop = True
        for row_idx in range(9):
            for col_idx in range(9):
                used_list = []
                for x in range(9):
                    if x != col_idx:
                        if board[row_idx][x] != 0:
                            used_list.append(board[row_idx][x])
                    if x != row_idx:
                        if board[x][col_idx] != 0:
                            used_list.append(board[x][col_idx])
                row_box = row_idx//3
                col_box = col_idx//3
                for x in range(3*row_box, 3+3*row_box):
                    for y in range(3*col_box, 3+3*col_box):
                        if [row_idx, col_idx] != [x, y]:
                            if board[x][y] != 0:
                                used_list.append(board[x][y])
                used_list = list(set(used_list))
                if board[row_idx][col_idx] == 0:
                    possible_list = [x for x in range(1, 10) if not x in used_list]
                    if 1 == len(possible_list):
                        board[row_idx][col_idx] = possible_list[0]
                        exit_loop = False
                    if 0 == len(possible_list):
                        exit_loop = True
                elif board[row_idx][col_idx] in used_list:
                    exit_loop = True
    return board


def check_solved(board):
    return not True in [0 in x for x in board]


def unfilled_coords_list(board):
    return [[row, col] for row in range(9) for col in range(9) if 0 == board[row][col]]

#Takes too long
def hard_solve(board):
    solved = False
    board = simple_solve(board)
    original_board = copy.deepcopy(board)
    coord_list = unfilled_coords_list(board)
    blank_list_len = len(coord_list)
    loop_idx = 0
    while not solved:
        board = copy.deepcopy(original_board)
        value_list = [int(x) for x in str(loop_idx + 1).rjust(blank_list_len, '0')]
        #Make change to only run if value_list is valid
        loop_idx += 1
        for x in range(blank_list_len):
            board[coord_list[x][0]][coord_list[x][1]] = value_list[x]
        board = simple_solve(board)
        if 0 == loop_idx%1000:
            print_board(board)
        solved = check_solved(board)
    return board


'''
>>> print_board(example_board)
-------------
|5  |6 7| 9 |
|126|   | 4 |
| 9 |   |6  |
-------------
|6  |   | 24|
|931| 74|   |
| 45|836| 79|
-------------
|35 |71 | 6 |
|  2|  3|815|
|   |  2|4  |
-------------
>>> print_board(simple_solve(example_board))
-------------
|583|647|291|
|126|985|743|
|497|321|658|
-------------
|678|159|324|
|931|274|586|
|245|836|179|
-------------
|354|718|962|
|762|493|815|
|819|562|437|
-------------
>>> r = hard_solve(example_board)
>>> print_board(r)
-------------
|583|647|291|
|126|985|743|
|497|321|658|
-------------
|678|159|324|
|931|274|586|
|245|836|179|
-------------
|354|718|962|
|762|493|815|
|819|562|437|
-------------
>>> r == simple_solve(example_board)
True





>>> print_board(example_board_2)
-------------
| 7 |9  | 45|
|   |  5|7  |
|2 6|4  |8  |
-------------
|   |  9|   |
| 1 |   |6 7|
|4  |5  | 1 |
-------------
| 9 |7  |16 |
|132|6  |  9|
|   |291| 3 |
-------------
Not solved by simple_solve
>>> print_board(simple_solve(example_board_2))
-------------
|871|9  |345|
| 4 |  5|726|
|256|4  |891|
-------------
|   |  9|   |
| 1 |   |6 7|
|4  |5  | 1 |
-------------
|59 |7  |16 |
|132|6  |  9|
|   |291| 3 |
-------------
Need alternative method
>>> print_board(hard_solve(example_board_2))
-------------
|871|962|345|
|349|815|726|
|256|437|891|
-------------
|683|179|254|
|915|324|687|
|427|586|913|
-------------
|598|743|162|
|132|658|479|
|764|291|538|
-------------

'''
