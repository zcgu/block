from model import *


def corner_different(board, user):
    return len(find_corners(board, user)) - len(find_corners(board, user1 + user2 - user))


def oppenent_corners(board, user):
    return len(find_corners(board, user)) - len(find_corners(board, user1 + user2 - user)) * 1000

