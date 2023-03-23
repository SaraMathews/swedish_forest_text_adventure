import time

from colorama import Fore, Style

global axe 
axe = "no"

riddles = {
        "First riddle": {
            "riddle": "This thing all things devours;\n"
                      "Birds, beasts, trees, flowers;\n"
                      "Gnaws iron, bites steel;\n"
                      "Grinds hard stones to meal;\n"
                      "Slays king, ruins town,\n"
                      "And beats mountain down.\n",
            "answers": ["time", "wind"]
        },
        "Second riddle": {
            "riddle": "It cannot be seen, cannot be felt,\n"
                      "Cannot be heard, cannot be smelt.\n"
                      "It lies behind stars and under hills,\n"
                      "And empty holes it fills.\n"
                      "It comes out first and follows after,\n"
                      "Ends life, kills laughter.\n",
            "answers": ["dark", "shadow"]
        }
    }


def play_game():
    """
    Starts the adventure game with a welcome message.
    Lets the player choose a character name.
    Asks the player if they are ready to play the game.
    Displays indtroduction before the first question.
    """
    print("\nThis is the Swedish Forest Text Adventure Game\n")
    time.sleep(1)

    # Character name must be chosen before continuing
    print("Welcome brave adventurer!\n")
    time.sleep(1)
    character_names = ["Bjorn", "Ragnar", "Hilda"]
    name = input(
        "Choose one of the following "
        f"character names: {', '.join(character_names)}: "
                )
    while name not in character_names:
        print("\nThat's not one of the options. Please try again\n")
        name = input(
            "Choose one of the following "
            f"character names: {','.join(character_names)}:"
            )
    time.sleep(1)

    # Asks the player if they are ready. They must enter yes or no
    are_you_ready = input(
        "\nAre you ready to enter the deep, "
        f"dark Swedish forest, {name}? (yes or no): "
        )
    time.sleep(1)
    while are_you_ready.lower() not in ["yes", "no"]:
        are_you_ready = input("\nHmm... was that a yes or a no? ")
        time.sleep(1)

    # If the player answers yes, the game continues with the introduction
    if are_you_ready.lower() == "yes":
        print("")
        print(f"Well then, {name}! Get ready...\n")
        time.sleep(1.5)
        print("You find yourself lost in the Swedish forest...")
        time.sleep(2)
        print("With no memory of how you got there...\n")
        time.sleep(2)
        print("The cold autumn wind sends shivers down your spine...")
        time.sleep(2)
        print("When you listen closely, you can hear the trees "
              "whispering to each other...\n")
        time.sleep(2)
        print("You can't stay here, you have to find a way out!\n")
        time.sleep(1.5)
        print("Or else.. who knows what's lurking in the dark...\n")
        time.sleep(2)
        print("Good luck, see you on the other side...hopfully.\n")
        print("--------------------------------------\n")
        time.sleep(2)
        first_question()

    # If the player answers no, 
    # the game over and restart game functions are called
    else: 
        print("\nIt's game over before it even begins!\n")
        game_over()
        time.sleep(1)
        restart_game()
        

def first_question():
    """
    Presents the player with the first question,
    to either cross the stream or follow the stream.
    Depedning on the answer the player eiter continues to
    second_question, or it's game over.
    """
    print("You try to stand up...")
    time.sleep(1.5)
    print("Your head is spinning.")
    time.sleep(1.5)
    print("But you need to get going.\n")
    time.sleep(1.5)
    print("You stumble through the forest until you reach a small stream.")
    time.sleep(1.5)
    print("It looks calm.\n")
    time.sleep(1.5)
    
    # Displays the question and answers
    print("Do you:")
    time.sleep(1.5)
    print("a) Follow the stream until you find a safer way to cross it")
    time.sleep(1.5)
    print("b) Cross the stream and hope it is as calm as it looks \n")
    time.sleep(1.5)

    while True:
        your_answer = input("What do you do? (a or b): ")
        print("\n--------------------------------------")

        # If the player answers "a" the loop breaks and they continue
        # to second_question
        if your_answer.lower() == "a":
            time.sleep(1.5)
            second_question()
            break

        # If the player answers "b" the loop breaks and it's game over
        elif your_answer.lower() == "b":
            print("\nYou attempt to cross the stream.\n")
            time.sleep(1.5)
            print("But oh no! Quicksand!\n")
            time.sleep(1.5)
            print("It drags you down and you drown.\n")
            time.sleep(1.5)
            game_over()
            time.sleep(1.5)
            restart_game()
            time.sleep(1.5)
            break

        # If the player answers neither a or b they are promped to answer
        # the question again
        else:
            print("Invalid choice. Please enter a or b.")
            continue


