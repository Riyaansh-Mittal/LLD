import random
from collections import deque


class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def get_name(self):
        return self.name

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position


class Snake:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail


class Ladder:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end


class Board:
    def __init__(self):
        self.snakes = {}
        self.ladders = {}
        self.players = {}
    
    def set_snake(self, head, tail):
        if head == 100:
            raise ValueError("Snake's head cannot be at position 100.")
        if head in self.snakes or head in self.ladders:
            raise ValueError("Duplicate start/head point for snake or ladder.")
        if head <= tail:
            raise ValueError("Snake's head must be higher than its tail.")
        self.snakes[head] = Snake(head, tail)

    def set_ladder(self, start, end):
        if start in self.snakes or start in self.ladders:
            raise ValueError("Duplicate start/head point for snake or ladder.")
        if start >= end:
            raise ValueError("Ladder's start must be smaller than its end.")
        self.ladders[start] = Ladder(start, end)

    def add_player(self, name):
        self.players[name] = Player(name)

    def get_final_position(self, pos):
        while pos in self.snakes or pos in self.ladders:
            if pos in self.snakes:
                pos = self.snakes[pos].get_tail()
            elif pos in self.ladders:
                pos = self.ladders[pos].get_end()
        return pos


class Game:
    def __init__(self):
        self.board = Board()
        self.queue = deque()

    def set_snake(self, head, tail):
        self.board.set_snake(head, tail)

    def set_ladder(self, start, end):
        self.board.set_ladder(start, end)

    def add_player(self, name):
        self.board.add_player(name)
        self.queue.append(name)

    def play_turn(self):
        current_player_name = self.queue.popleft()
        current_player = self.board.players[current_player_name]
        dice_roll = random.randint(1, 6)
        initial_position = current_player.get_position()
        final_position = initial_position + dice_roll

        if final_position > 100:
            final_position = initial_position  # Cannot move beyond 100
        else:
            final_position = self.board.get_final_position(final_position)

        current_player.set_position(final_position)
        print(
            f"{current_player_name} rolled a {dice_roll} and moved from {initial_position} to {final_position}"
        )

        if final_position == 100:
            print(f"{current_player_name} wins the game!")
            return False

        self.queue.append(current_player_name)
        return True


if __name__ == "__main__":
    game = Game()

    # Input snakes
    num_snakes = int(input())
    for _ in range(num_snakes):
        head, tail = map(int, input().split())
        game.set_snake(head, tail)

    # Input ladders
    num_ladders = int(input())
    for _ in range(num_ladders):
        start, end = map(int, input().split())
        game.set_ladder(start, end)

    # Input players
    num_players = int(input())
    for _ in range(num_players):
        player_name = input()
        game.add_player(player_name)

    # Play the game
    while game.play_turn():
        pass
