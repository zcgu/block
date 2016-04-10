
def corner_different_value_function(board):
    return len(board.find_user_corners(board.user2)) - len(board.find_user_corners(board.user1))


class ValueFunction:
    # corner_difference = corner_different_value_function
    def __init__(self):
        self.corener_difference = corner_different_value_function
