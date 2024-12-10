from collections import deque

class Player:
    def __init__(self, sign, name):
        self.sign = sign
        self.name = name

class Board:
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.players = {}
        self.current_player = 'X'
    
    def setPlayers(self, sign, name):
        self.players[sign] = Player(sign, name)
    
    def showBoard(self):
        for row in self.board:
            print(" ".join(cell if cell else "-" for cell in row))
        print()

    def isValidMove(self, x, y):
        return 0 <= x < 3 and 0 <= y < 3 and self.board[x][y] is None

    def move(self, x, y, player):
        self.board[x][y] = player
        self.showBoard()

    def checkWin(self, x, y, player):
        if all(self.board[x][i] == player for i in range(3)):  # Row
            return True
        if all(self.board[i][y] == player for i in range(3)):  # Column
            return True
        if x == y and all(self.board[i][i] == player for i in range(3)):  # Diagonal
            return True
        if x + y == 2 and all(self.board[i][2 - i] == player for i in range(3)):  # Anti-diagonal
            return True
        return False

class Game:
    def __init__(self):
        self.board = Board()

    def setup(self):
        for _ in range(2):
            sign, name = input().split()
            self.board.setPlayers(sign, name)
        self.board.showBoard()

    def play(self):
        moves_left = 9
        while moves_left > 0:
            move = input()
            if move == "exit":
                return
            try:
                x, y = map(int, move.split())
                x, y = x - 1, y - 1
                if self.board.isValidMove(x, y):
                    player = self.board.current_player
                    self.board.move(x, y, player)
                    if self.board.checkWin(x, y, player):
                        print(f"{self.board.players[player].name} won the game")
                        return
                    self.board.current_player = 'O' if player == 'X' else 'X'
                    moves_left -= 1
                else:
                    print("INVALID MOVE")
            except ValueError:
                print("INVALID MOVE")
        print("GAME OVER")

if __name__ == "__main__":
    game = Game()
    game.setup()
    game.play()
