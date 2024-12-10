from collections import deque

class Player():
    def __init__(self, sign, name, moves):
        self.sign = sign
        self.name = name
        self.moves = moves
    
    def getName(self):
        return self.name
    def getMoves(self):
        return self.moves
    def setMoves(self):
        self.moves =- 1

class Board():
    def __init__(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.queue = deque()
        self.players = {}
    
    def setPlayers(self, sign, name):
        if(sign == 'X'):
            self.queue.appendleft(sign)
            moves = 5
        elif(sign == 'O'):
            self.queue.append(sign)
            moves = 4
        self.players[sign] = Player(sign, name, moves)
        
    def getPlayerName(self, sign):
        name = self.players[sign]
        name = name.getName()
        return name
    
    def move(self, x, y, player):
            self.board[x][y] = player
            self.showBoard()
        
    def showBoard(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j] if self.board[i][j] else '-', end=" ")
            print('\n')
    
    def checkWin(self, x, y, player):
        win = True
        #check horizontal
        for i in range(0,3):
            if(self.board[x][i] != player):
                win = False
                break
        if(win):
            return True
        #check vertical
        win = True
        for i in range(0,3):
            if(self.board[i][y] != player):
                win = False
                break
        if(win):
            return True
        #check diagonal
        win = True
        for i in range(0,3):
            if(self.board[i][i] != player):
                win = False
                break
        if(win):
            return True
        #check other diagonal
        win = True
        for i in range(0,3):
            if(self.board[i][2-i] != player):
                win = False
                break
        if(win):
            return True
            
        
        

class Game():
    def __init__(self):
        self.board = Board()
    
    def setup(self):
        for _ in range(2):
            sign, name = input().split()
            self.board.setPlayers(sign, name)
        self.board.showBoard()
    
    def play(self):
        for _ in range(9):
            while(True):
                move = input()
                if(move == 'exit'):
                    return
                move = move.split()
                x=int(move[0])
                y=int(move[1])
                if(x <= 3 and x > 0 and y <= 3 and x > 0 and self.board.board[x-1][y-1] == None):
                    current = self.board.queue.popleft()
                    self.board.move(x-1, y-1, current)
                    self.board.queue.append(current)
                    #check if player has won
                    if(self.board.checkWin(x-1 ,y-1, current)):
                        print(self.board.getPlayerName(current) + ' won the game')
                        return
                    break
                else:
                    print('INVALID MOVE')
        print('GAME OVER')

if __name__ == "__main__":
    game = Game()
    game.setup()
    game.play()
                
    
    