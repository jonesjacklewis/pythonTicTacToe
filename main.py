from TicTacToe import TicTacToe


player_1 = input("Enter player one's name: ")
player_1_symbol = input("Enter a single character for player one's symbol: ")[0].upper()

player_2 = input("Enter player two's name: ")
player_2_symbol = input("Enter a single character for player two's symbol: ")[0].upper()

size = ""

while not size.isdigit():
    size = input("Enter the game board size: ")

size = int(size)

game = TicTacToe(
    player_one = player_1,
    player_two = player_2,
    player_one_symbol = player_1_symbol,
    player_two_symbol = player_2_symbol,
    size = size
)

game.game()