from Tkinter import *
from model import *
import time

import model

from board_ui import BoardUI


class UIController:
    def __init__(self, board, search_algo, value_func):
        self.board = board
        self.search_algo = search_algo
        self.value_func = value_func

        self.root = Tk()
        self.app = BoardUI(self.board, master=self.root)
        self.root.bind('<Up>', self.key_up)
        self.root.bind('<Down>', self.key_down)
        self.root.bind('<Left>', self.key_left)
        self.root.bind('<Right>', self.key_right)
        self.root.bind('<Return>', self.key_enter)
        self.root.bind('<space>', self.key_space)
        self.root.bind('<Tab>', self.key_tab)

        self.block_num = 0
        self.shape_num = 0
        self.p = [BOARD_LEN / 2, BOARD_LEN / 2]

    def start_ui(self):
        self.app.mainloop()
        try:
            self.root.destroy()
        finally:
            return

    def key_up(self, event):
        if in_range(self.board, self.block_num, self.shape_num, (self.p[0], self.p[1]+1)):
            self.p[1] += 1
            self.app.redraw_current_block_on_point(self.block_num, self.shape_num, self.p)

    def key_left(self, event):
        if in_range(self.board, self.block_num, self.shape_num, (self.p[0]-1, self.p[1])):
            self.p[0] -= 1
            self.app.redraw_current_block_on_point(self.block_num, self.shape_num, self.p)

    def key_right(self, event):
        if in_range(self.board, self.block_num, self.shape_num, (self.p[0]+1, self.p[1])):
            self.p[0] += 1
            self.app.redraw_current_block_on_point(self.block_num, self.shape_num, self.p)

    def key_down(self, event):
        if in_range(self.board, self.block_num, self.shape_num, (self.p[0], self.p[1]-1)):
            self.p[1] -= 1
            self.app.redraw_current_block_on_point(self.block_num, self.shape_num, self.p)

    def key_enter(self, event):
        if can_put_block(self.board, user1, self.block_num, self.shape_num, self.p):
            self.app.draw_block_on_point(self.block_num, self.shape_num, self.p, 'green', True)
            put_block(self.board, user1, self.block_num, self.shape_num, self.p)
            self.p = [BOARD_LEN / 2, BOARD_LEN / 2]
            self.block_num = self.board[user1][0]
            self.shape_num = 0
            self.app.redraw_current_block_on_point(self.block_num, self.shape_num, self.p)
            self.root.update_idletasks()
            self.computer_calculate()
            self.if_game_ends()

    def key_space(self, event):
        self.shape_num = (self.shape_num + 1) % len(block_pool[self.block_num])
        while not in_range(self.board, self.block_num, self.shape_num, self.p):
            if self.p[0] > BOARD_LEN / 2:
                self.p[0] -= 1
            else:
                self.p[0] += 1
            if self.p[1] > BOARD_LEN / 2:
                self.p[1] -= 1
            else:
                self.p[1] += 1
        self.app.redraw_current_block_on_point(self.block_num, self.shape_num, self.p)

    def key_tab(self, event):
        self.block_num = (self.block_num + 1) % 21
        while self.block_num not in self.board[user1]:
            self.block_num = (self.block_num + 1) % 21
        self.shape_num = 0
        while not in_range(self.board, self.block_num, self.shape_num, self.p):
            if self.p[0] > BOARD_LEN / 2:
                self.p[0] -= 1
            else:
                self.p[0] += 1
            if self.p[1] > BOARD_LEN / 2:
                self.p[1] -= 1
            else:
                self.p[1] += 1
        self.app.redraw_current_block_on_point(self.block_num, self.shape_num, self.p)

    def if_game_ends(self):
        if len(possible_puts(self.board, user1)) == 0 and \
                        len(possible_puts(self.board, user2)) == 0:
            print 'Game Ends'
            score1 = 0
            score2 = 0
            for x in range(0, BOARD_LEN):
                for y in range(0, BOARD_LEN):
                    if self.board[points][x][y] == user1:
                        score1 += 1
                    elif self.board[points][x][y] == user2:
                        score2 += 1
            print 'Score:', 'Player:', score1, 'Computer:', score2

    def computer_calculate(self):
        if len(possible_puts(self.board, user2)) == 0:
            print 'User 2 out of move'
            return
        move = self.search_algo(self.board, user2, self.value_func)
        self.app.draw_block_on_point(move[0], move[1], move[2], 'purple', True)
        put_block(self.board, user2, move[0], move[1], move[2])
