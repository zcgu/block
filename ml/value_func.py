from model import *


def opponent_corners(board, user):
    return len(find_corners(board, user)) - len(find_corners(board, user1 + user2 - user)) * 1000

