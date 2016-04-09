from point_class import Point


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

    def is_user_corner(self, user, point):
        if not point.in_board_range(self):
            return False
        if not self.user_can_put_on_point(user, point):
            return False
        if (point + Point(1, 1)).in_board_range(self) and self.point_inuse_dic[point + Point(1, 1)] == user:
            return True
        if (point + Point(-1, 1)).in_board_range(self) and self.point_inuse_dic[point + Point(-1, 1)] == user:
            return True
        if (point + Point(1, -1)).in_board_range(self) and self.point_inuse_dic[point + Point(-1, 1)] == user:
            return True
        if (point + Point(-1, -1)).in_board_range(self) and self.point_inuse_dic[point + Point(-1, -1)] == user:
            return True
        return False

    def find_user_corners(self, user):
        corner_point_list = []
        for point in self.point_list:
            if self.is_user_corner(user, point):
                corner_point_list.append(point)
        return corner_point_list

    def user_can_put_block_on_point(self, user, block, point):
        for block_point in block.point_list:
            if not self.user_can_put_on_point(user, block_point + point):
                return False
        for block_point in block.point_list:
            if self.is_user_corner(user, block_point + point):
                return True
        return False

    def user_put_block_on_point(self, user, block, point):
        for block_point in block.point_list:
            self.point_inuse_dic[block_point + point] = user
        user.block_pool.block_list.remove(block)

