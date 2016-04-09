from point_class import Point

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

    def __hash__(self):
        return hash(self.size)

    def __eq__(self, other):
        for block in other.all_possible_shapes_list():
            if self.is_same_shape(block):
                return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def copy(self):
        point_list_copy = []
        for point in self.point_list:
            point_list_copy.append(point.copy())
        return Block(point_list_copy)

    def rotate_left(self):
        for point in self.point_list:
            point.rotate_left_with_0_0_center()
        return self

    def rotate_right(self):
        for point in self.point_list:
            point.rotate_right_with_0_0_center()
        return self

    def top_bottom_turn(self):
        for point in self.point_list:
            point.top_bottom_turn_with_0_0_center()
        return self

    def left_right_turn(self):
        for point in self.point_list:
            point.left_right_turn_with_0_0_center()
        return self

    def sorted_point_list(self):
        return sorted(self.point_list, key=lambda point: point.x * 100 + point.y)

    def all_possible_shapes_list(self):
        block_list = [self.copy(),
                      self.copy().rotate_left(),
                      self.copy().rotate_left().rotate_left(),
                      self.copy().rotate_right(),
                      self.copy().top_bottom_turn(),
                      self.copy().top_bottom_turn().rotate_left(),
                      self.copy().top_bottom_turn().rotate_left().rotate_left(),
                      self.copy().top_bottom_turn().rotate_right(),
                      self.copy().left_right_turn(),
                      self.copy().left_right_turn().rotate_left(),
                      self.copy().left_right_turn().rotate_left().rotate_left(),
                      self.copy().left_right_turn().rotate_right(),
                      self.copy().top_bottom_turn().left_right_turn(),
                      self.copy().top_bottom_turn().left_right_turn().rotate_left(),
                      self.copy().top_bottom_turn().left_right_turn().rotate_left().rotate_left(),
                      self.copy().top_bottom_turn().left_right_turn().rotate_right()]

        return block_list

    def is_same_shape(self, other):
        return self.sorted_point_list() == other.sorted_point_list()

    def unique_possible_shapes_list(self):
        all_block_list = self.all_possible_shapes_list()
        unique_block_list = []
        for block in all_block_list:
            flag = True
            for unique_block in unique_block_list:
                if block.is_same_shape(unique_block):
                    flag = False
            if flag:
                unique_block_list.append(block)
        return unique_block_list
