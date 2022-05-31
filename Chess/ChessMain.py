#This file handles user input and current game state object.

import pygame as p
from chessEngine import ChessEngine

WIDTH = HEIGHT = 512 #based on image files
DIMENSION = 8
SQ_SIZE = HEIGHT / DIMENSION
MAX_FPS = 24
IMAGES = {}

def loadImages():
    pieces = ["wp", "bp", "wR", "bR", "wN", "bN", "wB", "bB", "wQ", "bQ", "wK", "bK"]
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png") (SQ_SIZE, SQ_SIZE))
    #is accessible from IMAGES["*"]


#Main Driver handles inputs and realtime graphics
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("blue"))
    gs = ChessEngine.GameState()
    print(gs.board)

main()
