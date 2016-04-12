from model import *
from ui import *
from ml import *

board = Board(player1, player2)

ui_controller = UIController(board, two_level_search, ValueFunction().oppenent_corners)
ui_controller.start_ui()

