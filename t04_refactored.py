######################################################################
# Author: Scott Heggen  # Don't change me this time!
# Username: heggens     # Don't change me this time!
#
# Assignment: T04: Adventure in Gitland
#
# Purpose: To recreate a choose-your-own-adventure style game
# by refactoring T01.
#
# Each "twist" in the story is from a different group. The resulting story
# will either be incoherently random, or entertainingly "Mad Lib" like.
# Either way, it should be fun!
#
# This new version will take advantage of functions, as well as
# demonstrate the value of git as a tool for collaborating.
# https://docs.google.com/document/d/12AqOblfS_IRP24dKtyJrNh9a8E8JcmrvfzseTkbixyU/edit#
https://docs.google.com/document/d/10pPuYIQyzvUHcUOLCjlP7qWjj2qGqdNFRzZIwPNPCWw/edit?usp=sharing

######################################################################
# Acknowledgements:
#   Original Author: Scott Heggen
#
######################################################################
import random
from time import sleep
from random import *  # Code needed to import randomness. Group 5
delay = 1.0          # change to 0.0 for testing/speed runs; larger for dramatic effect!
dead = False


def start_story():
    """
    Introduction text for the story. Don't modify this function.

    :return: the user's name, captured from user input
    """
    user = input("What do they call you, unworthy adversary? ")
    print()
    print("Welcome,", user, ", to the labyrinth")
    sleep(delay)
    print("Before you lies two paths. One path leads to treasures of unimaginable worth.")
    print("The other, certain death. Choose wisely.")
    print()
    sleep(delay * 2)
    print("You are in a dark cave. You can see nothing.")
    print("Staying here is certainly not wise. You must find your way out.")
    print()
    sleep(delay)
    return user


def end_story(user):
    """
    This is the ending to the story. Don't modify this function, either.

    :param user: the user's name
    :return: None
    """
    print("Congratulations, " + user + ", you have made it to the end of this... strange... adventure. I hope you feel accomplished.")
    print()
    print()
    print()
    sleep(delay*5)
    print("Now go play again.")


def kill_if_dead(dead):
    """
    Simple function to check if you're dead

    :param dead: A boolean value where false let's the story continue, and true ends it.
    :return: None
    """
    if dead:
        quit()

###################################################################################


