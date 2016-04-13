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


def two_level_search(board, user, value_func):
    que1 = one_level_search(board, user, value_func, True)
    que1 = que1[:min(10, len(que1))]
    for state in que1:
        que2 = one_level_search(board, user1 + user2 - user, value_func, True)
        state.append(value_func(que2[0][0], user1 + user2 - user))
    que1 = sorted(que1, key=lambda states: states[2])
    return que1[0][1]
