# Imported modules
import time
import random
import sys
from colorama import Fore, Style

# Global variables
global axe
axe = "no"
global CHARACTER_NAME
CHARACTER_NAME = ""

# The riddles dictionary contains three items, each of which is another
# dictionary representing a riddle.
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


def choose_name():
    """
    Starts the adventure game with a welcome message.
    Lets the player choose a character name.
    """
    global CHARACTER_NAME

    time.sleep(2)
    print("\nThis is the Swedish Forest Text Adventure Game.\n")
    time.sleep(2)
    print("After you've typed your answer you press the 'Enter' key to "
          "submit your answer.")
    time.sleep(2)
    print("(You can exit the game by answering 'exit' "
          "to the questions)")
    time.sleep(2)
    print("\n--------------------------------------\n")
    time.sleep(2)

    # Character name must be chosen before continuing
    print("Welcome, brave adventurer!\n")
    time.sleep(2)
    character_names = ["Bjorn", "Ragnar", "Hilda"]
    name = input("Choose one of the following "
                 f"character names: {', '.join(character_names)}:\n")
    time.sleep(1.5)

    while True:
        if name in character_names:
            CHARACTER_NAME = name
            are_you_ready()
            break

        if name.lower() == "exit":
            exit_game()
            break

        else:
            print("\nThat's not one of the options. Please try again.")
            name = input("Choose one of the following "
                         f"character names: {', '.join(character_names)}: \n")
        time.sleep(2)


def are_you_ready():
    """
    Asks the player if they are ready to play the game.
    Displays introduction before displaying the first question.
    """
    global CHARACTER_NAME

    while True:
        try:
            ready = input("\nAre you ready to enter the deep, dark "
                          f"Swedish forest, {CHARACTER_NAME}? (yes or no):\n")
            time.sleep(1.5)

            # If the player answers yes, the game continues with
            # the introduction
            if ready.lower() == "yes":
                print("")
                print("Get ready.\n")
                print("--------------------------------------\n")
                time.sleep(2)
                print("You find yourself lost in the Swedish forest.")
                time.sleep(2.5)
                print("You have no memory of how you got there.\n")
                time.sleep(2.5)
                print("The cold autumn wind sends shivers down your spine.")
                time.sleep(2.5)
                print("When you listen closely, you can hear the trees "
                      "whispering to each other.\n")
                time.sleep(2.5)
                print("You can't stay here. You have to find a way out!\n")
                time.sleep(2.5)
                print("Good luck. See you on the other side...hopefully.\n")
                time.sleep(1.5)
                print("--------------------------------------\n")
                time.sleep(2.5)
                first_question()

            elif ready.lower() == "exit":
                exit_game()
                break

            # If the player answers no,
            # the game over and restart game functions are called
            elif ready.lower() == "no":
                print("\nIt's game over before it even begins!\n")
                time.sleep(2)
                game_over()
                time.sleep(1.5)
                restart_game()
                break
            else:
                raise ValueError("\nInvalid answer. Plese enter yes or no.")
        except ValueError as error:
            print(error)


def first_question():
    """
    Presents the player with the first question,
    to either cross the stream or follow the stream.
    Depedning on the answer the player eiter continues to
    second_question, or it's game over.
    """
    print("You try to stand up.")
    time.sleep(2)
    print("Your head is spinning.")
    time.sleep(2)
    print("But you need to get going.\n")
    time.sleep(2)
    print("You stumble through the forest until you reach a small stream.")
    time.sleep(2)
    print("It looks calm.\n")
    time.sleep(2)

    # Displays the question and possible answers
    print("Do you:")
    time.sleep(1.5)
    print("a) Follow the stream until you find a safer way to cross it")
    time.sleep(2)
    print("b) Cross the stream and hope it is as calm as it looks \n")
    time.sleep(1.5)

    while True:
        # If the player answers "a" the loop breaks and they continue
        # # to second_question
        your_answer = input("What do you do? (a or b):\n")

        if your_answer.lower() == "a":
            time.sleep(2)
            second_question()
            break

        # If the player answers "b," the loop breaks, and it's game over
        elif your_answer.lower() == "b":
            print("--------------------------------------\n")
            time.sleep(1.5)
            print("You attempt to cross the stream.\n")
            time.sleep(2)
            print("But oh no! Quicksand!\n")
            time.sleep(2)
            print("It drags you down and you drown.\n")
            time.sleep(2)
            game_over()
            time.sleep(2)
            restart_game()
            time.sleep(2)
            break

        elif your_answer.lower() == "exit":
            exit_game()
            break

        # If the player answers neither a nor b, they are prompted to answer
        # the question again
        else:
            print("Invalid answer. Please enter a or b.")
            continue


