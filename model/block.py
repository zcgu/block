import copy


"""
Block Pool structure:
block_pool[block_num][shape_num] = [[x,y]]
"""

block_pool = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]


def init_block_pool():
    block_pool[0].append([[0, -2], [0, -1], [0, 0], [0, 1], [0, 2]])
    block_pool[1].append([[0, -2], [0, -1], [0, 0], [1, 0], [1, 1]])
    block_pool[2].append([[0, 0], [1, 0], [2, 0], [0, 1], [0, 2]])
    block_pool[3].append([[-1, 0], [0, 0], [1, 0], [0, 1], [0, 2]])
    block_pool[4].append([[-1, -1], [0, -1], [0, 0], [0, 1], [-1, 1]])
    block_pool[5].append([[-1, -1], [0, -1], [0, 0], [0, 1], [0, 2]])
    block_pool[6].append([[0, -2], [0, -1], [0, 0], [1, 0], [0, 1]])
    block_pool[7].append([[-1, -1], [0, -1], [0, 0], [0, 1], [1, 1]])
    block_pool[8].append([[-1, -1], [-1, 0], [0, 0], [0, 1], [1, 1]])
    block_pool[9].append([[0, -1], [0, 0], [0, 1], [1, 0], [1, 1]])
    block_pool[10].append([[0, 0], [1, 0], [0, 1], [-1, 0], [0, -1]])
    block_pool[11].append([[-1, -1], [0, -1], [0, 0], [1, 0], [0, 1]])
    block_pool[12].append([[0, -1], [0, 0], [1, 0], [1, 1]])
    block_pool[13].append([[0, 0], [0, -1], [0, -2], [0, 1]])
    block_pool[14].append([[0, 0], [1, 0], [0, 1], [0, 2]])
    block_pool[15].append([[0, 0], [1, 0], [0, 1], [1, 1]])
    block_pool[16].append([[0, -1], [0, 0], [0, 1], [1, 0]])
    block_pool[17].append([[0, -1], [0, 0], [0, 1]])
    block_pool[18].append([[0, 0], [1, 0], [0, 1]])
    block_pool[19].append([[0, 0], [0, 1]])
    block_pool[20].append([[0, 0]])

    for block_num in range(0, len(block_pool)):
        block = block_pool[block_num]
        block.append(top_turn(block[0]))
        block.append(left_turn(block[0]))
        block.append(left_turn(top_turn(block[0])))
        block.append(rotate(block[0]))
        block.append(rotate(rotate(block[0])))
        block.append(rotate(rotate(rotate(block[0]))))
        block.append(rotate(block[1]))
        block.append(rotate(rotate(block[1])))
        block.append(rotate(rotate(rotate(block[1]))))
        block.append(rotate(block[2]))
        block.append(rotate(rotate(block[2])))
        block.append(rotate(rotate(rotate(block[2]))))
        block.append(rotate(block[3]))
        block.append(rotate(rotate(block[3])))
        block.append(rotate(rotate(rotate(block[3]))))

        for shape_num in range(0, len(block)):
            block[shape_num] = sort_shape(block[shape_num])

        new_block = []
        for shape in block:
            flag = True
            for new_shape in offset_shape(shape):
                if new_shape in new_block:
                    flag = False
                    break
            if flag:
                new_block.append(shape)
        block_pool[block_num] = new_block

def in_range(board, block_num, shape_num, p):


def sort_shape(shape):
    return sorted(shape, key=lambda point: point[0] * 100 + point[1])


def rotate(shape):
    shape = copy.deepcopy(shape)
    for point in shape:
        if point[0] * point[1] != 0:
            point[0], point[1] = point[1], point[0]
            point[0] = -point[0]
        elif point[1] == 0:
            point[1] = point[0]
            point[0] = 0
        elif point[0] == 0:
            point[0] = -point[1]
            point[1] = 0
    return shape


def top_turn(shape):
    shape = copy.deepcopy(shape)
    for point in shape:
        point[1] = -point[1]
    return shape


def left_turn(shape):
    shape = copy.deepcopy(shape)
    for point in shape:
        point[0] = -point[0]
    return shape


def offset_shape(shape):
    shapes = []
    for x in range(-5, 6):
        for y in range(-5, 6):
            new_shape = copy.deepcopy(shape)
            for point in new_shape:
                point[0] += x
                point[1] += y
            shapes.append(new_shape)
    return shapes
