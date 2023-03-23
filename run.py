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
    name = input(f"Choose one of the following character names:{','.join(character_names)}:")
    while name not in character_names:
        print("That's not one of the options. Please try again")
        name = input(f"Choose one of the following character names: {','.join(character_names)}:")
    
    # Asks the player if they are ready. They must enter yes or no
    are_you_ready = input(f"Are you ready to enter the deep, dark Swedish forest, {name}? (yes/no):")
    while are_you_ready.lower() not in ["yes", "no"]:
        are_you_ready = input("Hmm... was that a yes or a no?")

    if are_you_ready.lower() == "yes":
        print(f"Well then, {name}! Get ready...")
        print("You find yourself lost in the Swedish forest...")
        print("With no memory of how you got there...")
        print("The cold autumn wind sends shivers down your spine...")
        print("When you listen closely, you can hear the trees" 
              "whispering to each other...")
        print("You can't stay here, you have to find a way out!")
        print("Or else.. who knows what's lurking in the dark...")
        print("Good luck, see you on the other side...hopfully.")
        first_question()
    else: 
        print("It's game over before it even begins!")
        game_over()
        restart_game()


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

def game_over():
    """
    Is called every time the player answers a question/riddle wrong. 
    Displays a Game Over box before the restart_game function
    """
    print(Fore.RED + " ######################")
    print(Fore.RED + " #                    #")
    print(Fore.RED + " #      GAME OVER     #")
    print(Fore.RED + " #                    #")
    print(Fore.RED + " ######################")
    print(Style.RESET_ALL)

def restart_game():
    """
    Is called every time the player answers a question/riddle wrong. 
    Lets the player choose to either restart the game or exit.  
    """
    restart_game = input("Do you want to restart the game? (yes or no): ")
    while restart_game.lower() not in ["yes", "no"]:
        print("Please enter either 'yes' or 'no'.")
        restart_game = input("Do you want to restart the game? (yes or no): \n")
    if restart_game.lower() == "yes":
        play_game()
    else:
        print("")
        print("Bye then!")
        print("        /\\_/\\   ")
        print("  ____/ o o  \\  ")
        print("  /~____   \"  ) ")
        print("(_____\/    / \n") 
        exit()


play_game()
game_over()
restart_game()