def second_question_intro():
    """
    Presents the player with the intro to the
    second question.
    """
    print("\n--------------------------------------")
    time.sleep(1.5)
    print("\nYou follow the stream.")
    print("After a while, it narrows down enough for you to jump over.\n")
    time.sleep(2)
    print("But what's that sound?\n")
    time.sleep(2)
    print("People! You can hear a faint laughter coming from inside the "
          "forest.")
    time.sleep(2)
    print("You notice a bonfire in the distance. "
          "Maybe they can help you?\n")


def second_question():
    """
    Presents the player with the second question,
    to either approach the group of people or stay away from them.
    Depending on the answer the player eiter continues to
    first_riddle, or it's game over.
    """
    second_question_intro()

    # Displays the question and answers
    time.sleep(2)
    print("Do you:")
    time.sleep(1.5)
    print("a) Approach the group of people and ask for directions out of "
          "the forest")
    time.sleep(2)
    print("b) Stay away from them. You don't know who these people are\n")
    time.sleep(1.5)

    while True:
        your_answer = input("What do you do? (a or b):\n")
    
        # If the player answers "b" the loop breaks and it's game over
        if your_answer.lower() == "a":
            print("--------------------------------------\n")
            print("You approach the group of people.\n")
            time.sleep(2)
            print("But you realise now... they are not people..they are...\n")
            time.sleep(2)
            print("TROLLS!\n")
            print("      ▴▴▴▴    ")
            print("   ☾=( ⚯ )=☽  ")
            print(r" /    \⎴ /  \ ")
            print(r" /|    •    |\      ⺣")
            print(r" \_\   •   /_/     ⺣ ")
            print(r"  |    /    |     ⺣ ⺣ ")
            print(r"   |   ()   |       /^\\")
            print(r"   \   \\\  /      //^\\")
            print(r"   mmm   mmm      ///^\\\\")
            print("")
            time.sleep(2)
            print("They are having a barbecue, and you just served them "
                  "dessert.\n")
            game_over()
            time.sleep(2)
            restart_game()
            time.sleep(2)
            break

        # If the player answers "a" the loop breaks and they continue. 
        # to first_riddle
        elif your_answer.lower() == "b":
            time.sleep(2)
            third_question()
            break

        elif your_answer.lower() == "exit":
            exit_game()

        # If the player answers neither a or b they are promped to answer
        # the question again
        else:
            print("\nInvalid choice. Please enter a or b.")
            continue


def third_question():
    """
    Presents the player with the third question,
    to either take the axe or leave it.
    Depedning on if the player answers yes or no, different print
    messages are displayed. Both answers leads to first_riddle
    """
    print("\n--------------------------------------")
    print("\nGood choice! Trust no one.\n")
    time.sleep(2)
    print("It's still dark, but the full moon lights up your way.")
    time.sleep(2)
    print("Suddenly, you trip over something.\n")
    time.sleep(2)
    print("It's an axe!\n")
    time.sleep(2)
    print("Wonder who it belongs to?\n")
    time.sleep(2)

    # Displays the third question. Both answers leads to first_riddle
    while True:
        global axe

        axe = input("Do you take the axe with you? (yes or no):\n")

        if axe == "yes":
            time.sleep(2)
            print("\nThat's probably a smart move, considering what's "
                  "out there.")
            time.sleep(1.5)
            print("\n--------------------------------------\n")
            time.sleep(2)
            first_riddle()
            break

        elif axe == "no":
            time.sleep(2)
            print("\nThat's probably a smart move.\nThe owner of the axe will "
                  "not be happy when he notices it's gone.")
            time.sleep(1.5)
            print("\n--------------------------------------\n")
            time.sleep(2)
            first_riddle()
            break

        elif axe == "exit":
            exit_game()
            break

        else:
            print("Invalid choice. Please enter yes or no.")
            continue


