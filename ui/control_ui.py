from board_ui import BoardUI
from Tkinter import *
from model import *


class UIController:
    def __init__(self, board):
        self.board = board
        self.root = Tk()
        self.app = BoardUI(self.board, master=self.root)
        self.root.bind('<Up>', self.key_up)
        self.root.bind('<Down>', self.key_down)
        self.root.bind('<Left>', self.key_left)
        self.root.bind('<Right>', self.key_right)
        self.root.bind('<Return>', self.key_enter)
        self.root.bind('<End>', self.key_space)
        self.root.bind('<Tab>', self.key_tab)

        self.current_choose = 0
        self.current_transform = 0
        self.current_point = Point(self.board.length / 2, self.board.length / 2)

    def start_ui(self):
        self.app.mainloop()
        try:
            self.root.destroy()
        finally:
            return

    def current_block(self):
        return self.board.user1.block_pool.block_list[self.current_choose]\
            .unique_possible_shapes_list()[self.current_transform]

    def key_up(self, event):
        if self.current_block().in_board_range(self.board, self.current_point + Point(0, 1)):
            self.current_point += Point(0, 1)
            self.app.redraw_current_block_on_point(self.current_block(), self.current_point)

    def key_left(self, event):
        if self.current_block().in_board_range(self.board, self.current_point + Point(-1, 0)):
            self.current_point += Point(-1, 0)
            self.app.redraw_current_block_on_point(self.current_block(), self.current_point)

    def key_right(self, event):
        if self.current_block().in_board_range(self.board, self.current_point + Point(1, 0)):
            self.current_point += Point(1, 0)
            self.app.redraw_current_block_on_point(self.current_block(), self.current_point)

    def key_down(self, event):
        if self.current_block().in_board_range(self.board, self.current_point + Point(0, -1)):
            self.current_point += Point(0, -1)
            self.app.redraw_current_block_on_point(self.current_block(), self.current_point)

    def key_enter(self, event):
        if self.board.user_can_put_block_on_point(self.board.user1, self.current_block(), self.current_point):
            self.app.draw_block_on_point(self.current_block(), self.current_point, 'green', True)
            self.board.user_put_block_on_point(self.board.user1, self.current_block(), self.current_point)
            self.current_point = Point(self.board.length / 2, self.board.length / 2)
            self.current_choose = 0
            self.current_transform = 0
            self.app.redraw_current_block_on_point(self.current_block(), self.current_point)
            self.app.computer_calculate()
            self.if_game_ends()

    def key_space(self, event):
        self.current_transform = (self.current_transform + 1) % \
                                 len(self.board.user1.block_pool.block_list[self.current_choose].
                                     unique_possible_shapes_list())
        while not self.current_block().in_board_range(self.board, self.current_point):
            if self.current_point.x > self.board.length / 2:
                self.current_point.x -= 1
            else:
                self.current_point.x += 1
            if self.current_point.y > self.board.length / 2:
                self.current_point.y -= 1
            else:
                self.current_point.y += 1
        self.app.redraw_current_block_on_point(self.current_block(), self.current_point)

    def key_tab(self, event):
        self.current_choose = (self.current_choose + 1) % len(self.board.user1.block_pool.block_list)
        self.current_transform = 0
        while not self.current_block().in_board_range(self.board, self.current_point):
            if self.current_point.x > self.board.length / 2:
                self.current_point.x -= 1
            else:
                self.current_point.x += 1
            if self.current_point.y > self.board.length / 2:
                self.current_point.y -= 1
            else:
                self.current_point.y += 1
        self.app.redraw_current_block_on_point(self.current_block(), self.current_point)

    def if_game_ends(self):
        if len(self.board.user_possible_puts(self.board.user1)) == 0 and \
                        len(self.board.user_possible_puts(self.board.user2)) == 0:
            print 'Game Ends'
            score1 = 0
            score2 = 0
            for point in self.board.point_list:
                if self.board.point_inuse_dic[point] == self.board.user1:
                    score1 += 1
                elif self.board.point_inuse_dic[point] == self.board.user2:
                    score2 += 1
            print 'Score:', 'Player:', score1, 'Computer:', score2