def second_question():
    """
    Presents the player with the second question,
    to either approach the group of people or stay away from them.
    Depedning on the answer the player eiter continues to
    first_riddle, or it's game over.
    """
    print("\nYou follow the stream. After a while it narrows down enough "
          "for you to jump over.\n")
    time.sleep(1.5)
    print("When you have landed on the other side of the stream,")
    print("you find a log to sit on. You need to catch your breath.\n")
    time.sleep(1.5)
    print("But what's that sound?\n")
    time.sleep(1.5)
    print("People! You can hear a faint laugther coming from inside the "
          "forest")
    time.sleep(1.5)
    print("You now notice a bonfire in the distance. "
          "Maybe they can help you?\n")
    time.sleep(1.5)

    # Displays the question and answers
    while True:
        print("Do you:")
        time.sleep(1.5)
        print("a) Approach the group of people and ask for directions out of "
              "the forest")
        time.sleep(1.5)
        print("b) Stay away from them. You don't know who these people are\n")
        time.sleep(1.5)
        your_answer = input("What do you do? (a or b): ")
        print("\n--------------------------------------")

        # If the player answers "a" the loop breaks and they continue
        # to first_riddle
        if your_answer.lower() == "b":
            time.sleep(1.5)
            third_question()
            break

        # If the player answers "b" the loop breaks and it's game over
        elif your_answer.lower() == "a":
            print("\nYou approach the group of people.\n")
            time.sleep(1.5)
            print("But you realise now... they are not people..they are...\n")
            time.sleep(1.5)
            print("TROLLS!\n")
            print("      ▴▴▴▴    ")
            print("   ☾=( ⚯ )=☽  ")
            print(r" /    \⎴ /   \ ")
            print(r" /|    •    |\      ⺣")
            print(r" \_\   •   /_/     ⺣ ")
            print(r"  |    /    |      ⺣ ⺣ ")
            print("   |   ()    |      /^\\")
            print(r"   \   \\\   /      //^\\")
            print(r"   mmm   mmm     ///^\\\\")
            print("")
            time.sleep(1.5)
            print("They are having a barbecue, and you just served them "
                  "dessert...\n")
            game_over()
            time.sleep(1.5)
            restart_game()
            time.sleep(1.5)
            break

        # If the player answers neither a or b they are promped to answer
        # the question again
        else:
            while True:
                print("Invalid choice. Please enter a or b.")
                your_answer = input("What do you do? (a or b): ")
                if your_answer.lower() == "a" or your_answer.lower() == "b":
                    break
            continue


def third_question():
    """
    Presents the player with the third question,
    to either take the axe or leave it.
    Depedning on if the player answers yes or no, different print
    messages are displayed. Both answers leads to first_riddle
    """
    print("\nGood choice! Trust no one.\n")
    time.sleep(2)
    print("It feels like you've been walking for hours")
    time.sleep(1.5)
    print("It's still dark, but the full moon lights up your way\n")
    time.sleep(1.5)
    print("Suddenly, you trip over something..\n")
    time.sleep(1.5)
    print("It's an axe!\n")
    time.sleep(1.5)
    print("Why is there an axe lying around in the middle of the forest..?\n")
    time.sleep(2)
    print("And who does it belongs to...?\n")
    time.sleep(1.5)

    # Displays the third question. Both answers leads to first_riddle
    while True:
        global axe
        axe = input("Do you take the axe with you? (yes or no): ")
        if axe == "yes":
            time.sleep(1.5)
            print("\nThat's probably a smart move, considering what "
                  "might be out there..\n")
            first_riddle()
            break
        elif axe == "no":
            time.sleep(1.5)
            print("\nThat's probably a smart move, the owner of the axe will "
                  "not be happy when he notices it's gone...\n")
            first_riddle()
            break
        else: 
            print("Invalid choice. Please enter yes or no.\n")
            time.sleep(1)
            continue


def first_riddle():
    """
    Presents the player with the first riddle.
    Depedning on the answer the player eiter continues to
    second_riddle, or it's game over.
    """
    print("You're thirsty...and tired.")
    print("After a while you decide you need a rest")
    print("And look over there!")
    print("A small lake")
    print("You spash your face with water and have a drink")
    print("You don't notice the creature Gollum sneaking up behind you..")
    print("################")
    print("#              #")
    print("#     BOOO     #")
    print("#              #")
    print("################")
    print("Gollum won't let you go until you've answered both of his riddles\n")
    print("But he's in a good mood today..")
    print("He just found his missing gold ring\n")
    print("So he's giving you a fair chance to answer his riddles")
    print("Think carefully... \n")
    while True:
        print(riddles["First riddle"]["riddle"])
        your_answer = input("What is it, time or wind?")

        if your_answer in riddles["First riddle"]["answers"][0]:
            print("Correct!")
            print("One riddle left...")
            second_riddle()
            break
        elif your_answer == riddles["First riddle"]["answers"][1]:
            print("Wrong answer...")
            game_over()
            restart_game()
            break
        else: 
            print("Invalid answer. Please choose between time or wind.\n")
            time.sleep(1)
            continue


def second_riddle():
    """
    Presents the player with the second riddle.
    Depedning on the answer the player eiter continues to
    third_question, or it's game over.
    """


def final_question():
    """
    Presents the player with the final question.
    The player now has three options:
    Fight the giant, talk to the giant, or sneak past the giant.
    Depedning on the answer it's either game over,
    game finished (player made it out of the forest)
    or player is taken back to first_riddle.
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
        print("\n--------------------------------------")
        time.sleep(1.5)
        play_game()
    else:
        time.sleep(1)
        print("")
        print("Bye then!")
        print("        /\\_/\\   ")
        print("  ____/ o o  \\  ")
        print("  /~____   \"  ) ")
        print("(_____\/    / \n") 
        exit()


play_game()
