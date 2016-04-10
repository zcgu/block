from model import *


def swap(a, b):
    c = a
    a = b
    b = c
    return a, b


class Point:
    """
    Point of board and block.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __hash__(self):
        return hash(self.x * 100 + self.y)

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def copy(self):
        return Point(self.x, self.y)

    def rotate_left_with_0_0_center(self):
        if self.x * self.y != 0:
            self.x, self.y = swap(self.x, self.y)
            self.x = -self.x
        elif self.y == 0:
            self.y = self.x
            self.x = 0
        elif self.x ==0:
            self.x = -self.y
            self.y = 0

    def rotate_right_with_0_0_center(self):
        self.rotate_left_with_0_0_center()
        self.rotate_left_with_0_0_center()
        self.rotate_left_with_0_0_center()

    def top_bottom_turn_with_0_0_center(self):
        self.y = -self.y

    def left_right_turn_with_0_0_center(self):
        self.x = -self.x

    def in_board_range(self, board):
        return 0 <= self.x < board.length and 0 <= self.y < board.length
