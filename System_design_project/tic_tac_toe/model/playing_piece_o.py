from model.playing_piece import PlayingPiece
from model.piece_type import PieceType

class PyaingPieceO(PlayingPiece):
    def __init__(self):
        super().__init__(PieceType.O.value)