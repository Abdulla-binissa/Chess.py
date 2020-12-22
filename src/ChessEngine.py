



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
        self.whiteToMove = True
        self.moveLog = []