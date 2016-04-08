from point_class import *
from block_class import *


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
