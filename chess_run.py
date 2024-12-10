from chess_board import Solution

# Sample helper class to print outputs
class Helper:
    def println(self, message):
        print(message)

# Initialize the chessboard
initial_board = [
    ['BR', 'BH', 'BB', 'BQ', 'BK', 'BB', 'BH', 'BR'],
    ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP'],
    ['..', '..', '..', '..', '..', '..', '..', '..'],
    ['..', '..', '..', '..', '..', '..', '..', '..'],
    ['..', '..', '..', '..', '..', '..', '..', '..'],
    ['..', '..', '..', '..', '..', '..', '..', '..'],
    ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP'],
    ['WR', 'WH', 'WB', 'WQ', 'WK', 'WB', 'WH', 'WR']
]

# Instantiate the solution and initialize the game
helper = Helper()
solution = Solution()
solution.init(helper, initial_board)

# Perform some moves
print("Move WP from (6, 0) to (5, 0):", solution.move(6, 0, 5, 0))  # Valid pawn move
print("Move BP from (1, 1) to (3, 1):", solution.move(1, 1, 3, 1))  # Invalid pawn move
print("Move BP from (1, 1) to (2, 1):", solution.move(1, 1, 2, 1))  # Valid pawn move

# Check game state and next turn
print("Game Status:", solution.get_game_status())  # Should be 0 (game in progress)
print("Next Turn:", solution.get_next_turn())  # Should alternate between 0 (white) and 1 (black)

# Test an invalid move
print("Invalid move WP from (5, 0) to (7, 0):", solution.move(5, 0, 7, 0))  # Backward pawn move

# Capture a piece
solution.move(6, 1, 4, 1)  # Move a white pawn forward
solution.move(1, 0, 3, 0)  # Move a black pawn forward
print("Capture BP with WP at (4, 0):", solution.move(4, 1, 3, 0))  # Capture

# Check the game state after capturing a king (simulate win)
solution.move(7, 4, 6, 4)  # Move the white king
solution.move(0, 4, 1, 4)  # Move the black king
print("Capture BK with WK:", solution.move(6, 4, 1, 4))  # Capture black king
print("Game Status after capturing BK:", solution.get_game_status())  # Should be 1 (white wins)
print("Next Turn after game ends:", solution.get_next_turn())  # Should be -1
