from one_level_search import one_level_search
from model import *

def two_level_search(board, user, value_func):
    que1 = one_level_search(board, user, value_func, True)
    que1 = que1[:min(5, len(que1))]
    for state in que1:
        que2 = one_level_search(board, other_player(user), value_func, True)
        state.append(value_func(que2[0][0], other_player(user)))
    que1 = sorted(que1, key=lambda move: move[2])
    return que1[0][1]
