import math
import random


class Player():
    """
    A superclass is created for the user, the computer  level 
    and computer hard level. 
    Player class to select a tag ( X or O) and a game.
    
    """
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RealPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid move. Try again.')
        return val

