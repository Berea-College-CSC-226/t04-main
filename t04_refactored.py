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
######################################################################
# Acknowledgements:
#   Original Author: Scott Heggen
#
######################################################################
import random
from time import sleep

delay = 1.0  # change to 0.0 for testing/speed runs; larger for dramatic effect!
isDead = False


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
    print(
        "Congratulations, " +
        user +
        ", you have made it to the end of this... strange... adventure. I hope you feel accomplished.")
    print()
    print()
    print()
    sleep(delay * 5)
    print("Now go play again.")


def kill_if_dead(dead):
    """
    Simple function to check if you're dead

    :param dead: A boolean value where false lets the story continue, and true ends it.
    :return: None
    """
    if dead:
        quit()


###################################################################################
###################################################################################

def scott_adventure():
    """
    My original adventure text I gave as an example. Leave it alone as well.

    :return: None
    """
    global isDead  # You'll need this to be able to modify the dead variable
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
        sleep(delay * 2)
        print("He eats you. You are delicious.")
        isDead = True
    else:
        # Neutral choice
        print(
            '''You're in another part of the cave. It is equally dark, and equally uninteresting. 
            Please get me out of here!''')
        sleep(delay)

    kill_if_dead(isDead)


###################################################################################
###################################################################################
###################################################################################

def team_1_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_2_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_3_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_4_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_5_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_6_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_7_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_8_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_9_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_10_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_11_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_12_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_13_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_14_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_15_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_16_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_17_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_18_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_19_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_20_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_21_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_22_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_23_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_24_adv():
    pass
    # TODO Add your code here


def main():
    """
    The main function, where the program starts. No modifications are needed here!
    :return: None
    """

    user = start_story()
    paths = [scott_adventure, team_1_adv, team_2_adv,
             team_3_adv, team_4_adv, team_5_adv,
             team_6_adv, team_7_adv, team_8_adv,
             team_9_adv, team_10_adv, team_11_adv,
             team_12_adv, team_13_adv, team_14_adv,
             team_15_adv, team_16_adv, team_17_adv,
             team_18_adv, team_19_adv, team_20_adv,
             team_21_adv, team_22_adv, team_23_adv,
             team_24_adv]
    random.shuffle(paths)  # Shuffles the order of paths, so each adventure is different

    for i in range(len(paths)):
        paths[i]()  # Runs each function in the paths list

    end_story(user)


main()
