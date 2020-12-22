



import pygame as p 
import ChessEngine

WIDTH = HEIGHT = 512 #400 is another option
DIMENSION = 8 # Chess board is 8x8
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15 # For animations later on
IMAGES = {}

'''
Initialize global directory of images
'''
def loadImages():
    pieces = ['wP', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bP', 'bR', 'bN', 'bB', 'bQ', 'bK']
    for piece in pieces:
        IMAGES[piece] = p.image.load("../images/regularSet/" + piece +".png")

'''
Main -- Handle user input and update graphics
'''
def main():
    p.init()
    screen = p.display.set_mode((WIDTH, HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    gs = ChessEngine.GameState()
    loadImages()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
        drawGameState(screen, gs)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Responsible for all graphics within a current game state
'''
def drawGameState(screen, gs):
    drawBoard(screen) # Draw Board
    # Add in piece highlighting or move suggestions
    drawPieces(screen, gs.board) # Draw Pieces


'''
Draw squares on the board
'''
def drawBoard(screen):
    colors = [p.Color("white"), p.Color("gray")]
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))
    

'''
Draw pieces on the board using current GameState.board
'''
def drawPieces(screen, board):
    for r in range(DIMENSION):
        for c in range(DIMENSION):
            piece = board[r][c]
            if piece != '--': # Not empty
                screen.blit(IMAGES[piece], p.Rect(c*SQ_SIZE, r*SQ_SIZE, SQ_SIZE, SQ_SIZE))


























'''
Run Main
'''
if __name__ == "__main__":
    main() 
