import unittest
import chess
import parse
import numpy as np

class TestParse(unittest.TestCase):

    # Not testing the whole one hot encoding since the vector is huge! Just doing some basic sanity checks
    def test_starting(self):
        board = chess.Board()
        # chess starting position
        board.set_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
        encoding = parse.parseBoard(board)
        self.assertEqual(8*8*12+1, len(encoding))
        # 32 pieces, plus whites turn
        self.assertEqual(33, np.count_nonzero(encoding))
    
    def test_other(self):
        board = chess.Board()
        # white: rook+king, black: king, move: black
        board.set_fen("8/8/3k3R/8/3K4/8/8/8 b - - 2 2")
        encoding = parse.parseBoard(board)
        self.assertEqual(8*8*12+1, len(encoding))
        self.assertEqual(3, np.count_nonzero(encoding))

if __name__ == '__main__':
    unittest.main()