def first_riddle():
    """
    Presents the player with the first riddle.
    Depedning on the answer the player eiter continues to
    second_riddle, or it's game over.
    """
    print("After a while, you decide you need a rest. \n")
    time.sleep(2)
    print("You reach a small lake.")
    time.sleep(2)
    print("You splash your face with water and have a drink. \n")
    time.sleep(2.5)
    print("You don't notice the creature Gollum sneaking up behind you...\n")
    time.sleep(2.5)
    print(Fore.BLUE + " ###################")
    print(Fore.BLUE + " #                 #")
    print(Fore.BLUE + " #      BOOO!      #")
    print(Fore.BLUE + " #                 #")
    print(Fore.BLUE + " ###################")
    print(Style.RESET_ALL)
    time.sleep(2)
    print("Gollum will let you go once you've played a game of riddles.\n")
    time.sleep(2.5)
    print("He's giving you a fair chance to answer his riddles.\n"
          "You'll get two options.")
    time.sleep(3)
    print("So think carefully.\n")
    time.sleep(2)
    print("First riddle:\n")
    time.sleep(2)

    # Displays the first riddle and possible answers
    print(riddles["First riddle"]["riddle"])
    time.sleep(7)
    print("Choose between the following options: "
          + riddles["First riddle"]["answers"][0]
          + " or "
          + riddles["First riddle"]["answers"][1])
    time.sleep(1)

    while True:
        your_answer = input("What's your answer?\n")
        time.sleep(2)

        # If the player answers "time" the loop breaks and they continue
        # to second_riddle
        if your_answer in riddles["First riddle"]["answers"][0]:
            print("\nRight answer.")
            time.sleep(1.5)
            print("\n--------------------------------------\n")
            time.sleep(1.5)
            print("Next riddle:\n")
            time.sleep(2)
            second_riddle()
            break

        # If the player answers "wind" the loop breaks and it's game over
        elif your_answer == riddles["First riddle"]["answers"][1]:
            print("\nWrong answer.\n")
            time.sleep(2)
            game_over()
            restart_game()
            break

        # If the player types "exit" the loop breaks and they exit the game
        elif your_answer.lower() == "exit":
            exit_game()
            break

        # If the player answers neither time or wind they are promped to answer
        # the question again
        else:
            if your_answer not in riddles["First riddle"]["answers"]:
                print("\nInvalid answer. Please choose between time or wind.")
                time.sleep(1)
                continue


def second_riddle():
    """
    Presents the player with the second riddle.
    Depedning on the answer the player eiter continues to
    third_question, or it's game over.
    """
    # Displays the second riddle and possible answers
    print(riddles["Second riddle"]["riddle"])
    time.sleep(7)
    print("Choose between the following options: "
          + riddles["Second riddle"]["answers"][0]
          + " or "
          + riddles["Second riddle"]["answers"][1])
    time.sleep(1)

    while True:
        your_answer = input("What's your answer?\n")
        time.sleep(2)

        # If the player answers "darkness" the loop breaks and they continue
        # to final_question
        if your_answer in riddles["Second riddle"]["answers"][0]:
            print("\nRight answer.\n")
            time.sleep(2)
            print("You are very good at riddles.\n")
            time.sleep(2)
            print("'yess..yess my precious, very good..'\n")
            time.sleep(2.5)
            print("Gollum lets you go.")
            time.sleep(2)
            print("\n--------------------------------------\n")
            time.sleep(2)
            final_question()
            break
        # If the player answers "shadow" the loop breaks and it's game over
        elif your_answer == riddles["Second riddle"]["answers"][1]:
            print("\nWrong answer.\n")
            time.sleep(2)
            game_over()
            restart_game()
            break

        # If the player types "exit" the loop breaks and they exit the game
        elif your_answer.lower() == "exit":
            exit_game()
            break

        # If the player answers neither darkness or wind they are promped to
        # answer the question again
        else:
            if your_answer not in riddles["Second riddle"]["answers"]:
                print("\nInvalid answer. Please choose between darkness or shadow.")
                time.sleep(1)
                continue


