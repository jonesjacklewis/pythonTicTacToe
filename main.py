from TicTacToe import TicTacToe


player_1 = input("Enter player one's name: ")
player_2 = input("Enter player two's name: ")

size = ""

while not size.isdigit():
    size = input("Enter the game board size")

game = TicTacToe(player_1, player_2, int(size))

game.game()