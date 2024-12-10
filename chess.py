class ChessPiece:
    def __init__(self, color, type):
        self.color = color
        self.type = type

    def is_valid_move(self, start, end, board):
        raise NotImplementedError("This method should be overridden by subclasses")


class Pawn(ChessPiece):
    def __init__(self, color):
        super().__init__(color, 'P')
        self.has_moved = False  # Track whether the pawn has moved

    def is_valid_move(self, start, end, board):
        start_col, start_row = start
        end_col, end_row = end

        direction = -1 if self.color == 'W' else 1

        # Check one step forward
        if start_col == end_col and start_row + direction == end_row and board[end_row][end_col] is None:
            return True

        # Check two steps forward on first move (must also ensure no pieces are in between)
        if not self.has_moved and start_col == end_col and start_row + 2 * direction == end_row and board[end_row][end_col] is None:
            if board[start_row + direction][start_col] is None:  # Check if square in between is empty
                return True

        # Capture move (diagonal move)
        if abs(start_col - end_col) == 1 and start_row + direction == end_row and board[end_row][end_col] is not None:
            if board[end_row][end_col].color != self.color:
                return True

        return False

    def mark_as_moved(self):
        self.has_moved = True


class Knight(ChessPiece):
    def __init__(self, color):
        super().__init__(color, 'N')

    def is_valid_move(self, start, end, board):
        start_col, start_row = start
        end_col, end_row = end

        dx = abs(start_col - end_col)
        dy = abs(start_row - end_row)

        if (dx == 2 and dy == 1) or (dx == 1 and dy == 2):
            return True
        return False


class Rook(ChessPiece):
    def __init__(self, color):
        super().__init__(color, 'R')

    def is_valid_move(self, start, end, board):
        start_col, start_row = start
        end_col, end_row = end

        if start_col == end_col:
            # Vertical move
            step = 1 if end_row > start_row else -1
            for row in range(start_row + step, end_row, step):
                if board[row][start_col] is not None:
                    return False
            return True
        elif start_row == end_row:
            # Horizontal move
            step = 1 if end_col > start_col else -1
            for col in range(start_col + step, end_col, step):
                if board[start_row][col] is not None:
                    return False
            return True
        return False


class Bishop(ChessPiece):
    def __init__(self, color):
        super().__init__(color, 'B')

    def is_valid_move(self, start, end, board):
        start_col, start_row = start
        end_col, end_row = end

        if abs(start_col - end_col) != abs(start_row - end_row):
            return False

        step_col = 1 if end_col > start_col else -1
        step_row = 1 if end_row > start_row else -1

        col, row = start_col + step_col, start_row + step_row
        while col != end_col and row != end_row:
            if board[row][col] is not None:
                return False
            col += step_col
            row += step_row

        return True


class Queen(ChessPiece):
    def __init__(self, color):
        super().__init__(color, 'Q')

    def is_valid_move(self, start, end, board):
        rook = Rook(self.color)
        bishop = Bishop(self.color)

        return rook.is_valid_move(start, end, board) or bishop.is_valid_move(start, end, board)


class King(ChessPiece):
    def __init__(self, color):
        super().__init__(color, 'K')

    def is_valid_move(self, start, end, board):
        start_col, start_row = start
        end_col, end_row = end

        if max(abs(start_col - end_col), abs(start_row - end_row)) == 1:
            return True
        return False


class ChessBoard:
    def __init__(self):
        self.board = self.create_initial_board()
        self.turn = 'W'

    def create_initial_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]

        board[7] = [Rook('W'), Knight('W'), Bishop('W'), Queen('W'), King('W'), Bishop('W'), Knight('W'), Rook('W')]
        board[6] = [Pawn('W')] * 8

        board[0] = [Rook('B'), Knight('B'), Bishop('B'), Queen('B'), King('B'), Bishop('B'), Knight('B'), Rook('B')]
        board[1] = [Pawn('B')] * 8

        return board

    def print_board(self):
        for row in self.board:
            print(" ".join([str(piece.type + piece.color if piece else '--') for piece in row]))

    def move_piece(self, start, end):
        start_col, start_row = start
        end_col, end_row = end

        start_piece = self.board[start_row][start_col]
        if start_piece is None:
            print("Invalid Move")
            return False

        if start_piece.color != self.turn:
            print("Invalid Move")
            return False

        if start_piece.is_valid_move(start, end, self.board):
            target_piece = self.board[end_row][end_col]

            # Check if the move captures the opponent's king
            if target_piece and target_piece.type == 'K' and target_piece.color != start_piece.color:
                print(f"Game Over! {self.turn} wins by capturing the King.")
                self.board[end_row][end_col] = start_piece
                self.board[start_row][start_col] = None
                return "Game Over"

            self.board[end_row][end_col] = start_piece
            self.board[start_row][start_col] = None

            if isinstance(start_piece, Pawn):
                start_piece.mark_as_moved()

            self.turn = 'B' if self.turn == 'W' else 'W'
            return True

        print("Invalid Move")
        return False


def convert_position(position):
    col = ord(position[0]) - ord('a')
    row = 8 - int(position[1])
    return col, row


def play_game():
    chess_board = ChessBoard()
    chess_board.print_board()
    print()

    while True:
        move = input().strip()

        if move == 'exit':
            break

        start, end = move.split()
        start_col, start_row = convert_position(start)
        end_col, end_row = convert_position(end)

        result = chess_board.move_piece((start_col, start_row), (end_col, end_row))
        if result == "Game Over":
            break

        chess_board.print_board()
        print()


if __name__ == "__main__":
    play_game()