def final_question():
    """
    Presents the player with the final question.
    The player now has two options.
    Option a) is game over
    Option c) has two outcomes. Depending on if they picked up
    the axe or not. If they picked up the axe, they are taken back to
    Gollum to answer a third riddle. If they didn't pick up the axe it's
    victory, the player makes it out of the forest
    """
    print("You don't have much energy left.")
    time.sleep(2)
    print("Will you ever find your way out?\n")
    time.sleep(2)
    print("You can hear something...\n")
    time.sleep(2)
    print("It's a dwarf sitting on a rock further ahead. He's crying.")
    time.sleep(2.5)
    print("What do you do?\n")
    time.sleep(2)
    print("You have to choose wisely.\n")
    time.sleep(2.5)
    print("Your life might depend on it...\n")
    time.sleep(2)

    # Displays the question and answers
    print("Do you:")
    time.sleep(1.5)
    print("a) Approach the dwarf and ask why he's upset.")
    time.sleep(2)
    print("b) Sneak past the dwarf and hope he doesn't notice you.\n")
    time.sleep(1.5)

    while True:
        your_answer = input("What do you do? (a or b):\n")
        time.sleep(2)

        # If the player answers "b" the loop breaks and it's game over
        if your_answer.lower() == "b":
            print("\nYou sneak past the dawrf.")
            time.sleep(2)
            print("Keeping a close eye on him the whole time.\n")
            time.sleep(2)
            print("You're so focused on not being spotted.")
            time.sleep(2)
            print("That you don't notice the cliff you're slowly "
                  "heading towards.\n")
            time.sleep(2)
            print("And down you fall, to a certain death.\n")
            time.sleep(2)
            game_over()
            restart_game()
            break

        elif your_answer.lower() == "a":
            # If the player answers "a" and axe == "no" the loop breaks and the
            # game is finished.
            if axe == "no":
                print("\nYou walk over to the crying dwarf.")
                time.sleep(2)
                print("He tells you he's lost his axe.\n")
                time.sleep(2)
                print("He lights up when you tell him you've seen it!")
                time.sleep(2)
                print("You point him in the right direction.")
                time.sleep(2)
                print("He's forever thankful.\n")
                time.sleep(2)
                print("He offers you his map to help you find your way out.\n")
                time.sleep(2)
                print("With the map in you hand, you're out of the forest in "
                      "no time!\n")
                time.sleep(2.5)
                print(Fore.GREEN + " ######################")
                print(Fore.GREEN + " #                    #")
                print(Fore.GREEN + " #      VICTORY!      #")
                print(Fore.GREEN + " #                    #")
                print(Fore.GREEN + " ######################")
                print(Style.RESET_ALL)
                print(f"\nCongratulations, {CHARACTER_NAME}, you completed "
                      "the Swedish Forest Text Adventure Game!")
                restart_game()

            # If axe == "yes" the player is directed to third_riddle
            elif axe == "yes":
                print("\nYou walk towards the crying dwarf.")
                time.sleep(2)
                print("He sees you holding his missing axe!\n")
                time.sleep(2)
                print("He yells!\n")
                time.sleep(2)
                print("     THIEF!\n")
                time.sleep(2)
                print("Before you have time to react, the dwarf throws a "
                      "rock at you.\n")
                time.sleep(2.5)
                print("It hits you right between the eyes.")
                time.sleep(1.5)
                print("\n--------------------------------------\n")
                time.sleep(2)
                third_riddle()
                break

        # If the player types "exit" the loop breaks and they exit the game
        elif your_answer.lower() == "exit":
            exit_game()
            break

        # If the player answers neither a or b, they are promped to answer
        # the question again
        else:
            print("\nInvalid choice. Please enter a or b.")
            continue


def third_riddle():
    """
    If the player answers a) on the final question and
    axe == yes, they will be presented with the third riddle.
    Depedning on the answer the player eiter continues to
    final_question, or it's game over.
    """
    print("You wake up with a terrible headache.\n")
    time.sleep(2)
    print("You're back at the lake.")
    time.sleep(2)
    print("How did you get here?\n")
    time.sleep(2)
    print("'They are awake, my precious! They are awake!'\n")
    time.sleep(2)
    print("Oh no..it's Gollum again.\n")
    time.sleep(2)
    print("He has prepared another riddle.")
    time.sleep(2)
    print("And just like before he will only let you go "
          "if you answer correctly.\n")
    time.sleep(3)
    print("The third riddle goes as follows:\n")
    time.sleep(2)

    # Displays the third riddle and possible answers
    print(riddles["Third riddle"]["riddle"])
    time.sleep(4)
    print("Choose between the following options: "
          + riddles["Third riddle"]["answers"][0]
          + " or "
          + riddles["Third riddle"]["answers"][1])

    while True:
        your_answer = input("What's your answer?\n")
        time.sleep(1)

        # If the player answers "egg" the loop breaks and they continue
        # to final_question
        if your_answer in riddles["Third riddle"]["answers"][1]:
            print("\nRight answer.\n")
            time.sleep(2)
            print("You're free to go, again.\n")
            time.sleep(1.5)
            print("--------------------------------------\n")
            time.sleep(2)
            second_final_question()
            break

        # If the player answers "sun" the loop breaks and it's game over
        elif your_answer == riddles["Third riddle"]["answers"][0]:
            print("\nWrong answer.\n")
            time.sleep(2)
            game_over()
            restart_game()
            break

        elif your_answer.lower() == "exit":
            exit_game()
            break

        # If the player answers neither sun or egg they are promped to
        # answer the question again
        else:
            print("\nInvalid answer. Please choose between sun or egg")
            time.sleep(1)
            continue


