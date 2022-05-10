from termcolor import colored
import pyfiglet


ASCII_BANNER = pyfiglet.figlet_format(
    "Hello!! \n WELCOME TO TIC TAC TOE GAME!!")
COLOR_CHOICES = ["1- Red", "2-Yellow"]

# A function to print the Tic Tac Toe board
class Game:
    """
    A class to play tic tac toe


    """
    def __init__(self, username):
        self.username = username
        self.color = self.get_color()

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




def print_tic_tac_toe(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")


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
