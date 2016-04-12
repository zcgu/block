from model import *
from ml import *
from ui import *

init_block_pool()
board = init_board()
ui = UIController(board, one_level_search, oppenent_corners)

ui.start_ui()
