# **Swedish Forest Text Adventure Game**
## **Description**
The game is a text-based adventure game where the player is tasked with answering questions and riddles to progress through the game. The player will encounter various scenarios and meet different creatures. The end goal is to make it out of the forest.  

![Description](docs/text_adventure.png)
### *How to play*
The game begins with an introduction where the player is given some background information about the game and the quest they are embarking on. The player is then presented with a series of questions and riddles that they must answer correctly to progress in the game. If they choose the correct answer, they move on to the next question/riddle. If they choose the wrong answer, they lose the game and can choose to start over. The player can also choose to exit the game at any time by answering "exit" on the questions/riddles.

In addition, the game keeps track of whether the player has picked up an axe. In the final question (when the player encounters a dwarf) the outcomes differs depending on if the player picked up the axe or not. This question follows a different procedure than the previous ones. The player will not lose if they answer wrong, but they will be taken back to the lake where they must answer another riddle. If they answer the riddle correctly, another final question is displayed, where the "random" factor has been implemented to give the game a twist.

## *Flow chart*
The flow chart was created to provide a clear visual representation of how I wanted the game to progress based on the player's answers. It helped me design the game and its functions more effectively, without getting lost in the code. I have revised the flow chart a few times as new ideas and functions were added to the game.

![Flow chart](docs/text%20_adventure.jpeg)

## **Features**
### *Choose character name*
 Lets the player choose their character's name before the game begins. The function starts with instructions on how to play the game. If the player chooses a valid name, the game proceeds to the next function. If the player types an invalid name, they are prompted to choose a name again until they choose a valid one.

 ![Choose character name](docs/choose_name.png)
### *Are you ready?*
Asks the player if they are ready to play the game and displays an introduction if they answer yes. If they answer no, the game ends. 
If the player answers an invalid answer, they are prompted to enter yes or no. 

![Are you ready](docs/are_you_ready.png)
### *Exit game early*
This function is called if the player chooses to exit the game at any stage by answering "exit" on the question/riddle. It prints a goodbye message that includes the characters' name. The "sys.exit()" command is used to immediately terminate the game. 

![Exit game](docs/exit_game.png)
### *Choose answer*
The player is always presented with two answer options to choose from (except in the function second_final_question). 
They select their answer by typing it in the console, and the game then evaluates their response and proceeds accordingly. 
In the second final question, the player has to enter "flip" to flip the coin and continue the game.

![Choose answer](docs/choose_answer.png)
### *Improve chance of victory*
The third question function gives the player the option to pick up an axe.
This can either improve their chances of victory or not, depending on what they choose. 
The function displays different messages depending on if the player picks up the axe or not, but both answeres lead to the first riddle function.

![Improve chance of victory](docs/improve_chances.png)
### *Correct answer declaration*
Whenever the player answers correctly, the game will either acknowledge that it was the correct answer or continue the story, indicating to the player that they are making progress.

![Correct answer](docs/correct_answer.png)
### *Wrong answer declaration*
Whenever the player answers wrong, the game will acknowledge that it was the wrong answer by displaying a message suitable for the answer to the question/riddle. 

![Wrong answer](docs/wrong_answer.png)
### *Game over message*
The game over message will display after the wrong answer declaration and will let the player know its game over. 

![Game over](docs/game_over.png)
### *Restart game message*
After displaying the "Game Over" message the player is asked to choose whether they want to restart the game or not. If they choose "yes", the game restarts from the beginning. If they choose "no", the "exit game" message is displayed before the game is terminated. 

![Restart](docs/restart.png)

### *Features left to implement*
I would add a feature that allows the player to choose the desired speed at which the game runs. 

## **Testing**
### *Validator testing*
![test_validator](docs/test_validation.png)

### *Functional testing*
Below, I have summarized the testing in screenshots of several Excel sheets for easier overview. I have separated the sheets into the following categories:
- Function testing introduction. <br>
    Includes the function choose_name() and are_you_ready() <br>

- Function testing questions. <br>
    Includes the function first_question()second_question and third_question(axe) <br>

- Function testing riddles.<br>
    Includes the function first_riddle(axe), second_riddle(axe), and third_riddle()<br>

- Function testing final questions.<br>
    Includes the function final_question() and second_final_question()<br>

- Function testing other.<br>
    Includes the function game_over(),
    restart_game() and exit_game 

In this test, I also ensured that all the print messages were correct and displayed in the appropriate order.

**Function testing introduction**
![test_intro](docs/test_intro.png)

