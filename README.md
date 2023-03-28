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
