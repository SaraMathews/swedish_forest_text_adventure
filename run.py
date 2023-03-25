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
            "answers": ["darkness", "shadow"]
        },
        "Third riddle": {
            "riddle": "A box without hinges, key, or lid,\n"
                      "Yet golden treasure inside is hid.\n",
            "answers": ["sun", "egg"]
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
        f"character names: {', '.join(character_names)}:\n"
                )
    while name not in character_names:
        print("\nThat's not one of the options. Please try again\n")
        name = input(
            "Choose one of the following "
            f"character names: {','.join(character_names)}: \n"
            )
    time.sleep(1)

    # Asks the player if they are ready. They must enter yes or no
    are_you_ready = input(
        "\nAre you ready to enter the deep, "
        f"dark Swedish forest, {name}? (yes or no):\n"
        )
    time.sleep(1)
    while are_you_ready.lower() not in ["yes", "no"]:
        are_you_ready = input("\nHmm... was that a yes or a no?\n")
        time.sleep(1)

    # If the player answers yes, the game continues with the introduction
    if are_you_ready.lower() == "yes":
        print("")
        print(f"Well then, {name}! Get ready.\n")
        time.sleep(1.5)
        print("You find yourself lost in the Swedish forest.")
        time.sleep(2)
        print("With no memory of how you got there.\n")
        time.sleep(2)
        print("The cold autumn wind sends shivers down your spine.")
        time.sleep(2)
        print("When you listen closely, you can hear the trees "
              "whispering to each other.\n")
        time.sleep(2)
        print("You can't stay here, you have to find a way out!\n")
        time.sleep(1.5)
        print("Or else.. who knows what's lurking in the dark.\n")
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
    print("You try to stand up.")
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
        your_answer = input("What do you do? (a or b):\n")
        time.sleep(1)
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
    time.sleep(2.5)
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
        your_answer = input("What do you do? (a or b):\n")
        time.sleep(1)
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
            print(r" /    \⎴ /  \ ")
            print(r" /|    •    |\      ⺣")
            print(r" \_\   •   /_/     ⺣ ")
            print(r"  |    /    |      ⺣ ⺣ ")
            print(r"   |   ()   |      /^\\")
            print(r"   \   \\\  /     //^\\")
            print(r"   mmm   mmm     ///^\\\\")
            print("")
            time.sleep(1.5)
            print("They are having a barbecue, and you just served them "
                  "dessert.\n")
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
                your_answer = input("What do you do? (a or b): \n")
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
    print("Suddenly, you trip over something.\n")
    time.sleep(1.5)
    print("It's an axe!\n")
    time.sleep(1.5)
    print("Why is there an axe lying around in the middle of the forest?\n")
    time.sleep(2)
    print("And who does it belongs to...?\n")
    time.sleep(1.5)

    # Displays the third question. Both answers leads to first_riddle
    while True:
        global axe
        axe = input("Do you take the axe with you? (yes or no): \n")
        time.sleep(1)
        print("\n--------------------------------------")
        if axe == "yes":
            time.sleep(1.5)
            print("\nThat's probably a smart move, considering what "
                  "might be out there.\n")
            time.sleep(1.5)
            first_riddle()
            break
        elif axe == "no":
            time.sleep(1.5)
            print("\nThat's probably a smart move, the owner of the axe will "
                  "not be happy when he notices it's gone.\n")
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
    print("You're thirsty and tired.")
    time.sleep(1.5)
    print("After a while you decide you need a rest. \n")
    time.sleep(1.5)
    print("You reach a small lake.")
    time.sleep(1.5)
    print("You spash your face with water and have a drink. \n")
    time.sleep(1.5)
    print("You don't notice the creature Gollum sneaking up behind you...\n")
    time.sleep(2)
    print("################")
    print("#              #")
    print("#     BOOO     #")
    print("#              #")
    print("################\n")
    time.sleep(2)
    print("Gollum won't let you go until you've played a game of riddles.\n")
    time.sleep(1.5)
    print("But he's in a good mood.")
    time.sleep(1.5)
    print("He just found his missing gold ring.\n")
    time.sleep(1.5)
    print("He's giving you a fair chance to answer his riddles.\n")
    time.sleep(1.5)
    print("So think carefully.\n")
    time.sleep(2)
    print(riddles["First riddle"]["riddle"])
    time.sleep(7)
    print("Choose between the following: " + riddles["First riddle"]["answers"][0] + " or " + riddles["First riddle"]["answers"][1])    
    time.sleep(3)  
    your_answer = input("What's your answer?")
    time.sleep(1)
    print("\n--------------------------------------\n")
    time.sleep(1.5)

    while True:

        if your_answer in riddles["First riddle"]["answers"][0]:
            print("Right answer.\n")
            time.sleep(1.5)
            print("Next riddle:\n")
            time.sleep(2)
            second_riddle()
            break
        elif your_answer == riddles["First riddle"]["answers"][1]:
            print("Wrong answer.")
            time.sleep(1.5)
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
    print(riddles["Second riddle"]["riddle"])
    time.sleep(7)
    print("Choose between the following: " + riddles["Second riddle"]["answers"][0] + " or " + riddles["Second riddle"]["answers"][1]) 
    time.sleep(3)
    your_answer = input("What's your answer?\n")
    time.sleep(1)
    print("\n--------------------------------------\n")
    time.sleep(1.5)

    while True:

        if your_answer in riddles["Second riddle"]["answers"][0]:
            print("Right answer.\n")
            time.sleep(1.5)
            print("You are vey good at riddles.\n")
            time.sleep(1.5)
            print("yess..yess my precious, very good..\n")
            time.sleep(1.5)
            print("Gollum lets you g.o")
            time.sleep(1.5)
            print("\n--------------------------------------\n")
            final_question()
            break
        elif your_answer == riddles["Second riddle"]["answers"][1]:
            print("Wrong answer.")
            time.sleep(1.5)
            game_over()
            restart_game()
            break
        else:
            print("Invalid answer. Please choose between darkness "
                  "or shadows\n")
            time.sleep(1)
            continue


