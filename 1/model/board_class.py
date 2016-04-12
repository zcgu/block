from point_class import Point
from user_class import User, player1, player2, player3, player4

MODE_TWO_BOARD_LENGTH = 14
MODE_FOUR_BOARD_LENGTH = 20

MODE_TWO_INIT_POINT_X_AND_Y = 4
MODE_FOUR_INIT_POINT_X_AND_Y = 0


class Board:

    def __init__(self, user1, user2, user3=None, user4=None):
        if (user3 is None and user4 is not None) or (user3 is not None and user4 is None):
            print "Invalid init board: Player number is 3"
        # User list.
        self.users = [User(), User()]

        # Board length.
        if user3 is None:
            self.length = MODE_TWO_BOARD_LENGTH
        else:
            self.length = MODE_FOUR_BOARD_LENGTH

        # Points List.
        self.point_list = []
        for x in range(0, self.length):
            for y in range(0, self.length):
                self.point_list.append(Point(x, y))

        # Points usage. None or player1, player2, etc.
        self.point_inuse_dic = {}
        for point in self.point_list:
            self.point_inuse_dic[point] = None

        # Init point position.
        self.init_point_dic = {}
        if user3 is None:
            self.init_point_dic[player1] = Point(MODE_TWO_INIT_POINT_X_AND_Y,
                                               MODE_TWO_INIT_POINT_X_AND_Y)
            self.init_point_dic[player2] = Point(self.length - MODE_TWO_INIT_POINT_X_AND_Y,
                                               self.length - MODE_TWO_INIT_POINT_X_AND_Y)
        else:
            self.init_point_dic[player1] = Point(MODE_FOUR_INIT_POINT_X_AND_Y,
                                               MODE_FOUR_INIT_POINT_X_AND_Y)
            self.init_point_dic[player2] = Point(MODE_FOUR_INIT_POINT_X_AND_Y,
                                               self.length - MODE_FOUR_INIT_POINT_X_AND_Y)
            self.init_point_dic[player3] = Point(self.length - MODE_FOUR_INIT_POINT_X_AND_Y,
                                               self.length - MODE_FOUR_INIT_POINT_X_AND_Y)
            self.init_point_dic[player4] = Point(self.length - MODE_FOUR_INIT_POINT_X_AND_Y,
                                               MODE_FOUR_INIT_POINT_X_AND_Y)

    def copy(self):
        if len(self.users) == 2:
            board_copy = Board(self.users[player1].copy(), self.users[player2].copy())
        else:
            board_copy = Board(self.users[player1].copy(), self.users[player2].copy(),
                               self.users[player3].copy(), self.users[player4].copy())
        for point in self.point_inuse_dic:
            board_copy.point_inuse_dic[point] = self.point_inuse_dic[point]
        return board_copy

    def __str__(self):
        string = ''
        for y in range(self.length - 1, -1, -1):
            for x in range(0, self.length):
                if self.point_inuse_dic[Point(x, y)] is not None:
                    string += '[] '
                else:
                    string += '   '
            string += '\n'
        return string

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
        if point == self.init_point_dic[user]:
            return True
        if (point + Point(1, 1)).in_board_range(self) and self.point_inuse_dic[point + Point(1, 1)] == user:
            return True
        if (point + Point(-1, 1)).in_board_range(self) and self.point_inuse_dic[point + Point(-1, 1)] == user:
            return True
        if (point + Point(1, -1)).in_board_range(self) and self.point_inuse_dic[point + Point(1, -1)] == user:
            return True
        if (point + Point(-1, -1)).in_board_range(self) and self.point_inuse_dic[point + Point(-1, -1)] == user:
            return True
        return False

    def find_user_corners(self, user):
        corner_point_list = []
        for point in self.point_list:
            if self.is_user_corner(user, point) and point not in corner_point_list:
                corner_point_list.append(point)
        return corner_point_list

    def user_can_put_block_on_point(self, user, block, point):
        contains_corner = False
        for block_point in block.point_list:
            if not self.user_can_put_on_point(user, block_point + point):
                return False
            if self.is_user_corner(user, block_point + point):
                contains_corner = True
        if contains_corner:
            return True
        else:
            return False

    def user_put_block_on_point(self, user, block, point):
        for block_point in block.point_list:
            self.point_inuse_dic[block_point + point] = user
        self.users[user].block_pool.block_list.remove(block)

    def user_possible_block_puts_around_corner(self, user, block, corner_point):
        block_point_list = []
        for block_shape in block.unique_possible_shapes_list():
            for block_point in block_shape.point_list:
                if self.user_can_put_block_on_point(user, block_shape, corner_point - block_point):
                    block_point_list.append((block_shape, corner_point - block_point))
        return block_point_list

    def user_possible_puts_around_corner(self, user, corner_point):
        block_point_list = []
        for block in self.users[user].block_pool.block_list:
            for block_point in self.user_possible_block_puts_around_corner(user, block, corner_point):
                block_point_list.append(block_point)
        return block_point_list

    def user_possible_puts(self, user):
        block_point_list = []
        for corner_point in self.find_user_corners(user):
            for block_point in self.user_possible_puts_around_corner(user, corner_point):
                block_point_list.append(block_point)
        return block_point_list
