
def corner_different(board):
    return len(board.find_user_corners(board.user2)) - len(board.find_user_corners(board.user1))


def oppenent_corners(board):
    return -len(board.find_user_corners(board.user1)) * 1000 + len(board.find_user_corners(board.user2))


class ValueFunction:
    # corner_difference = corner_different_value_function
    def __init__(self):
        self.corener_difference = corner_different
        self.oppenent_corners = oppenent_corners