from player import RealPlayer, NoobComputerPlayer, ProComputerPlayer
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
    def __init__(self):
        self.board = self.make_board()
        self.current_winner = None

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
        winner if player ticks 3 in a row (either vertically, horizontally, or diagonally) # noqa
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

    def play(game, x_player, o_player, print_game=True):
        """
        returns the winner of the game or None if it's a tie
        """

    if print_game:
        game.print_board_nums()

    character = 'X'
    while game.empty_squares():
        if character == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)
        if game.make_move(square, character):

            if print_game:
                print(character + ' makes a move to square {}'.format(square))
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(character + ' wins!')
                return character  # ends loop and exits the game
            
            # alternates between players each round
            if character == 'X':
                character = 'O'
            else:
                character = 'X'

        time.sleep(.8)

    if print_game:
        print('It\'s a tie!')

if __name__ == '__main__':
    x_player = ProComputerPlayer('X')
    o_player = RealPlayer('O')
    t = TicTacToe()
    play(t, x_player, o_player, print_game=True)