def second_final_question():
    """
    If the player answer "egg" in the third_riddle
    the player is directed to second_final_question() and is
    displayed with the last question that either leads to victory or
    game over, using the random factor.
    """
    # Displays the question and answers
    print("You find a path you start following.")
    time.sleep(2)
    print("Oh no, a dead end.\n")
    time.sleep(2)
    print("But wait, you see a rune at the end of the path.")
    time.sleep(2)
    print("There's a poem on the rune.\n")
    time.sleep(2.5)
    print("A coin you toss,")
    time.sleep(1.5)
    print("A chance you take,")
    time.sleep(1.5)
    print("Heads or tails,")
    time.sleep(1.5)
    print("Which path will fate make?\n")
    time.sleep(2.5)
    print("On a small pedestal next to the rune, there is a coin.\n")
    time.sleep(2.5)
    print("You decide to flip it.\n")
    time.sleep(2)
    print("You count to 3:")
    time.sleep(1.5)
    print("1")
    time.sleep(1.5)
    print("2")
    time.sleep(1.5)
    print("3")
    time.sleep(1.5)

    # Ask player to enter "toss and randomly generates results
    input("Enter 'flip' to flip the coin:\n")
    time.sleep(2)
    coin_tossed = random.choice(["heads", "tails"])
    print(f"\nThe coin lands on {coin_tossed}. \n")
    time.sleep(2)

    # If the coin lands on "heads" the game is finished
    while True:
        if coin_tossed == "heads":
            print("Everything becomes dark.\n")
            time.sleep(2)
            print("You open your eyes and realize...")
            time.sleep(2)
            print("You're in your bed, safe!")
            time.sleep(2)
            print("\n--------------------------------------")
            print(Fore.GREEN + " ######################")
            print(Fore.GREEN + " #                    #")
            print(Fore.GREEN + " #      VICTORY!      #")
            print(Fore.GREEN + " #                    #")
            print(Fore.GREEN + " ######################")
            print(Style.RESET_ALL)
            time.sleep(1.5)
            print(f"Congratulations, {CHARACTER_NAME}! You completed the "
                  "Swedish Forest Text Adventure Game!\n")
            time.sleep(1.5)
            restart_game()
            break

        # If the coin lands on "tails", it's game over
        print("A trap door opens beneath you and you fall to your "
              "death.\n")
        time.sleep(2)
        game_over()
        restart_game()
        break


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
    global CHARACTER_NAME

    restart_game = input(f"Do you want to restart the game, {CHARACTER_NAME}? "
                         "(yes or no): ")

    while restart_game.lower() not in ["yes", "no"]:
        print("\nPlease enter either 'yes' or 'no'.")
        restart_game = input("Do you want to restart the game? "
                             "(yes or no): \n")

    if restart_game.lower() == "yes":
        print("\n--------------------------------------")
        time.sleep(1.5)
        choose_name()

    else:
        time.sleep(1)
        print("")
        print(Fore.BLUE + " ######################")
        print(Fore.BLUE + " #                    #")
        print(Fore.BLUE + " #      BYE BYE!      #")
        print(Fore.BLUE + " #                    #")
        print(Fore.BLUE + " ######################")
        print(Style.RESET_ALL)
        exit_game()


def exit_game():
    """
    Is called if the player chooses to exit the game,
    at any stage.
    """
    global CHARACTER_NAME
    print(f"\nThanks for playing, {CHARACTER_NAME}!\n")
    sys.exit()


choose_name()
