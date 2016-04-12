import block as block_class

"""
Board Structure:
board[points][x][y] = None / user1 / user2
board[user1 / user2] = [block_num]
"""

points = 0
user1 = 1
user2 = 2

BOARD_LEN = 14
INIT_POINT = 4


def init_board():
    board = [[], [], []]

    for x in range(0, BOARD_LEN):
        board[points].append([])
        for y in range(0, BOARD_LEN):
            board[points][x].append(None)

    for block_num in range(0, 21):
        board[user1].append(block_num)
        board[user2].append(block_num)

    return board


def put_block(board, user, block_num, shape_num, p):
    for point in block_class.block_pool[block_num][shape_num]:
        board[points][point[0]+p[0]][point[1]+p[1]] = user
    board[user].remove(block_num)


def in_range(point):
    return 0 <= point[0] < BOARD_LEN and 0 <= point[1] < BOARD_LEN


def can_put(board, user, p):
    if not in_range(p):
        return False
    if board[points][p[0]][p[1]] is not None:
        return False
    if in_range((p[0] + 1, p[1])) and board[points][p[0] + 1][p[1]] == user:
        return False
    if in_range((p[0] - 1, p[1])) and board[points][p[0] - 1][p[1]] == user:
        return False
    if in_range((p[0], p[1] + 1)) and board[points][p[0]][p[1] + 1] == user:
        return False
    if in_range((p[0], p[1] - 1)) and board[points][p[0]][p[1] - 1] == user:
        return False
    return True


def is_corner(board, user, p):
    if not in_range(p) or not can_put(board, user, p):
        return False
    if (p[0] == INIT_POINT and p[1] == INIT_POINT and user == user1) or \
            (p[0] == BOARD_LEN - INIT_POINT - 1 and p[1] == BOARD_LEN - INIT_POINT - 1 and user == user2):
        return True
    if in_range((p[0] + 1, p[1] + 1)) and board[points][p[0] + 1][p[1] + 1] == user:
        return True
    if in_range((p[0] + 1, p[1] - 1)) and board[points][p[0] + 1][p[1] - 1] == user:
        return True
    if in_range((p[0] - 1, p[1] + 1)) and board[points][p[0] - 1][p[1] + 1] == user:
        return True
    if in_range((p[0] - 1, p[1] - 1)) and board[points][p[0] - 1][p[1] - 1] == user:
        return True
    return False


def find_corners(board, user):
    corner_list = []
    for x in range(0, BOARD_LEN):
        for y in range(0, BOARD_LEN):
            if is_corner(board, user, (x, y)):
                corner_list.append((x, y))
    return corner_list


def can_put_block(board, user, block_num, shape_num, p):
    block = block_class.block_pool[block_num][shape_num]
    contains_corner = False
    for point in block:
        if not can_put(board, user, (point[0]+p[0], point[1]+p[1])):
            return False
        if is_corner(board, user, (point[0]+p[0], point[1]+p[1])):
            contains_corner = True
    if contains_corner:
        return True
    else:
        return False


def possible_puts(board, user):
    block_shape_p_list = []
    for p in find_corners(board, user):
        for block_num in board[user]:
            for shape_num in range(0, len(block_class.block_pool[block_num])):
                for point in block_class.block_pool[block_num][shape_num]:
                    if can_put_block(board, user, block_num, shape_num, (p[0]-point[0], p[1]-point[1])):
                        block_shape_p_list.append((block_num, shape_num, (p[0]-point[0], p[1]-point[1])))
    return block_shape_p_list
