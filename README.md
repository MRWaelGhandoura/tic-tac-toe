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

- You will find my manual testing sheet [here](https://docs.google.com/spreadsheets/d/1fMe3BTr-Y4Ad66SLm8-v50p5OfLmdcYoYzU7DUQ-fQU/edit#gid=296578096).


### Validation Testing

- [PEP8 Validator](http://pep8online.com/)


- For the run.py
 
 ![image](https://user-images.githubusercontent.com/99558735/168196722-0373034b-a160-47f4-8cae-6eb3cb8cfb65.png)
 
 - For the players.py
  
  ![image](https://user-images.githubusercontent.com/99558735/168196814-12f3c760-7866-4440-8b9c-8f2e9ed83128.png)

Note any errors or warnings you are ignoring and why. IT IS BEST NOT to have ERRORS, but NINJA, COLOR VARIABLES sometimes are ok to ignore if you say the IDE that has the correct linters noted no errors. Or you can take the rendered HTML and run it through the HTML validator for the Flask html templates.

If the line is too long just add 
```$python 
# noqa
```
There is a space before the # and after it to skip the quality assurance for that line.

### Manual Testing

You can track your test in various ways.  

But for any scenarios that have not been automated, test the user stories manually and provide as much detail as is relevant. 

1. Markdown
>  A particularly useful form for describing your testing process is via scenarios, such as:
> 
>  **Register Page**
>  Go to the Register page: http://<YOUR APPP>.herokuapp.com/register
>    - [x] Try to submit the empty form and verify that an error message about the required fields appears
>    - [x] Try to submit the form with an invalid username format and verify that a relevant error message appears
>    - [x] Try to submit the form with an invalid password format and verify that a relevant error message appears
>    - [x] Try to submit the form with an existing username, should re-render page with relevant error message/warning
>    - [x] Try to submit the form with all inputs valid and verify that a success message appears and user is on profile page
>    - [x] Be logged in and go to register page url http://<YOUR APPP>.herokuapp.com/register, should have error saying you are already registered and be on profile page

2. Spreadsheet    
> Here is a [Manual Testing Template](https://docs.google.com/spreadsheets/d/189VpSeEG9oevSRhvb2WZl8zCk9L3s2iWQyrJ_1jjAGQ/edit?usp=sharing) that you can use as a starting point to keep track of your testing efforts. Make a copy of it in your own account and update as needed to reflect the browsers you are testing and features.  

3. GitHub Issues, Milestones & Boards
> You can also use agile tools in github to help track your testing and defects. Here's a document that I put together about that [process](https://docs.google.com/document/d/1nDS5tZeMO77Dfq85IZGMSV6C41XaPm9FwcpR3k-UTVc/edit?usp=sharing)
> 
> For more information you can visit: https://docs.github.com/en/issues/organizing-your-work-with-project-boards/managing-project-boards/about-project-boards 

It's ok to spot check specific functionality across devices and browsers but each page should be viewed as a whole for each device/browser combo at least once.

### Defect Tracking

You can use git hub issues to track any bugs rather than a spread sheet and just link to that page for your repository.

![image](https://user-images.githubusercontent.com/23039742/130149053-bf506388-a791-426e-8ffc-a56c1212e01c.png)

You should created issues in real time and close them out as you fix the bugs. Include steps to recreate and screenshots.

Create a link to the issues dashboard  of your repository
[ci_insights isssues](https://github.com/maliahavlicek/ci_mentor_insights/issues)

### Defects of Note
Some defects are more pesky than others. Highlight 3-5 of the bugs that drove you the most nuts and how you finally ended up resolving them.


### Outstanding Defects
It's ok to not resolve all the defects you found. If you know of something that isn't quite right, list it out and explain why you chose not to resolve it.

### Commenting Code

Make sure you  use triple double quotes to document fuctions and classes.
 Here'a  documentation worthy example:
```$python
def yes_no(question):
    """
    Function to ask a simple yes no question of the user.
    :param question: String displayed as the question
    :return: answer: String equal to "1" or "2" representing yes or no respectfully
    """
    print(question)
    print("yes = 1")
    print("no = 2")
    answer = input("enter your answer here \n").strip()
    while answer not in ("1", "2"):
        print("please choose 1 for yes and 2 for no")
        answer = input("enter your answer here \n").strip()
    return answer

```

## Deployment

### Requirements
If the user is required to have certain keys and credentials you should include this section with diretions on how to get the necessary information.
ex)
1. **Google Account:** In order to have this program work, you need a google account. If you don't have one  [Create a google account](https://accounts.google.com/Signup)
2. **Google APIs**
    1. in a new incognito tab, log into your new google account.
    1. then update the url to be: https://console.cloud.google.com/getting-started?pli=1 
        
        **GOOGLE DRIVE API Access**
        1.  create a new project for this, call it XXXXXX (You might want to refer to what you see in this video: https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/071036790a5642f9a6f004f9888b6a45/ at the bottom of the screen to write out steps.)
        2. Then click on Add APIs and Services and select Libraries
        3. Search for Google Drive
        4. Click Enable
        5. Click Create Credentials
        6. Select Google Drive API from the drop down, Application Data, then no and click the Next Button
        7.  (https://developers.google.com/drive/api/v3/enable-drive-api) 
        8. for service account details fill in a service account name ex) xxx_API, then click Create and Continue
        9. For the Accoun acces, select Role: Basic/Editor then continue
        10. Then Click Done
        11. Now select the newly created service account
        12. Click on the KEYS Tab
        13. Click Add Key
        14. Select JSON type (right click to show in folder so you know where the file was saved.
        
        **GOOGLE SHEETS API Access**
        You may need to us the back button get to the APIS & SErvices section from where you were.
        1. click the Libray  Tab and serarch for Google Sheets
        2. click enable

3. The downloaded credentialsJSON file is basically your creds.json file that you need to put into your heroku settings or gitpod environment to access your google drive.

4. Google Sheet Template
  - If you had to create specific sheets for your project, instruct users to make their own copy of it from yours and rename it back to what the python project expects
  - And don't forget to share the spreadsheet in question with the client_email from the creds.json 
### Gitpod
This section should describe the process someone would have to go through to get the local working in gitpod.  Such as install requirements.txt  and setting up a creds.json file that is in the gitignore and keeping their workspace.

If you have project settings required such as a creds.json file from the GOOGLE DRIVE API acess, please provide an example of that file in the writeup with the project key values:
```$python
{
    "type": "service_account",
    "project_id": "<YOUR_VALUE>",
    "private_key_id": "<YOUR_VALUE>",
    "private_key": "<YOUR_VALUE>",
    "client_email": "<YOUR_VALUE>",
    "client_id": "<YOUR_VALUE>",
    "auth_uri": "https://accoutns.google.com/0/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cer_url": "https://www.googleapis.com/oauth2/v1/certs",
    "clien_x509_cert_url": "<YOUR_VALUE>"
}
```

If you have any dependencies, you should instruct users to install them
```$python
pip3 install -r requirements.txt
```



### Heroku
This section should describe the process you went through to deploy the project to Heroku. Include screenshots if you think they would make the process easier.

You may want to re-watch the [python essentials deployment video](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/e3b664e16366444c8d722c5d8340b340/?child=first) when writing up this section.


If you have project settings required for Heroku, provide a table of the keys and values.
Do not share your personal keys but either cut them out of the screen shot or say <YOUR_VALUE> and include links on how the user would obtain such values.

#### Fork the repository
Make a fork so you have a copy of the repository in your own git hub account: https://github.com/maliahavlicek/portfolio_project_03

![image](https://user-images.githubusercontent.com/23039742/132136504-eb79a6f3-0205-4c82-80c2-eef136ec7e4c.png)
  
![image](https://user-images.githubusercontent.com/99558735/168186379-c6e5bc87-e566-4db6-a2be-9147157be06c.png)
![image](https://user-images.githubusercontent.com/99558735/168186433-02d15074-ee62-468c-9c24-1426828153b6.png)
  ![image](https://user-images.githubusercontent.com/99558735/168186467-a06cc6b5-7109-4492-8b5f-5afd0e1829e5.png)




#### New Project
Log into Heroku and create a new project. Name it something like XXX_coders_bistro.


#### Settings
On the settings tab you have to address two things:
1. **Config Vars**

  ![image](https://user-images.githubusercontent.com/23039742/132135869-215d2e0f-805d-40a8-a8c2-fb1098e2645d.png)

  At a bar minimum you should show the user that they need to add the PORT. 8000 key value pair.


2. **Build Packs**

  ![image](https://user-images.githubusercontent.com/23039742/132135918-28cac112-7766-4277-905c-4a4963d8442d.png)

  add Python Then Node.js


#### Deploy
1. Set up to github and select the correct repository:

  ![image](https://user-images.githubusercontent.com/23039742/132136113-c257c921-d10c-4ccc-af09-6a1d25136395.png)

2. Deploy either manual or automatic

![image](https://user-images.githubusercontent.com/23039742/132136241-9d76fabb-39f0-4696-bc5f-047398fdaf41.png) 



## Credits

To avoid plagiarism amd copyright infringement, you should mention any other projects, stackoverflow, videos, blogs, etc that you used to gather imagery or ideas for your code even if you used it as a starting point and modified things. Giving credit to other people's efforts and ideas that saved you time acknowledges the hard work others did. 

-[Code Institute Template](https://github.com/Code-Institute-Org/python-essentials-template)
    - The Template for the GUI for this project was provided by Code Institute. This allows for the Command line to be shown and used within the browser.

### Content

Use bullet points to list out sites you copied text from and cross-reference where those show up on your site

### Media

Make a list of sites you used images from. If you used several sites try to match up each image to the correct site. This includes attribution for icons if they came from font awesome or other sites, give them credit.

### Acknowledgments

This is the section where you refer to code examples, mentors, blogs, stack overflow answers and videos that helped you accomplish your end project. Even if it's an idea that you updated you should note the site and why it was important to your completed project.

If you used a CodeInstitute Instructional project as a starting point. Make note of that here too.

