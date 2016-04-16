from model import *
import copy


def one_level_search(board, user, value_func, require_score=False):
    moves, scores = init(board, user)

    for move in moves:
        board2 = perform(board, user, move)
        scores[moves.index(move)] = value_func(board2, user)

    if require_score:
        return max(scores)

    return result(moves, scores)


def two_level_search(board, user, value_func):
    moves, scores = init(board, user)

    for move in moves:
        board2 = perform(board, user, move)
        scores[moves.index(move)] = -one_level_search(board2, other(user), value_func, True)

    return result(moves, scores)


def init(board, user):
    moves = possible_puts(board, user)
    scores = [float("-inf")] * len(moves)
    return moves, scores


def result(moves, scores):
    max_score = max(scores)
    return moves[scores.index(max_score)]


def perform(board, user, move):
    board2 = copy.deepcopy(board)
    put_block(board2, user, move[0], move[1], move[2])
    return board2


def other(user):
    return user1 + user2 - user
