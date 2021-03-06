from players import RealPlayer, NoobComputerPlayer, ProComputerPlayer
import colorama
import time
import pyfiglet

ASCII_BANNER = pyfiglet.figlet_format(
    "Hello!! \n WELCOME TO TIC TAC TOE GAME!!")
COLOR_CHOICES = ["1- Red", "2-Yellow"]


# A function to print the Tic Tac Toe board
class TicTacToe:
    """
    A class to define the structure of the Tic tac toe game:
    A welcome massage
    A Game board
    A Display board
    To Make a move with a input tag
    To Validate the move
    To check the winning move

    """

    def __init__(self, game_mode):
        self.color = self.get_color()
        self.board = [' ' for _ in range(9)]  # 3x3 game board
        self.current_winner = None  # track the winner
        if game_mode == 'easy':
            print(f"You've selected {game_mode}, easy for you, good luck!\n")
            self.computer = NoobComputerPlayer('O')
        elif game_mode == 'hard':
            print(f"You've selected {game_mode}, good luck beating the PRO!\n")
            self.computer = ProComputerPlayer('O')
        self.player = RealPlayer('X')

    @staticmethod
    def make_board():
        return [' ' for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1) * 3] for i in range(3)]:
            print(('| ' + ' | '.join(row) + ' |').replace('X',
                  f'{self.color}X{colorama.Fore.WHITE}'))

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, character):
        if self.board[square] == ' ':
            self.board[square] = character
            if self.winner(square, character):   # check the winner
                self.current_winner = character
            return True
        return False

    # code credit: https://www.geeksforgeeks.org/print-colors-python-terminal/ # noqa
    def get_color(self):
        print("choose your color\n")
        print(COLOR_CHOICES)
        color = input().strip()
        color_choice = 'white'
        while color not in ["1", "2"]:
            print("You must enter 1 or 2")
            color = input().strip()
        if color == "1":
            color_choice = colorama.Fore.RED
            # print(colored("You choose Red !!\n", color_choice))
            print(f'{color_choice}You choose Red !!\n{colorama.Fore.WHITE}')
        elif color == "2":
            color_choice = colorama.Fore.YELLOW
            # print(colored("You choose Yellow !!\n", color_choice))
            print(f'{color_choice}You choose Yellow !!\n{colorama.Fore.WHITE}')
        return color_choice

    # code credit: https://www.youtube.com/watch?v=n2o8ckO-lfk&list=PLAA3uifegEK98UkLE614yowsG7OHfANz9&index=1&t=663s  # noqa
    def winner(self, square, character):
        """
        winner if player ticks 3 in a row (vertically, horizontally, or diagonally)  # noqa
        """

        # checks row
        row_ind = square // 3
        row = self.board[row_ind*3: (row_ind + 1) * 3]
        if all([spot == character for spot in row]):
            return True

        # checks column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == character for spot in column]):
            return True

        # checks diagonally
        # only possible if all squares are even numbers
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == character for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == character for spot in diagonal2]):
                return True

        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]


def play(game_mode, print_game=True):
    """
    returns the winner of the game or nothing if it's a tie
    """

    game = TicTacToe(game_mode)

    if print_game:
        game.print_board_nums()

    character = 'X'  # starting character

    while game.empty_squares():  # as long as the game board still has empty squares,the corresponding player gets a turn.  # noqa
        if character == 'O':
            square = game.computer.get_move(game)
        else:
            square = game.player.get_move(game)

        if game.make_move(square, character):
            if print_game:
                print(character + f' makes a move to square {square}')
                game.print_board()
                print('')  # empty line

            if game.current_winner:
                if print_game:
                    print(character + ' wins!')
                return character

            # alternates between players each round
            if character == 'X':
                character = 'O'
            else:
                character = 'X'

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')


def welcome():
    # code credit: https://towardsdatascience.com/prettify-your-terminal-text-with-termcolor-and-pyfiglet-880de83fda6b  # noqa
    print(ASCII_BANNER)
    print("Please Enter your name: \n")
    username = input().strip()

    while len(username) == 0:
        print("It looks like you haven't typed anything, please enter your name!")  # noqa
        username = input().strip()
    # return hello message
    print("\nHi " + f"{username}!" + " Nice to meet you!\n")

    time.sleep(1)

    # code credit: https://codereview.stackexchange.com/questions/179550/python-tic-tac-toe-game-with-two-difficulty-levels # noqa
    while True:
        difficulty = input("Select a difficulty to start playing. Type in 'easy', 'hard' or 'quit' to exit: \n").strip().lower()  # noqa
        time.sleep(2)
        if difficulty == 'quit':
            print(f"Thanks for playing {username}, goodbye!")
            break
        elif difficulty == 'easy' or difficulty == 'hard':
            play(difficulty)
        else:
            print("Please enter a valid option to continue...\n")
            continue


welcome()
