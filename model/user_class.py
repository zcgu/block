from block_pool_class import *

player1 = 0
player2 = 1
player3 = 2
player4 = 3


def other_player(user):
    if user == player1:
        return player2
    else:
        return player1


class User:

    def __init__(self):
        self.block_pool = BlockPool()

    def copy(self):
        user_copy = User()
        user_copy.block_pool = self.block_pool.copy()
        return user_copy
