from model import *
import copy


def one_level_search(board, user, value_func, return_list=False):
    que = []

    for move in possible_puts(board, user):
        board2 = copy.deepcopy(board)
        put_block(board2, user, move[0], move[1], move[2])
        que.append([board2, move])

    que = sorted(que, key=lambda state: value_func(state[0], user), reverse=True)

    if return_list:
        return que
    else:
        return que[0][1]
