import chess
import numpy as np

# Takes in a board, and returns a 8*8*12+1 encoded vector as a one hot encoding.
# Chess board is 8x8, there are 12 possible pieces, and the move is either white or black.
def parseBoard(board):
    encoding = np.zeros((64, 12))
    for square, piece in board.piece_map().items():
        encoding[square][piece.piece_type+(6*piece.color)-1] = 1
    encoding = np.reshape(encoding, 64*12)
    encoding = np.append(encoding, board.turn)
    return encoding
    