from model import *
from ml import *
from ui import *

init_block_pool()
board = init_board()
ui = UIController(board, two_level_search, opponent_corners)

ui.start_ui()