**Function testing questions**
![test_questions](docs/test_questions.png)

**Function testing riddles**
![test_riddles](docs/test_riddles.png)

**Function testing final questions**


**Function testing other**
![test_other](docs/test_other.png)


### *Unfixed bugs*
I have not noticed any bugs that would affect the game, but it's still possible that there are minor bugs present that I have yet to discover. If that's the case, these minor bugs do not appear to impact the gameplay experience.

I have however, encountered one warning messages. 
This one is beacuse I'm using a global variable:
- global CHARACTER_NAME : Using the global statement at the module levelpylint(global-at-module-level)

This one is beacuse I have to many statements. I did not have time to correct this.  
- def final_question(axe): Too many statements (65/50)pylint(too-many-statements)

### *Other commentss*
A few people in my family tested the game to see if they could spot any bugs, and also to provide feedback. One of the comments I received was that the game's pace was too fast, so I made adjustments to slow it down. <br>

When I decided to create an axe variable that changes value based on player input, I initially made it a global variable for easy access throughout the game. However, as taught in the LMS, global variables should be avoided if possible. So i decided to change it, and instead pass the axe down as arguments in functions.  
I encountered bugs and errors due to having to pass the axe argument down through the code, which took time to resolve. Although I eventually made it work, it would have been easier to understand and avoid potential bugs if I had continued using the global variable, at least for me as a new coder. If I had more time, I would consider changing it back to a global variable, but since the game is functioning as intended, I don't want to risk disrupting the code just hours before the deadline.

## **Technologies**
- The game was developed using Python.
- All content was stored on GitHub.
- The game was deployed to the web using Heroku.
- The flowchart was made using LucidChart.
- Python module time was used to add a delay between pieces of code.
- Python module sys was used in the exit_game() function.
- Python module colorama was used to add colours and styles. 

## **Deployment**
### *Version Control*
The git commands below were used throughout development to push code to the remote repository in GitHub:
- `git add .` - This command was used to add a change in the working directory to the staging area.
- `git commit -m "message"` -This command was used to save changes to the local repository. A brief description of what has changed and when.
- `git push` - This command was used to push all commits to the remote repository on GitHub.
### *Deploy to Heroku*
The steps below were followed to deploy the app to Heroku:
- Open the Heroku website and select "New" to create a new app. 
- After choosing a name for the new app, and selecting the correct region, click on "Create app". 
- Navigate to "Settings" and go to the Config Vars section. Add a Config Var with the keyword "PORT" and 
value of "8000". 
- Still in "Settings", go to Buildpacks and add the buildpacks for Python and NodeJS, in that order. 
- Navigate to the top menu and go to "Deploy". Scroll down and set the Deployment Method to "Github". 
Once Github is selected, locate your repository and link it to Heroku. 
- Scroll down to Manual Deploy, ensure that the "main" branch is selected, and click "Deploy Branch".
- You will see the text "Your app was successfully deployed.". Click the button "View" to open the link to your
deployed app. 
### *Clone the Repository from GitHub*
The steps below were followed to clone the repository locally: 
- Navigate to the main page of the GitHub Repository you want to clone. 
- Above the list of files, click on the drop-down button "<>Code".
- Copy the repository link. 
- Open Terminal, type git clone followed by the copied URL, and press enter to create your local clone.

## **Credits**
- Code Institute LMS
- Slack
- My mentor Daisy McGirr
- https://pypi.org/project/colorama/
- The text adventure game is in some parts inspired by Lord of The Rings.
- All three riddles is taken from "The Hobbit: An Unexpected Journey".

Inspiration was taken from 
- https://www.askpython.com/python/text-based-adventure-game
- https://www.thecoderpedia.com/blog/text-based-adventure-game-in-python/
- https://www.youtube.com/watch?v=u8X6TiJA8as
- https://github.com/OlgaJ1989/text_adventure/blob/main/run.py


Help and guidance when I encountered problems I didn't know how to solve myself
- https://www.w3schools.com/python/ 
- https://stackoverflow.com/questions/2070684/how-can-i-make-my-python-code-stay-under-80-characters-a-line
- https://stackoverflow.com/questions/15435811/what-is-pep8s-e128-continuation-line-under-indented-for-visual-indent
- https://www.programiz.com/python-programming/break-continue
- https://stackoverflow.com/questions/33466860/expected-two-blank-lines-pep8-warning-in-python
- https://pythonprogramminglanguage.com/try-except/