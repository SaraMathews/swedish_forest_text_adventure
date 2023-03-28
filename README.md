# **Swedish Forest Text Adventure Game**
## **Description**
### *Game ruless*
### *Flow chart*
## **Features**
## **Testing**
### *Unfixed bugs*
## **Deployment**
### *Version Control*
The git commands below were used throughout development to push code to the remote repository in GitHub:
- `git add .` - This command was used to add a change in the working directory to the staging area
- `git commit -m "message"` -This command was used to save changes to the local repository. A brief description of what has changed and when
- `git push` - This command was used to push all commits to the remote repository on GitHub
### *Deploy to Heroku*
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
## **Credits**
- Code Institute LMS
- Slack
- My mentor Daisy McGirr
- https://pypi.org/project/colorama/
- The text adventure game is in some parts inspired by Lord of The Rings
- All three riddles is taken from "The Hobbit: An Unexpected Journey"

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