def final_question():
    """
    Presents the player with the final question.
    The player now has three options.b
    Option a) is game over
    Option b) is victory, the player makes it out of the forest
    Option c) has two outcomes. Depending on if they picked up 
    the axe or not. If they picked up the axe, they are takem back to 
    Gollum to answer a third riddle. If they didn't pick up the axe it's
    victory the player makes it out of the forest
    """
    while True:
        your_answer = input("What do you do? (a, b or c): ")
        print("\n--------------------------------------\n")

        if your_answer.lower() == "b":
            time.sleep(1.5)
            print("You win!")
            restart_game()
            break

        elif your_answer.lower() == "c":
            game_over()
            time.sleep(1.5)
            restart_game()
            time.sleep(1.5)
            break
        
        elif your_answer.lower() == "a":
            if axe == "no":
                print("You win!")
                restart_game()
            else:
                if axe == "yes":
                    third_riddle()
            break

        else:
            print("Invalid choice. Please enter a, b or c.")
            continue


def third_riddle():
    """
    If the player answers a) on the final question and axe == yes,
    they will be presented with the third riddle.
    Depedning on the answer the player eiter continues to
    final_question, or it's game over.
    """
    print(riddles["Third riddle"]["riddle"])
    time.sleep(5)
    print("Choose between the following: " + riddles["Third riddle"]["answers"][0] + " or " + riddles["Third riddle"]["answers"][1]) 
    time.sleep(2)
    your_answer = input("What's your answer?\n")
    print("\n--------------------------------------")
    time.sleep(1)

    while True:
        your_answer = input("What's your answer, sun or egg?")

        if your_answer in riddles["Third riddle"]["answers"][1]:
            print("Right answer.\n")
            time.sleep(1.5)
            final_question()
            break
        elif your_answer == riddles["Third riddle"]["answers"][0]:
            print("Wrong answer.")
            time.sleep(1.5)
            game_over()
            restart_game()
            break
        else: 
            print("Invalid answer. Please choose between sun or egg\n")
            time.sleep(1)
            continue


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
        print(Fore.BLUE + " ######################")
        print(Fore.BLUE + " #                    #")
        print(Fore.BLUE + " #      BYE BYE!      #")
        print(Fore.BLUE + " #                    #")
        print(Fore.BLUE + " ######################")
        print(Style.RESET_ALL)


play_game()
