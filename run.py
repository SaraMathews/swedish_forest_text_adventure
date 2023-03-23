import time

from colorama import Fore, Back, Style

def play_game():
    """
    Starts the adventure game with a welcome message.
    Lets the player choose a character name.
    Introduces the conditions before displaying the first question.
    """

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