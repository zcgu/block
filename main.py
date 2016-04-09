from model import *
import random

user1 = User()
user2 = User()
board = Board(user1, user2)

while len(board.user_possible_puts(user1)) != 0:
    block_point = random.choice(board.user_possible_puts(user1))
    board.user_put_block_on_point(user1, block_point[0], block_point[1])
    print board