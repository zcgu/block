from Tkinter import *
from model import *
import copy

BOARD_WIDTH = 500

BLOCK_POOL_WIDTH = BOARD_WIDTH
BLOCK_POOL_HEIGHT = 300

border = 5.0
line_width = 2.0


class BoardUI(Frame):
    def __init__(self, board, master=None):
        self.board = board
        self.line_space = (BOARD_WIDTH - 2 * border) / BOARD_LEN

        Frame.__init__(self, master)
        self.pack()

        self.board_canvas = Canvas(self.master, width=BOARD_WIDTH, height=BOARD_WIDTH)
        self.board_canvas.pack()

        self.create_grid()
        self.draw_on_point([INIT_POINT, INIT_POINT], 'green', True)
        self.current_recs = None
        self.redraw_current_block_on_point(board[user1][0], 0, (BOARD_LEN / 2, BOARD_LEN / 2))

    def create_grid(self):
        board_length_point_number = BOARD_LEN

        for x in range(0, board_length_point_number + 1):
            self.board_canvas.create_line(border + x * self.line_space, border,
                                          border + x * self.line_space, BOARD_WIDTH - border,
                                          fill="black", width=line_width)

        for y in range(0, board_length_point_number + 1):
            self.board_canvas.create_line(border, border + y * self.line_space,
                                          BOARD_WIDTH - border, border + y * self.line_space,
                                          fill="black", width=line_width)

    def point_to_canvas_point(self, p):
        p = copy.deepcopy(p)
        p[1] = BOARD_LEN - 1 - p[1]

        x = p[0] * self.line_space + self.line_space / 2 + border
        y = p[1] * self.line_space + self.line_space / 2 + border

        return x, y

    def draw_on_point(self, point, color, solid):
        x, y = self.point_to_canvas_point(point)
        if solid:
            rec = self.board_canvas.create_rectangle(x - self.line_space / 2 + line_width / 2,
                                                     y - self.line_space / 2 + line_width / 2,
                                                     x + self.line_space / 2 - line_width / 2,
                                                     y + self.line_space / 2 - line_width / 2,
                                                     fill=color, width=0.0)
        else:
            rec = self.board_canvas.create_rectangle(x - self.line_space / 2 + line_width,
                                                     y - self.line_space / 2 + line_width,
                                                     x + self.line_space / 2 - line_width,
                                                     y + self.line_space / 2 - line_width,
                                                     outline=color, width=line_width)
        return rec

    def draw_block_on_point(self, block_num, shape_num, p, color, solid):
        recs = []
        for point in block_pool[block_num][shape_num]:
            recs.append(self.draw_on_point([p[0] + point[0], p[1] + point[1]], color, solid))
        return recs

    def redraw_current_block_on_point(self, block_num, shape_num, p, color='red', solid=False):
        if self.current_recs is not None:
            for rec in self.current_recs:
                self.board_canvas.delete(rec)
        self.current_recs = self.draw_block_on_point(block_num, shape_num, p, color, solid)