def scott_adventure():
    """
    My original adventure text I gave as an example. Leave it alone as well.

    :return: None
    """
    global dead             # You'll need this to be able to modify the dead variable
    direction = input("Which direction would you like to go? [North/South/East/West]")

    if direction == "North":
        # Good choice!
        print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
        sleep(delay)
    elif direction == "South":
        # Oh... Bad choice
        print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
        sleep(delay)
        print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
        print("Running seems like a good idea now. But... it's really, really dark.")
        print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
        print()
        sleep(delay*2)
        print("He eats you. You are delicious.")
        dead = True
    else:
        # Neutral choice
        print("You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
        sleep(delay)

    kill_if_dead(dead)

###################################################################################


def team_1_adv():
    pass
    # TODO Add your code here


def team_2_adv():
    pass
    # TODO Add your code here


def team_3_adv():
    pass
    # TODO Add your code here


def team_4_adv():
    pass
    # TODO Add your code here


def team_5_adv():

    sleep(3)
    print("You close your eyes for a brief second. As you do, you feel the wind swirl violently around you.")
    sleep(4)
    print("You open your eyes to find yourself in the middle of a dark forest.")
    sleep(3)
    escape = False  # Used to check if the player has escaped yet
    while not dead and not escape:
        doora = randint(1, 3)  # Assigns a random number to DoorA
        doorb = randint(1, 3)  # Assigns a random number to DoorB
        doorc = randint(1, 3)  # Assigns a random number to DoorC
        while ((doora == doorb) or (doorb == doorc) or (
                doorc == doora)):  # Re-rolls all values of the doors until they aren't equal.
            doora = randint(1, 3)
            doorb = randint(1, 3)
            doorc = randint(1, 3)
            # print("Another Iteration" + "\n")
        # print(str(DoorA) + str(DoorB) + str(DoorC))
        print("Every instinct you have is telling you to get out.")
        print("You start walking through the forest until you spot something in the distance.")
        sleep(5)
        print("You see a row of doors in the bark of trees that could lead you out of the forest." +
              " Which door do you enter (Door A, B, or C)?")
        choice = input("Pick one ")
        if choice.upper() == "A":
            print("You go through Door A")
            sleep(2)
            if doora == 1:
                print("You find a long windy path and decide to follow it.")
                sleep(delay * 3)
                print("You've died of starvation")
                sleep(3)
                dead = True
            elif doora == 2:
                print(
                    "You can't seem to find an exit from the forest, however you do stumble upon a small picnic basket.")
                sleep(3)
                print("You open the basket and find a warm sandwich and a red and white blanket to hold you over "
                      "until the morning.")
                sleep(5)
                print("You wake up to find yourself in the middle of a dark forest.")
                sleep(1)
            else:
                sleep(1)
                print("You follow a long tunnel")
                sleep(2)
                escape = True
        elif choice.upper() == "B":
            print("You go through Door B")
            sleep(2)
            if doorb == 1:
                print("You find a long windy path and decide to follow it.")
                sleep(delay * 3)
                print("You've died of starvation")
                dead = True
            elif doorb == 2:
                print(
                    "You can't seem to find an exit from the forest, however you do stumble upon a small picnic basket.")
                sleep(3)
                print("You open the basket and find a warm sandwich and a red and white blanket to hold you over "
                      "until the morning.")
                sleep(5)
                print("You wake up to find yourself in the middle of a dark forest.")
                sleep(1)
            else:
                sleep(1)
                print("You follow a long tunnel")
                sleep(2)
                escape = True
        elif choice.upper() == "C":
            print("You go through Door C")
            sleep(2)
            if doorc == 1:
                print("You find a long windy path and decide to follow it.")
                sleep(delay * 3)
                print("You've died of starvation")
                dead = True
            elif doorc == 2:
                print(
                    "You can't seem to find an exit from the forest, however you do stumble upon a small picnic basket.")
                sleep(3)
                print("You open the basket and find a warm sandwich and a red and white blanket to hold you over "
                      "until the morning.")
                sleep(5)
                print("You wake up to find yourself in the middle of a dark forest.")
                sleep(1)
            else:
                sleep(1)
                print("You follow a long tunnel")
                sleep(2)
                escape = True
        else:
            print("You pass out from thinking too hard. Good job.")
            sleep(2)
            print("You wake up to find yourself in the middle of a dark forest.")
            sleep(2)
    if not dead:
        sleep(1)
        print("Yay you Escaped!")


def team_6_adv():
    """
    Google Doc Link: https://docs.google.com/document/d/1w6XU_suOBSL9st5yvms3vZHbd9hZg8RCAYztqJXqp_E/edit#
    Refactored by Michale Hohl and Robert Dabbs
    :return:
    """
    # TODO Add your code here
    global dead
    import time
    doors = input("which doors you want to open? [A/B/C/D]")

    if doors == "A":
        # this is a very bad choice
        print("Samara is standing there with an axe, and she is not friendly.")  # Samara Morgan is a scary character from the ring movie
        print("It seems that she is very angry, and she start running towards you.")
        sleep(delay)
        print("You have been axed a question.")
        dead = True
    elif doors == "B":
        # this a good choice
        print("In this room there is a treasure hidden in one of a thousand boxes.")
        sleep(delay)
        print("Some of the boxes have warning signs on them.")
        print("It seems the best option is not to open the boxes.")
        print("You could stay in the room for safety or go back to the main area to choose another door.")
        # I believe the first group intended for the ability to choose a different option here
        print("You select a random box.")
        time.sleep(4)
        print("Congratulations! You have found the treasure.")
    elif doors == "C":
        # this door is another bad choice
        print("This room does not seem to be safe.")
        print("This is because there are groups of hungry zombies in with you, ready to attack.")
        print("The door is closed. There is no way out; you are trapped!")
        print("The only weapon in the room is a broom stick.")
        print("You attempt to fight the zombies off, however you are swept away.")
        print("The zombies eat you, and you are gone! However, they are still hungry.")
        print("Nice attempt though. Try to choose wisely next time!")
        print("You have been devoured by the zombies.")
        dead = True
    else:
        # This the exit
        print("This is the way out of this haunted house. Well done.")

    kill_if_dead(dead)


def team_7_adv():
    pass
    # TODO Add your code here


def team_8_adv():
    pass
    # TODO Add your code here


def team_9_adv():

    # TODO Add your code here

    print("You decided to go grave robbing and ran encounter a corridor with multiple directions")
    sleep(delay)
    direction = input("Which path will lead you to wealth untold? [North/South/East/West]")

    if direction == "West" or direction == "west":
        print("You stumble upon a pile of treasure")
        question = input("Do you take all the treasure? (Yes/No")
        if question == "Yes":
            print("You are greedy and get attacked by a mob of mummies.")
        if question == "No":
            print("You are encountered by a mummy that allows you to take as much gold as you can fit in your pockets. "
                  "Good job for not being greedy.")
    if direction == "North" or direction ==

def team_10_adv():
    pass
    # TODO Add your code here


def team_11_adv():
    pass
    # TODO Add your code here


def team_12_adv():
    pass
    # TODO Add your code here


def team_13_adv():
    pass
    # TODO Add your code here


def team_14_adv():

    # FIXME: TEAM 14

    doors = input("You come across three doors. Which door will you open? The Left, Middle, or Right door?")
    print()
    if doors == "Left" or doors == "left" or doors == " Left" or doors == " left":
        print("As you walk, you trip on a rock.")
        print("In front of you, there was a water well.")
        print("You fall into the well and start calling for help.")

        print()
        dead = True
    elif doors == "Middle" or doors == "middle" or doors == " Middle" or doors == " middle":
        print("In front of you is a long tunnel.")
        print("You walk for hours and hours, but never come to an end.")
        print("Eventually, you pass out from exhaustion, and your world goes black.")
        print()
        sleep(delay)
    else:
        print("You walk into a grass field, and as you walk, you see a farm off into the distance.")
        print("You see people milling about near the farm, and decide to walk towards it.")
        print("Your journey takes a little bit of time.")
        print()
        sleep(delay)

    if dead:
        print("You've died. RIP")
        print("That's the end of your story.")
        quit()


def team_15_adv():
    pass
    # TODO Add your code here


def team_16_adv():
    pass
    # TODO Add your code here


def team_17_adv():
    pass
    # TODO Add your code here


def team_18_adv():
    pass
    # TODO Add your code here


def team_19_adv():
    pass
    # TODO Add your code here


def team_20_adv():
    pass
    # TODO Add your code here


def main():
    """
    The main function, where the program starts.
    :return: None
    """

    user = start_story()
    paths = [scott_adventure, team_1_adv, team_2_adv,
             team_3_adv, team_4_adv, team_5_adv,
             team_6_adv, team_7_adv, team_8_adv,
             team_9_adv, team_10_adv, team_11_adv,
             team_12_adv, team_13_adv, team_14_adv,
             team_15_adv, team_16_adv, team_17_adv,
             team_18_adv, team_19_adv, team_20_adv]
    random.shuffle(paths)                               # Shuffles the order of paths, so each adventure is different

    for i in range(len(paths)):
        paths[i]()                                      # Runs each function in the paths list

    end_story(user)


main()

