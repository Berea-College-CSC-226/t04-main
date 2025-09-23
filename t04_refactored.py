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

DELAY = 1.0  # change to 0.0 for testing/speed runs; larger for dramatic effect!


def start_story():
    """
    Introduction text for the story.
    Don't modify this function.

    :return: the user's name, captured from user input
    """
    user = input("What do they call you, unworthy adversary? ")
    print()
    print("Welcome,", user, ", to the labyrinth")
    sleep(DELAY)
    print("Before you lies two paths. One path leads to treasures of unimaginable worth.")
    print("The other, certain death. Choose wisely.")
    print()
    sleep(DELAY * 2)
    print("You are in a dark cave. You can see nothing.")
    print("Staying here is certainly not wise. You must find your way out.")
    print()
    sleep(DELAY)
    return user


def end_story(user):
    """
    This is the ending to the story.
    Don't modify this function, either.

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
    sleep(DELAY * 5)
    print("Now go play again.")


def kill_if_dead(is_alive):
    """
    Simple function to check if you're dead

    :param is_alive: A boolean value representing livelihood.
    :return: None
    """
    if not is_alive:
        quit()


###################################################################################
###################################################################################

def scott_adventure():
    """
    My original adventure text I gave as an example. Leave it alone as well.

    :return: None
    """

    direction = input(
        "Which direction would you like to go? [North/South/East/West]")

    if direction == "North":
        # Good choice!
        print("You are still trapped in the dark, but someone else is there with you now! I hope they're friendly...")
        sleep(DELAY)
    elif direction == "South":
        # Oh... Bad choice
        print("You hear a growl. Not a stomach growl. More like a big nasty animal growl.")
        sleep(DELAY)
        print("Oops. Turns out the cave was home to a nasty grizzly bear. ")
        print("Running seems like a good idea now. But... it's really, really dark.")
        print("You turn and run like hell. The bear wakes up to the sound of your head bouncing off a low stalactite. ")
        print()
        sleep(DELAY * 2)
        print("He eats you. You are delicious.")
        return False     # kill the user!
    else:
        # Neutral choice
        print(
            '''You're in another part of the cave. It is equally dark, and equally uninteresting. 
            Please get me out of here!''')
        sleep(DELAY)
    return True       # User survives all other scenarios


###################################################################################
###################################################################################
###################################################################################

def team_1_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_2_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_3_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_4_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_5_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_6_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_7_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_8_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_9_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_10_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_11_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_12_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_13_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_14_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_15_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_16_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_17_adv(username):
    """
    https://docs.google.com/document/d/18woVZC0_gGfPwAVvYnmwAPByMWi1A6bwZOANyBjX2Kk/edit?usp=sharing
    Nahom Terrefe
    Naod Ksmu
    :return:none
    """
    dead = False
    direction = input("There are three boxes in front of you: left, middle, and right. Which one would you like to pick?").lower().strip()

    if direction == "left":
        # Ooooooh... unfortunate.
        print("Man, that sucks. ")
        sleep(DELAY)
        print("You picked... the bomb!!")
        print("BOOOOOOMMMM!!!")
        sleep(3)
        dead = True

    elif direction == "middle":
        # neutral
        print("You get...")
        sleep(DELAY)
        print("A pen with unlimited ink")
        sleep(DELAY)
        print("Fun right...?")
        dead = False
    elif direction == "right":
        print("There is a diming light coming out the box.")
        sleep(DELAY)
        print("It shines brighter by the second! You get close to see what is in the box")
        sleep(DELAY)
        print("BANG! you got hit by a punch! It was a shiny box glove!")
        dead = True
    else:
        # Noice
        print("I see you don't like to follow instructions, \n"
              "for you have not heeded to the instrutions you have chose a far greater "
              "predicament. ")
        sleep(DELAY)
        print(".")
        sleep(DELAY)
        print("..")
        sleep(DELAY)
        print("...")
        sleep(DELAY)
        print("INSTANT DEATH")
        dead= True

    if dead:
        print("welcome to the afterlife my child. You have chosen wrong. Until WE MEET AGAIN!")
        quit()


###################################################################################


def team_18_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_19_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_20_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_21_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_22_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_23_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_24_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_25_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_26_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_27_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_28_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_29_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_30_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def main():
    """
    The main function, where the program starts. No modifications are needed here!
    :return: None
    """

    paths = [scott_adventure, team_1_adv, team_2_adv,
             team_3_adv, team_4_adv, team_5_adv,
             team_6_adv, team_7_adv, team_8_adv,
             team_9_adv, team_10_adv, team_11_adv,
             team_12_adv, team_13_adv, team_14_adv,
             team_15_adv, team_16_adv, team_17_adv,
             team_18_adv, team_19_adv, team_20_adv,
             team_21_adv, team_22_adv, team_23_adv,
             team_24_adv, team_25_adv, team_26_adv,
             team_27_adv, team_28_adv, team_29_adv,
             team_30_adv]
    # Shuffles the order of paths, so each adventure is different
    random.shuffle(paths)

    user = start_story()
    for i in range(len(paths)):
        is_alive = paths[i](user)  # Runs each function in the paths list
        kill_if_dead(is_alive)

    end_story(user)


if __name__ == "__main__":
    main()