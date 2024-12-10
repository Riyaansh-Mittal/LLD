import random
from collections import deque


class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0

    def set_position(self, position):
        self.position = position

    def get_position(self):
        return self.position

    def __str__(self):
        return self.name


class Entity:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Snake(Entity):
    def __init__(self, head, tail):
        if head <= tail:
            raise ValueError("Snake's head must be higher than its tail.")
        super().__init__(head, tail)


class Ladder(Entity):
    def __init__(self, start, end):
        if start >= end:
            raise ValueError("Ladder's start must be lower than its end.")
        super().__init__(start, end)


class Board:
    def __init__(self):
        self.snakes = {}
        self.ladders = {}
        self.players = {}
        self.player_order = deque()

    def add_snake(self, head, tail):
        if head == 100:
            raise ValueError("Snake's head cannot be at position 100.")
        if head in self.snakes or head in self.ladders:
            raise ValueError("Duplicate start/head point for snake or ladder.")
        self.snakes[head] = Snake(head, tail)

    def add_ladder(self, start, end):
        if start in self.snakes or start in self.ladders:
            raise ValueError("Duplicate start/head point for snake or ladder.")
        self.ladders[start] = Ladder(start, end)

    def add_player(self, name):
        if name in self.players:
            raise ValueError("Player name must be unique.")
        player = Player(name)
        self.players[name] = player
        self.player_order.append(name)

    def get_final_position(self, position):
        visited = set()
        while position in self.snakes or position in self.ladders:
            if position in visited:
                raise ValueError("Infinite loop detected with snakes and ladders.")
            visited.add(position)
            if position in self.snakes:
                position = self.snakes[position].end
            elif position in self.ladders:
                position = self.ladders[position].end
        return position

    def is_winnable(self):
        visited = set()
        stack = [1]
        while stack:
            pos = stack.pop()
            if pos == 100:
                return True
            if pos in visited:
                continue
            visited.add(pos)
            for dice_roll in range(1, 7):
                next_pos = pos + dice_roll
                if next_pos <= 100:
                    next_pos = self.get_final_position(next_pos)
                    if next_pos not in visited:
                        stack.append(next_pos)
        return False


class Game:
    def __init__(self):
        self.board = Board()

    def setup(self):
        # Input snakes
        num_snakes = int(input("Enter number of snakes: "))
        for _ in range(num_snakes):
            head, tail = map(int, input("Enter snake head and tail: ").split())
            self.board.add_snake(head, tail)

        # Input ladders
        num_ladders = int(input("Enter number of ladders: "))
        for _ in range(num_ladders):
            start, end = map(int, input("Enter ladder start and end: ").split())
            self.board.add_ladder(start, end)

        # Input players
        num_players = int(input("Enter number of players: "))
        for _ in range(num_players):
            player_name = input("Enter player name: ")
            self.board.add_player(player_name)

        # Check if the game is winnable
        if not self.board.is_winnable():
            raise ValueError("The game configuration is not winnable!")

    def play(self):
        while True:
            current_player_name = self.board.player_order.popleft()
            current_player = self.board.players[current_player_name]
            dice_roll = random.randint(1, 6)

            initial_position = current_player.get_position()
            final_position = initial_position + dice_roll

            if final_position > 100:
                final_position = initial_position  # Stay in place if roll exceeds 100
            else:
                final_position = self.board.get_final_position(final_position)

            current_player.set_position(final_position)
            print(
                f"{current_player_name} rolled a {dice_roll} and moved from {initial_position} to {final_position}"
            )

            if final_position == 100:
                print(f"{current_player_name} wins the game!")
                break

            self.board.player_order.append(current_player_name)


if __name__ == "__main__":
    game = Game()
    game.setup()
    game.play()
