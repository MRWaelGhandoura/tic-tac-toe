# TIC TAC TOE

![image](https://user-images.githubusercontent.com/99558735/168180857-756cfd07-711f-4d6a-ba5d-2da1143f0f6e.png)


## Author
WAEL GHANDOURA

## Project Overview

![Python Terminal by Code Institute - Google Chrome - 13 May 2022](https://user-images.githubusercontent.com/99558735/168200871-97ef977d-e519-49ca-8543-87367aef0536.gif)


- A Tic Tac Toe game, a player versus computer style game, developed with Python as the only language. It contains two difficulty levels that are selected by the user   ( Noob level and Pro level). The user can select a color theme to use the character on the game board. The user can then play either against a computer that randomly   selects its moves, or against a computer that maximizes its wins while minimizing its losses, making it unbeatable.

- You can view my deployed app https://tic-tac-toe-waelgh.herokuapp.com/.


## How To Play/Use

- Go to the page : https://tic-tac-toe-waelgh.herokuapp.com/
- Click on "Run Program."
- Enter your user name.
- Choose your color.
- Select the difficulty level (either "easy" or "hard").
- You will be playing against a computer.
- Choose your first move from a numbered list of empty squares from 0 to 8.
- Then wait for the computer's turn, and when the board is full, which means the game ends, a result display appears, whether a win, a loss, or a draw.
- At the end you have the choice to play again or to quit by typing quit.

## Features

### Implemented Features

- Game logo: as a welcome to the user as a Pyfiglet/ASCII text
 inhereted from : https://towardsdatascience.com/prettify-your-terminal-text-with-termcolor-and-pyfiglet-880de83fda6b
 
![image](https://user-images.githubusercontent.com/99558735/168204158-19037782-48cf-4e79-b216-6eb0230d45d4.png)


- Game intro: letting the user enters his name

![image](https://user-images.githubusercontent.com/99558735/168204654-82c2a319-892a-4b29-8d86-8309768fff1e.png)


- Game mode: with two choices for the difficulty , and the one if he wishes to quit the game. 
- If you choose the "easy" option, the user plays against a computer that chooses its moves randomly and is therefore easy to beat. When choosing "hard", the user    plays against an ingenious computer that uses an algorithm to maximize its score while minimizing its losses, making it seemingly unbeatable. Finally, the "Quit" option offers the user a way to end the game. With each option, a personalized message is given to the user.

![image](https://user-images.githubusercontent.com/99558735/168205285-bdd26ad8-4033-47c1-8fc2-0204b5ad3556.png)


- Color mode: with two choices for the user, who can choose between red and yellow. 
- The selected color is printed on the board which makes it easier for the user's eyes to distinguish between his color and the color of the computer character.

![image](https://user-images.githubusercontent.com/99558735/168205909-fc0306f6-08be-49ef-92dd-c422a0446446.png)

![image](https://user-images.githubusercontent.com/99558735/168205977-c6a4cc0d-721e-4308-803f-67bdb87bc9d9.png)

![image](https://user-images.githubusercontent.com/99558735/168206051-82d1b9c2-3207-47ad-b427-09718883b6d9.png)

![image](https://user-images.githubusercontent.com/99558735/168206088-6ec8dec3-64e0-427e-8e8b-b0cabe95d577.png)


- Result mode: After each move, the game checks if the previous move was a winning move (a straight line vertically, horizontally or diagonally) and if it finds a winning move, it gives it to the tag with which the straight line was scored. If no moves are available on the board and no one has won, the game sends the "Tie" message.

![image](https://user-images.githubusercontent.com/99558735/168206414-f396e28b-79bf-49a1-b01c-85233129d89b.png)

![image](https://user-images.githubusercontent.com/99558735/168206583-03bfd6cb-a148-4af4-94bf-dcf9a852ac5e.png)

![image](https://user-images.githubusercontent.com/99558735/168206701-e953374a-b8db-4d65-90fa-ad8f29b7893b.png)



### Future Features

- An option for the user to choose a tag to start with.
- An option to store the score of the user with a score board.
- Adding more colors and animation to the game.


## Design Documents

- Game flow chart using : https://lucid.app/lucidchart/

![image](https://user-images.githubusercontent.com/99558735/168215286-d6cf9ac1-c2f9-437b-89fd-3e8b392778b6.png)

- Code flow chart:

![image](https://user-images.githubusercontent.com/99558735/168218058-9d8cf774-b55f-4b9d-8169-5bb47c64171b.png)


## Data Model/ Classes

## Classes
Four classes were created on an another python sheet to get let the coding be more organized.

### ActualPlayer
A superclass is created for the user, the computer  level and computer Pro level.

#### Properties
- **tag** the symbol to use to represent the player X or 0.

#### Methods
- **get_moves**  Method to choose a move based on a game's board.

### NoobComputerPlayer
A computer player is the computer in easy mode, it is an extension of the ActualPlayer class.
 
#### Properties
- **tag** The symbol to represent the player, set to 'O' when the game is initialized.
 
#### Methods
- **get_moves** For the easy game mode, the computer looks at the game's available moves and randomly chooses one.

### RealPlayer
A Real Player represents the human player. It is an extension of the ActualPlayer class.
 
#### Properties
- **tag** The symbol to represent the human player, set to 'X' when the game is initialized.
 
#### Methods
- **get_moves** Allows a user to select an available move on the board by numerical association. It handles invalid inputs until the human complies..

### ProComputerPlayer
When the user selects hard for the difficulty level, they play against the ProComputerPlayer which is an extension of the ActualPlayer class.
 
#### Properties
- **tag** The symbol to represent the player, set to 'O' when the game is initialized.

#### Methods
- **get_moves** In the hard game mode, the computer looks at the available moves in the game and strategically chooses corners to prevent the human player from winning. All games end in a win or a draw for the computer.

- **minimax** Tracks positions and game scores in dictionaries. Uses an algorithm to simulate a game after the last move. Update the position and score dictionary.

### Tic Tac Toe
A game of tic tac toe

#### Properties
- **board** an array of 9 entries representing positions.
- **current_winner** keeps track of whether a player has won the game or not.
- **computer** player representing the computer.
- **player** player representing the human user.

#### Methods
- **print_board(self)** Prints the board on the terminal.
- **print_board_nums()** Prints the numbers corresponding to the empty squares on which the user will make a move.
- **available_moves(self)** Appends an index to an empty list IF the spot is empty, and confirms the move if the spot is empty.
- **available_moves_display(self)** Creates a 9 digit array of blanks for executed moves, making it easy to print out what moves the user can make next to the board.
- **empty_squares(self)** Returns/tracks all empty squares during the game.
- **make_move(self, square, character)** Places the user's and the computer's  according to the given index. If the index is an empty square, return True and the move is executed. If the index is occupied, return False and invalidate the move.
- **winner(self, square, character)** Checks if the previous move was a winning move. If so, return True and end the game. Otherwise, return False and continue the game.

## Libraries used
- Colorama: used to color the game throughout.
- Pyfiglet: used to print out a ASCII welcome format to the user.
- Random: used to randomize the computer's moves in the"easy" mode and the first move the genius computer makes.
- Math: used to code the minimax algorithm to make the genius computer player.
- Time: used the sleep() function between messages to the user to allow time for reading.

## Testing

### Manual Testing

- Manual testing sheet [here](https://docs.google.com/spreadsheets/d/1fMe3BTr-Y4Ad66SLm8-v50p5OfLmdcYoYzU7DUQ-fQU/edit#gid=296578096).

### Defect Tracking

- Git hub issues [here](https://github.com/MRWaelGhandoura/tic-tac-toe/issues).

### Validation Testing

- [PEP8 Validator](http://pep8online.com/)


- For the run.py
 
 ![image](https://user-images.githubusercontent.com/99558735/168196722-0373034b-a160-47f4-8cae-6eb3cb8cfb65.png)
 
 - For the players.py
  
  ![image](https://user-images.githubusercontent.com/99558735/168196814-12f3c760-7866-4440-8b9c-8f2e9ed83128.png)




## Deployment


### Heroku
- 1) Head to [Heroku](https://heroku.com) and create an account.
- 2) Click on "Create New App".
- 3) Name your app, select your region and click on "Create app".

  ![image](https://user-images.githubusercontent.com/99558735/168227066-bdaf5b5a-f529-413d-bc44-2787b19694c2.png)

- 4) On your app's dashboard bar, click on "Settings" and then click on "Reveal Config Vars".

 ![image](https://user-images.githubusercontent.com/99558735/168227384-23005727-2123-464c-885f-0f8543db6377.png)
 
- 5) Enter a key with the value of "PORT" and a value with the value of "8000", then click on "Add".
 
 ![image](https://user-images.githubusercontent.com/99558735/168227540-9534f5fc-9a80-4ea7-8d31-4b859ed75e4b.png)
 
 
- 6) Scroll down and click on "Add buildpack", select "python" and "Save changes".
- 7) Repeat step 6 and select "nodejs" instead of "python" (they should be added in that order, python first and nodejs after).

<img width="830" alt="deployment4" src="https://user-images.githubusercontent.com/82375381/132575097-06258f70-6951-44da-9573-3c9523c839c6.png">

 - 8) Manual deploy to Heroku 

 ![image](https://user-images.githubusercontent.com/99558735/168186379-c6e5bc87-e566-4db6-a2be-9147157be06c.png)
 
 ![image](https://user-images.githubusercontent.com/99558735/168186433-02d15074-ee62-468c-9c24-1426828153b6.png)
 
 ![image](https://user-images.githubusercontent.com/99558735/168186467-a06cc6b5-7109-4492-8b5f-5afd0e1829e5.png)


## Credits

### Code Institute
- - [Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.

### GitHub

- https://github.com/gabriel-alves-p
    - Help with his ogranized Readme.md .

### Tutorials

- https://www.youtube.com/watch?v=dK6gJw4-NCo&list=PLAA3uifegEK98UkLE614yowsG7OHfANz9&index=2
- https://www.youtube.com/watch?v=8ext9G7xspg
- https://www.youtube.com/watch?v=n2o8ckO-lfk&list=PLAA3uifegEK98UkLE614yowsG7OHfANz9&index=1&t=663s
- https://www.youtube.com/watch?v=M3G1ZgOMFxo&t=549s
- https://www.youtube.com/watch?v=trKjYdBASyQ&t=56s

### Acknowledgments

Thanks to the help and support of:

- My Code Institute mentor Malia Havlicek, who explained all the problems I faced while creating this project and helped me solve them in a professional way.
- The community on Slack, who helped me connect with Heroku.
- Code Institute, which taught me all those challenging and wonderful methods to become an excellent programmer.
