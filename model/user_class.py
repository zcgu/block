from block_pool_class import *


class User:

    def __init__(self):
        self.block_pool = BlockPool()

    def copy(self):
        user_copy = User()
        user_copy.block_pool = self.block_pool.copy()
        return user_copy
