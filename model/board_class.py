from model import *


class Board:

    def __init__(self, length):
        # Board length.
        self.length = length

        # Points List.
        self.point_list = []
        for x in range(0, length):
            for y in range(0, length):
                self.point_list.append(Point(x, y))

        # Points usage. None or user1, user2, etc.
        self.point_inuse_dic = {}
        for point in self.point_list:
            self.point_inuse_dic[point] = None

    def user_can_put_on_point(self, user, point):
        if not point.in_board_range(self):
            return False
        if not self.point_inuse_dic[point] is None:
            return False
        if (point + Point(1, 0)).in_board_range(self) and self.point_inuse_dic[point + Point(1, 0)] == user:
            return False
        if (point + Point(-1, 0)).in_board_range(self) and self.point_inuse_dic[point + Point(-1, 0)] == user:
            return False
        if (point + Point(0, 1)).in_board_range(self) and self.point_inuse_dic[point + Point(0, 1)] == user:
            return False
        if (point + Point(0, -1)).in_board_range(self) and self.point_inuse_dic[point + Point(0, -1)] == user:
            return False
        return True
