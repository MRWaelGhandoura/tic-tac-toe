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
        show us the number corresponds to each empty space
        1 | 2 | 3 etc.
        """
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]  # noqa
        for row in number_board:
            numered_board = '| ' + ' | '.join(row) + ' |'
            print(numered_board)

        print('')

    def play(game_mode, print_game=True):
    """
    returns the winner of the game or None if it's a tie
    """

    game = Game(username, game_mode)

    if print_game:
        game.print_board_nums()

    tag = 'X'  # starting tag

    while game.empty_squares():
        """
        iterate as long as the game-board still has empty squares
        gets move from appropriate player
        """
        if tag == 'O':
            square = game.computer.get_move(game)
        else:
            square = game.player.get_move(game)

        if game.make_move(square, tag):
            if print_game:
                print(tag + f' makes a move to square {square}')
                game.print_board()
                print('')  # empty line

            if game.current_winner:
                if print_game:
                    print(tag + ' wins!')
                return tag

            # alternates / switches players for each round
            if tag == 'X':
                tag = 'O'
            else:
                tag = 'X'

        time.sleep(2)  # a break in between moves to make the game more user friendly # noqa
    if print_game:
        print('It\'s a tie!') 

    def available_moves_display(self):
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(str(i))
            else:
                moves.append(' ')
        return moves

    def available_moves(self):
        moves = []
        for (i, spot) in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, tag):
        """
        if the move is valid, proceed & return True
        if the move is invalid, return False
        """
        if self.board[square] == ' ':
            self.board[square] = tag
            if self.winner(square, tag):
                self.current_winner = tag
            return True
        return False       

    def winner(self, square, letter):
        # check the row
        row_ind = math.floor(square / 3)
        row = self.board[row_ind*3:(row_ind+1)*3]
        # print('row', row)
        if all([s == letter for s in row]):
            return True
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        # print('col', column)
        if all([s == letter for s in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            # print('diag1', diagonal1)
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            # print('diag2', diagonal2)
            if all([s == letter for s in diagonal2]):
                return True
        return False

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]
        

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
