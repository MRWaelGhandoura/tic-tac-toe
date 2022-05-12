import math
import random


class Player():
    """
    A superclass is created for the user, the computer  level 
    and computer hard level. 
    Player class to select a inputTag  X  O and a game.
    
    """
    def __init__(self, character):
        self.character = character

    def get_move(self, game):
        pass

class RealPlayer(Player):
     """
     The RealPlayer class is used to define a real player
     who plays against another real player. 
     It makes its moves taking into account the player's input 
     regarding the available squares on the board.

     """

    def __init__(self, character):
        super().__init__(character)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.character + '\'s turn. Input move (0-8): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid move. Try again.')
        return val

class NoobComputerPlayer(Player):
    """
    The class noobComputerPlayer is used to define a computer
    against which the user can play. 
    It makes its moves randomly, depending on what moves are available on the game board.

    """

    def __init__(self, character):
        super().__init__(character)

    def get_move(self, game):
        square = random.choice(game.available_moves())
        return square


class ProComputerPlayer(Player):
    """
    ProComputerPlayer is a class that defines an unbeatable
    computer player that uses a minimax algorithm to function.
    The algorithm maximizes his score while minimizing his
     losses, making it impossible to defeat him.

    """
    def __init__(self, input_tag):
        super().__init__(input_tag)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves())
        else:
            square = self.minimax(game, self.input_tag)['position']
        return square

    def minimax(self, state, player):
        max_player = self.input_tag  # User
        other_player = 'O' if player == 'X' else 'X'

        # Checking the previous move if it is a win move
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            return {'position': None, 'score': 0}

        if player == max_player:
            best = {'position': None, 'score': -math.inf}  # maximizing each score
        else:
            best = {'position': None, 'score': math.inf}  # minimizing each score
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            sim_score = self.minimax(state, other_player)  # simulate a game after making that move

            # undo move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move  # this represents the move optimal next move

            if player == max_player:  # X is max player
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score
        return best        