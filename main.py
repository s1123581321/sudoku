import copy

example_board = [
    [ 5, -1, -1,  6, -1,  7, -1,  9, -1],
    [ 1,  2,  6, -1, -1, -1, -1,  4, -1],
    [-1,  9, -1, -1, -1, -1,  6, -1, -1],
    [ 6, -1, -1, -1, -1, -1, -1,  2,  4],
    [ 9,  3,  1, -1,  7,  4, -1, -1, -1],
    [-1,  4,  5,  8,  3,  6, -1,  7,  9],
    [ 3,  5, -1,  7,  1, -1, -1,  6, -1],
    [-1, -1,  2, -1, -1,  3,  8,  1,  5],
    [-1, -1, -1, -1, -1,  2,  4, -1, -1]
    ]

def print_board(board):
    for row_idx in range(9):
        if 0 == row_idx%3:
            print("-------------")
        for col_idx in range(9):
            if col_idx in [0, 3, 6]:
                print("|", end="")
            if board[row_idx][col_idx] == -1:
                print(" ", end="")
            else:
                print(board[row_idx][col_idx], end="")
            if col_idx == 8:
                print("|")
        if row_idx == 8:
            print("-------------")

def simple_solve_board(board):
    solved = False
    board = copy.deepcopy(board)
    while(not solved):
        solved = True
        for row_idx in range(9):
            for col_idx in range(9):
                if board[row_idx][col_idx] == -1:
                    used_list = []
                    for x in range(9):
                        if x != col_idx:
                            if board[row_idx][x] != -1:
                                used_list.append(board[row_idx][x])
                        if x != row_idx:
                            if board[x][col_idx] != -1:
                                used_list.append(board[x][col_idx])
                    row_box = row_idx//3
                    col_box = col_idx//3
                    for x in range(3*row_box, 3+3*row_box):
                        for y in range(3*col_box, 3+3*col_box):
                            if [row_idx, col_idx] != [x, y]:
                                if board[x][y] != -1:
                                    used_list.append(board[x][y])
                    used_list = list(set(used_list))
                    possible_list = [x for x in range(1, 10) if not x in used_list]
                    if 1 == len(possible_list):
                        board[row_idx][col_idx] = possible_list[0]
                        solved = False
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
>>> print_board(simple_solve_board(example_board))
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
'''
