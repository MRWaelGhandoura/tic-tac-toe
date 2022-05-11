import math
import time
from player import RealPlayer, NoobComputerPlayer, ProComputerPlayer
from termcolor import colored
import pyfiglet


ASCII_BANNER = pyfiglet.figlet_format(
    "Hello!! \n WELCOME TO TIC TAC TOE GAME!!")
COLOR_CHOICES = ["1- Red", "2-Yellow"]


# A function to print the Tic Tac Toe board
class Game:
    """
    A class to define the structure of the Tic tac toe game:
    A welcome massage
    A Game board
    A Display board
    To Make a move with a tag
    To Validate the move
    To check if the last move is a winning move

    """
    def __init__(self, username, game_mode):
        self.username = username
        self.color = self.get_color()
        self.board = [' ' for _ in range(9)]  # 3x3 game board
        self.current_winner = None  # track the winner
        if game_mode == 'easy':
            print(f"You've selected {game_mode}, good luck!\n")
            self.computer = NoobComputerPlayer('O')
        elif game_mode == 'hard':
            print(f"You've selected {game_mode}, try your hardest to beat the computer!\n")  # noqa
            self.computer = ProComputerPlayer('O')
        self.player = RealPlayer('X')


    def print_board(self):
        print('')
        print("Available Moves       Game Board")
        for num, row in enumerate([self.board[i*3:(i+1)*3] for i in range(3)]):
            availableMoves = self.available_moves_display()
            availableRow = availableMoves[num*3:(num+1)*3]
            availablePart = '| ' + ' | '.join(availableRow) + ' |'
            boardPart = '       | ' + ' | '.join(row) + ' |'
            print(availablePart + boardPart)

    @staticmethod
    def print_board_nums():
        """
        Tells us which number corresponds to each empty space
        1 | 2 | 3 etc.
        """
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]  # noqa
        for row in number_board:
            numered_board = '| ' + ' | '.join(row) + ' |'
            print(numered_board)

        print('')    

    def get_color(self):
        print("choose your color")
        print(COLOR_CHOICES)
        color = input().strip()
        while color not in ["1", "2"]:
            print("you must enter 1 or 2")
            color = input().strip()
        if color == "1":
            self.color = 'red'
        elif color == "2":
            self.color = 'yellow'
        print(colored("You choose your color !!", self.color))
        print(color)

    
   


def welcome():
    print(ASCII_BANNER)
    print("Please Enter your name: \n")
    username = input().strip()

    while len(username) == 0:
        print("It looks like you haven't typed anything, please enter your name!")  # noqa
        username = input().strip()
    # return hello message
    print("\nHi " + f"{username}!" + " Nice to meet you!\n")
    game = Game(username)


welcome()
