from Tkinter import *

BOARD_WIDTH = 500

BLOCK_POOL_WIDTH = BOARD_WIDTH
BLOCK_POOL_HEIGHT = 300


class BoardUI(Frame):
    def __init__(self, board, master=None):
        self.board = board

        Frame.__init__(self, master)
        self.pack()

        self.board_canvas = Canvas(self.master, width=BOARD_WIDTH, height=BOARD_WIDTH)
        self.board_canvas.pack()

        self.create_grid()

    def create_grid(self):
        border = 5.0
        line_width = 2.0

        board_length_point_number = self.board.length

        line_space = (BOARD_WIDTH - 2 * border) / board_length_point_number

        for x in range(0, board_length_point_number + 1):
            self.board_canvas.create_line(border + x * line_space, border,
                                          border + x * line_space, BOARD_WIDTH - border,
                                          fill="black", width=line_width)

        for y in range(0, board_length_point_number + 1):
            self.board_canvas.create_line(border, border + y * line_space,
                                          BOARD_WIDTH - border, border + y * line_space,
                                          fill="black", width=line_width)

