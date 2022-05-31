#This class is responsible for storing information about the current gamestate.
#Also determines valid moves in current state.
#Reports a move log.
class GameState():
#alter this boardstate tracker to use numpi arrays for more efficient AI??
    def __init__(self):
        self.board = {
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"]
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"]
            ["--", "--", "--", "--", "--", "--", "--", "--"]
            ["--", "--", "--", "--", "--", "--", "--", "--"]
            ["--", "--", "--", "--", "--", "--", "--", "--"]
            ["--", "--", "--", "--", "--", "--", "--", "--"]
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"]
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
    self.whiteToMove = True
    self.moveLog = []
