class TicTacToe:
    """A method to model a game of TicTacToe"""

    def __init__(self, player_one, player_two, size=3):
        """The initialiser for the TicTacToe class

        Args:
            player_one (str): The name of player one
            player_two (str): The name of player two
            size (int): The size of the board size x size. Defaults to 3.
        """

        self.board = [["*" for _ in range(size)] for _ in range(size)]

        self.player_one = player_one

        self.player_two = player_two

        self.game_over = False
        self.winner = None

        self.x_message = "Enter an x coordinate: "
        self.y_message = "Enter a y coordinate: "

    def __player_one_move(self, coordinate):
        """Method to model player one moving

        Args:
            coordinate (list): A list consisting of the x and y coordinates of the place to mark
        """
        self.board[coordinate[1]][coordinate[0]] = "x"
        self.output_board()

    def __player_two_move(self, coordinate):
        """Method to model player two moving

        Args:
            coordinate (list): A list consisting of the x and y coordinates of the place to mark
        """
        self.board[coordinate[1]][coordinate[0]] = "o"
        self.output_board()

    def __round(self):
        """Method to model a single round of the game"""
        player_one_move = [int(input(self.x_message)), int(input(self.y_message))]

        if self.board[player_one_move[1]][player_one_move[0]] != "*":
            while self.board[player_one_move[1]][player_one_move[0]] != "*":
                print("Space already taken!")
                player_one_move = [
                    int(input(self.x_message)),
                    int(input(self.y_message)),
                ]
        self.__player_one_move(player_one_move)
        self.__check()
        print("\n\n")

        if self.game_over:
            return

        player_two_move = [int(input(self.x_message)), int(input(self.y_message))]

        if self.board[player_two_move[1]][player_two_move[0]] != "*":
            while self.board[player_two_move[1]][player_two_move[0]] != "*":
                print("Space already taken!")
                player_two_move = [
                    int(input(self.x_message)),
                    int(input(self.y_message)),
                ]
        self.__player_two_move(player_two_move)
        self.__check()

        print("\n\n")

    def game(self):
        """Method to model the entire game"""
        self.output_board()

        while not self.game_over:
            self.__round()

        if self.winner == "none":
            print("No One won, it was a draw")
        else:
            print(f"{self.winner}, won the game!")

    def output_board(self):
        """Method to output the game board"""
        rows = ["@"]

        rows.extend(str(i) for i in range(len(self.board)))
        print("|".join(rows))

        for i, row in enumerate(self.board, start=0):
            print(i, "|".join(row), sep="|")

    def __check_horizontal(self, board=False):
        """Method to check the rows to see if there is a winner

        Args:
            board (bool, optional): The board that should be checked. Defaults to False.

        Returns:
            List: List containing if there is a winner and if so who
        """
        if not board:
            board = self.board
        for row in board:
            if len(set(row)) == 1:
                if row[0] == "x":
                    return [True, self.player_one]
                if row[1] == "o":
                    return [True, self.player_two]
        return [False, None]

    def __check_vertical(self):
        """Method to check the columns to see if there is a winner

        Returns:
            List: List containing if there is a winner and if so who
        """
        rotate_board = list(zip(*self.board[::-1]))
        return self.__check_horizontal(rotate_board)

    def __check_left_diagonal(self):
        """Method to check the left diagonal to see if there is a winner

        Returns:
            List: List containing if there is a winner and if so who
        """
        elements = [self.board[i][i] for i in range(len(self.board))]

        if len(set(elements)) == 1:
            if elements[0] == "x":
                return [True, self.player_one]
            if elements[1] == "o":
                return [True, self.player_two]

        return [False, None]

    def __check_right_diagonal(self):
        """Method to check the right diagonal to see if there is a winner

        Returns:
            List: List containing if there is a winner and if so who
        """
        max_x = len(self.board) - 1
        y = 0
        elements = []

        while y != 0:
            elements.append(self.board[y][max_x])
            y += 1
            max_x -= 1

        if len(set(elements)) == 1:
            if elements[0] == "x":
                return [True, self.player_one]
            if elements[1] == "o":
                return [True, self.player_two]

        return [False, None]

    def __check(self):
        """Method to check the game board to see if there is a winner/if it is stalemate"""
        horizontal = self.__check_horizontal()

        if horizontal[0]:
            self.game_over = True
            self.winner = horizontal[1]

        vertical = self.__check_vertical()

        if vertical[0]:
            self.game_over = True
            self.winner = vertical[1]

        left_vertical = self.__check_left_diagonal()

        if left_vertical[0]:
            self.game_over = True
            self.winner = left_vertical[1]

        right_vertical = self.__check_right_diagonal()

        if right_vertical[0]:
            self.game_over = True
            self.winner = right_vertical[1]

        if sum(row.count("*") for row in self.board) == 0:
            self.game_over = True
            self.winner = "none"
