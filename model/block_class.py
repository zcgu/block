from point_class import *


class Block:
    """
    One block.

    """
    def __init__(self, point_list):
        self.point_list = point_list
        self.size = len(point_list)

    def __str__(self):
        string = ''
        for y in [2, 1, 0, -1, -2]:
            for x in [-2, -1, 0, 1, 2]:
                if Point(x, y) in self.point_list:
                    string += '[]'
                else:
                    string += '  '
            string += '\n'
        return string

    def rotate_left(self):
        for point in self.point_list:
            point.rotate_left_with_0_0_center()

    def rotate_right(self):
        for point in self.point_list:
            point.rotate_right_with_0_0_center()

    def top_bottom_turn(self):
        for point in self.point_list:
            point.top_bottom_turn_with_0_0_center()

    def left_right_turn(self):
        for point in self.point_list:
            point.left_right_turn_with_0_0_center()
