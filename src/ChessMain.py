



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
    validMoves = gs.getValidMoves()
    moveMade = False # Flag variable for when a move is made
    loadImages()
    
    sqSelected = () # (r, c) Last click of user
    playerClicks = [] # [(r, c), (r, c)] # Keeps track of player clicks

    running = True
    while running:
        for e in p.event.get():

            if e.type == p.QUIT:
                running = False

            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos() # (x, y) Location of mouse
                col = (location[0] // SQ_SIZE)
                row = (location[1] // SQ_SIZE)

                if sqSelected == (row, col): # Clicked same square twice
                    sqSelected = () # Unselect square
                    playerClicks = [] # Clear player clicks
                else:
                    sqSelected = (row, col)
                    playerClicks.append(sqSelected) # Appending both cliks

                if len(playerClicks) == 2: 
                    move = ChessEngine.Move(playerClicks[0], playerClicks[1], gs.board)
                    for i in range(len(validMoves)):
                        if move == validMoves[i]:
                            gs.makeMove(validMoves[i])
                            moveMade = True
                            sqSelected = () 
                            playerClicks = []
                    if not moveMade:
                        playerClicks = [sqSelected] 

            elif e.type == p.KEYDOWN:
                if e.key == p.K_z: # Undo move when 'z' is pressed
                    gs.undoMove()
                    moveMade = True
                    sqSelected = () 
                    playerClicks = []

        if moveMade:
            validMoves = gs.getValidMoves()
            moveMade = False

        drawGameState(screen, gs, validMoves, sqSelected)
        clock.tick(MAX_FPS)
        p.display.flip()

'''
Highlight square selected and moves for piece selected
'''
def highlightSquares(screen, gs, validMoves, sqSelected):
    if sqSelected != ():
        r, c = sqSelected
        if gs.board[r][c][0] == ('w' if gs.whiteToMove else 'b'):
            s = p.Surface((SQ_SIZE, SQ_SIZE))
            s.set_alpha(100) # 0 - transparent ; 255 - opaque
            s.fill(p.Color('blue'))
            screen.blit(s, (c*SQ_SIZE, r*SQ_SIZE))
            s.fill(p.Color('blue'))
            for move in validMoves:
                if move.startRow == r and move.startCol == c:
                    screen.blit(s, (SQ_SIZE * move.endCol, SQ_SIZE * move.endRow))


'''
Responsible for all graphics within a current game state
'''
def drawGameState(screen, gs, validMoves, sqSelected):
    drawBoard(screen) # Draw Board
    highlightSquares(screen, gs, validMoves, sqSelected) # Add in piece highlighting or move suggestions
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
