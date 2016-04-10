from board_ui import BoardUI
from Tkinter import *
from model import *

class UIController:
    def __init__(self, board):
        self.root = Tk()
        self.app = BoardUI(board, master=self.root)
        self.root.bind('<Up>', self.key_up)
        self.root.bind('<Down>', self.key_down)
        self.root.bind('<Left>', self.key_left)
        self.root.bind('<Right>', self.key_right)

    def start_ui(self):
        self.app.mainloop()
        try:
            self.root.destroy()
        finally:
            return

    def key_up(self, event):
        self.app.draw_on_point(Point(1, 1), 'green', True)
        print 'up', event

    def key_left(self, event):
        print 'left', event

    def key_right(self, event):
        print 'right', event

    def key_down(self, event):
        self.app.draw_on_point(Point(13, 1), 'red', False)
        print 'down', event
