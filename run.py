from players import RealPlayer, NoobComputerPlayer, ProComputerPlayer
from colorama import Fore
from termcolor import colored
import time
import pyfiglet


# A function to print the Tic Tac Toe board
class TicTacToe:
    """
    A class to define the structure of the Tic tac toe game:
    A welcome massage
    A Game board
    A Display board
    To Make a move with a input tag
    To Validate the move
    To check if the last move is a winning move

    """
    def __init__(self, game_mode):
        self.board = [' ' for _ in range(9)]  # 3x3 game board
        self.current_winner = None  # track the winner
        if game_mode == 'easy':
            print(f"You've selected {game_mode}, good luck!\n")
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
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        # 0 | 1 | 2
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, character):
        if self.board[square] == ' ':
            self.board[square] = character
            if self.winner(square, character):   # check the winner
                self.current_winner = character
            return True
        return False

    # code credit: https://www.youtube.com/watch?v=n2o8ckO-lfk&list=PLAA3uifegEK98UkLE614yowsG7OHfANz9&index=1&t=663s
    def winner(self, square, character):
        """
        winner if player ticks 3 in a row (either vertically, horizontally, or diagonally)
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
    returns the winner of the game or None if it's a tie
    """

    game = TicTacToe(game_mode)

    if print_game:
        game.print_board_nums()

    character = 'X'  # starting character

    while game.empty_squares():
        """
        iterate as long as the game-board still has empty squares
        gets move from appropriate player
        """
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

    print(Fore.YELLOW + "███████████████████████████████████████")
    print("█                                     █")
    print("█   ▄▄█▄▄█▄▄   " + Fore.BLUE + "TIC" + Fore.YELLOW + "                █")
    print("█   ▄▄█▄▄█▄▄       TAC                  █")
    print("█   " + Fore.RED + "X" + Fore.YELLOW + " █  █ " + Fore.BLUE + "O" + Fore.YELLOW + "       " + Fore.RED + "TOE" + Fore.YELLOW + "            █")
    print("█                                     █")
    print("█                    By Wael Ghandoura█")
    print("███████████████████████████████████████\n")

    time.sleep(2)

    print("Welcome to " + Fore.BLUE + "TIC" + Fore.YELLOW + "TAC " + Fore.RED + "TOE" + Fore.YELLOW + "!")

    time.sleep(2)

    while True:
        user = input("Please enter a username: \n")
        if len(user.strip()) == 0:
            print("Invalid username")
            continue
        else:
            break

    time.sleep(2)

    print(f"Hello {user}!")

    time.sleep(2)

    # code credit: help from https://stackoverflow.com/questions/42091015/check-if-python-input-contains-a-specific-word/42091192 # noqa
    while True:
        difficulty = input("Please select a difficulty to continue. Type in 'easy', 'hard' or 'quit' to exit: \n").strip().lower()  # noqa
        time.sleep(2)
        if difficulty == 'quit':
            print(f"Thanks for playing {user}, goodbye!")
            break
        elif difficulty == 'easy' or difficulty == 'hard':
            play(difficulty)
        else:
            print("You need to enter a valid difficulty to continue...\n")
            continue
    # end credit


welcome()
