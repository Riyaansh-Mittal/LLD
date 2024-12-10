from tic_tac_toe import TicTacToeGame

if __name__ == "__main__":
    game: TicTacToeGame = TicTacToeGame()
    print(f"Game winner is : {game.start_game()}")