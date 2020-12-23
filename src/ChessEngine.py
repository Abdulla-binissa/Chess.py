



class GameState():

    def __init__(self):

        # Chess board is a 2d list of elements with 2 characters each
        # First character represents color 'b' or 'w'
        # Second character represents the type 'R', 'N', 'B', 'Q', 'K', 'P'
        # '--' represents empty space
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bP","bP","bP","bP","bP","bP","bP","bP"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wP","wP","wP","wP","wP","wP","wP","wP"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]

        self.moveFunctions = {'P': self.getPawnMoves, 'R': self.getRookMoves, 'N': self.getKnightMoves, 'B': self.getBishopMoves, 'Q': self.getQueenMoves, 'K': self.getKingMoves}

        self.whiteToMove = True
        self.moveLog = []

    '''
    Takes a Move as a parameter and exectues it (does not work fro castling, pawn promotion, and en-passant
    '''
    def makeMove(self, move):
        self.board[move.startRow][move.startCol] = "--"
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.moveLog.append(move) # Log move
        self.whiteToMove = not self.whiteToMove # Swap players

    '''
    Undo last move made
    '''
    def undoMove(self):
        if len(self.moveLog) != 0:
            move = self.moveLog.pop()
            self.board[move.startRow][move.startCol] = move.pieceMoved
            self.board[move.endRow][move.endCol] = move.pieceCaptured
            self.whiteToMove = not self.whiteToMove # Swap players

    '''
    All moves including checks
    '''
    def getValidMoves(self):
        return self.getAllPossibleMoves() #temp

    '''
    All moves not including checks
    '''
    def getAllPossibleMoves(self):
        moves = []        
        for r in range(len(self.board)):
            for c in range(len(self.board[r])):
                turn = self.board[r][c][0]
                if (turn == 'w' and self.whiteToMove) or (turn == 'b' and not self.whiteToMove):
                    piece = self.board[r][c][1]
                    self.moveFunctions[piece](r, c, moves)
        return moves
        

    '''
    Get all pawn moves for pawn at row, col
    '''
    def getPawnMoves(self, r, c, moves):
        if self.whiteToMove:
            if self.board[r-1][c] == "--":
                moves.append(Move((r, c), (r-1, c), self.board))
                if r == 6 and self.board[r-2][c] == "--":
                    moves.append(Move((r, c), (r-2, c), self.board))
            if c-1 >= 0: # Capture to left
                if self.board[r-1][c-1][0] == 'b':
                    moves.append(Move((r, c), (r-1, c-1), self.board))
            if c+1 <= 7: # Capture to right
                if self.board[r-1][c+1][0] == 'b':
                    moves.append(Move((r, c), (r-1, c+1), self.board))

        else:
            if self.board[r+1][c] == "--":
                moves.append(Move((r, c), (r+1, c), self.board))
                if r == 1 and self.board[r+2][c] == "--":
                    moves.append(Move((r, c), (r+2, c), self.board))
            if c-1 >= 0: # Capture to left
                if self.board[r+1][c-1][0] == 'b':
                    moves.append(Move((r, c), (r+1, c-1), self.board))
            if c+1 <= 7: # Capture to right
                if self.board[r+1][c+1][0] == 'b':
                    moves.append(Move((r, c), (r+1, c+1), self.board))


    '''
    Get all rook moves for pawn at row, col
    '''
    def getRookMoves(self, r, c, moves):
        pass
    
    '''
    Get all knight moves for pawn at row, col
    '''
    def getKnightMoves(self, r, c, moves):
        pass

    '''
    Get all bishop moves for pawn at row, col
    '''
    def getBishopMoves(self, r, c, moves):
        pass

    '''
    Get all queen moves for pawn at row, col
    '''
    def getQueenMoves(self, r, c, moves):
        pass

    '''
    Get all king moves for pawn at row, col
    '''
    def getKingMoves(self, r, c, moves):
        pass



class Move():
    # Maps keys to values
    # Key: value
    ranksToRows = {"1": 7, "2": 6, "3": 5, "4": 4, "5": 3, "6": 2, "7": 1, "8": 0}
    rowsToRanks = {v: k for k, v in ranksToRows.items()}
    filesToCols = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
    colsToFiles = {v: k for k, v in filesToCols.items()}

    def __init__(self, startSq, endSq, board):
        self.startRow = startSq[0]
        self.startCol = startSq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.endRow = endSq[0]
        self.endCol = endSq[1]
        self.pieceCaptured = board[self.endRow][self.endCol]
        self.moveID = self.startRow * 1000 + self.startCol * 100 + self.endRow * 10 + self.endCol


    '''
    Overriding the equals method
    '''
    def __eq__(self, other):
        if isinstance(other, Move):
            return self.moveID == other.moveID


    def getChessNotation(self): 
        return self.getRankFile(self.startRow, self.startCol) + self.getRankFile(self.endRow, self.endCol)

    def getRankFile(self, r, c):
        return self.colsToFiles[c] + self.rowsToRanks[r]


