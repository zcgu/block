from model import *


def corner_different(board, user):
    if user == player1:
        user_o = player2
    else:
        user_o = player1
    return len(board.find_user_corners(user)) - len(board.find_user_corners(user_o))


def oppenent_corners(board, user):
    if user == player1:
        user_o = player2
    else:
        user_o = player1
    return -len(board.find_user_corners(user_o)) * 1000 + len(board.find_user_corners(user))


class ValueFunction:
    # corner_difference = corner_different_value_function
    def __init__(self):
        self.corener_difference = corner_different
        self.oppenent_corners = oppenent_corners
