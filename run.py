import time

from colorama import Fore, Back, Style

def play_game():
    """
    Starts the adventure game with a welcome message.
    Lets the player choose a character name.
    Asks the player if they are ready to play the game.
    Introduces the conditions before displaying the first question.
    """
    print("This is the Swedish Forest Text Adventure Game")

    # Character name must be chosen before continuing 
    print("Welcome brave adventurer!")
    character_names = ["Bjorn", "Ragnar", "Hilda"]
    name = input(f"Choose one of the following character names: {','.join(character_names)}:")
    while name not in character_names:
        print("That's not one of the options. Please try again")
        name = input(f"Choose one of the following character names: {','.join(character_names)}:")
    
    # Asks the player if they are ready. They must enter yes or no
    are_you_ready = input(f"Are you ready to enter the deep, dark Swedish forest, {name}? (yes/no):")
    while are_you_ready.lower() not in ["yes", "no"]:
        are_you_ready = input("Hmm... was that a yes or a no?")

def first_question():
    """
    Presents the player with the first question, 
    to either cross the stream or follow the stream.
    Depedning on the answer the player eiter continues to 
    second_question, or it's game over.
    """

def second_question():
    """
    Presents the player with the second question, 
    to either approach the group of people or stay away from them. 
    Depedning on the answer the player eiter continues to 
    first_riddle, or it's game over.
    """
def first_riddle():
     """
    Presents the player with the first riddle. 
    Depedning on the answer the player eiter continues to 
    second_riddle, or it's game over.
    """

def second_riddle():
     """
    Presents the player with the second riddle. 
    Depedning on the answer the player eiter continues to 
    third_question, or it's game over.
    """

def third_question():
    """
    Presents the player with the third question,
    to either trust the fairy or not.  
    Depedning on the answer the player eiter continues to 
    final_question, or it's game over.
    """

def final_question():
    """
    Presents the player with the final question. 
    The player now has three options: 
    Fight the giant, talk to the giant, or sneak past the giant. 
    Depedning on the answer it's either game over, 
    win (player made it out of the forest) or player is taken back to first_riddle. 
    """

def restart_game():
    """
    Is called every time the player answers a question/riddle wrong. 
    Displays a Game Over box and lets the player choose to either restart 
    the game or exit.  
    """

play_game()