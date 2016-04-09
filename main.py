from model import *

user1 = User()
board = Board(19)

block = user1.block_pool.block_list[1]

block_copy = block.copy()
block_copy.rotate_left()

# print block
# print block_copy
#
# print block == block_copy
#
for block in block.unique_possible_shapes_list():
    print block

