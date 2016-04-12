from block_class import Block
from point_class import Point


class BlockPool:
    """
    []
    []    []  []                    []  []                                             []
    []  [][]  []      []    [][]    []  [][]   [][]   [][]  [][]    []     []      []  []  []         []   []
    []  []    []      []      []    []  []     []   [][]    [][]  [][][]   [][]  [][]  []  []   [][]  [][] [] []   []
    []  []    [][]  [][][]  [][]  [][]  []   [][]   []      []      []   [][]    []    []  [][] [][]  []   [] [][] [] []
    """
    def __init__(self):
        self.block_list = []
        self.block_list.append(Block([Point(0, -2), Point(0, -1), Point(0, 0), Point(0, 1), Point(0, 2)]))
        self.block_list.append(Block([Point(0, -2), Point(0, -1), Point(0, 0), Point(1, 0), Point(1, 1)]))
        self.block_list.append(Block([Point(0, 0), Point(1, 0), Point(2, 0), Point(0, 1), Point(0, 2)]))
        self.block_list.append(Block([Point(-1, 0), Point(0, 0), Point(1, 0), Point(0, 1), Point(0, 2)]))
        self.block_list.append(Block([Point(-1, -1), Point(0, -1), Point(0, 0), Point(0, 1), Point(-1, 1)]))
        self.block_list.append(Block([Point(-1, -1), Point(0, -1), Point(0, 0), Point(0, 1), Point(0, 2)]))
        self.block_list.append(Block([Point(0, -2), Point(0, -1), Point(0, 0), Point(1, 0), Point(0, 1)]))
        self.block_list.append(Block([Point(-1, -1), Point(0, -1), Point(0, 0), Point(0, 1), Point(1, 1)]))
        self.block_list.append(Block([Point(-1, -1), Point(-1, 0), Point(0, 0), Point(0, 1), Point(1, 1)]))
        self.block_list.append(Block([Point(0, -1), Point(0, 0), Point(0, 1), Point(1, 0), Point(1, 1)]))
        self.block_list.append(Block([Point(0, 0), Point(1, 0), Point(0, 1), Point(-1, 0), Point(0, -1)]))
        self.block_list.append(Block([Point(-1, -1), Point(0, -1), Point(0, 0), Point(1, 0), Point(0, 1)]))
        self.block_list.append(Block([Point(0, -1), Point(0, 0), Point(1, 0), Point(1, 1)]))
        self.block_list.append(Block([Point(0, 0), Point(0, -1), Point(0, -2), Point(0, 1)]))
        self.block_list.append(Block([Point(0, 0), Point(1, 0), Point(0, 1), Point(0, 2)]))
        self.block_list.append(Block([Point(0, 0), Point(1, 0), Point(0, 1), Point(1, 1)]))
        self.block_list.append(Block([Point(0, -1), Point(0, 0), Point(0, 1), Point(1, 0)]))
        self.block_list.append(Block([Point(0, -1), Point(0, 0), Point(0, 1)]))
        self.block_list.append(Block([Point(0, 0), Point(1, 0), Point(0, 1)]))
        self.block_list.append(Block([Point(0, 0), Point(0, 1)]))
        self.block_list.append(Block([Point(0, 0)]))

    def copy(self):
        block_pool_copy = BlockPool()
        block_pool_copy.block_list = []
        for block in self.block_list:
            block_pool_copy.block_list.append(block.copy())
        return block_pool_copy