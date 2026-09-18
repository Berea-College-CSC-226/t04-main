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

    if is_alive is not None and is_alive == False:
        quit()

###################################################################################

def scott_adventure(username):
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

def team_1_adv(username):
    """
    https://docs.google.com/document/d/1CpA6AyTEu6KLumAtVBWUhpw5lc3oJrjbbiS-z4GUpRY/edit?userstoinvite=yukikaleg8106@gmail.com&sharingaction=manageaccess&role=writer&tab=t.0#heading=h.f6tumop9n7at
    Yuki Fukushima
    Ryan Hensley
    :return: None
    """
    direction = input(
        "You bump your head into a wall. You feel your way around, you have two choices, left or right.  [Left/Right]: ")

    if direction == "Left":
        # Good choice
        print("You safely leave the cave.")
        sleep(DELAY)
        return True
    elif direction == "Right":
        # Neutral choice
        print("You fall into a pit. You have another chance of life. ")
        sleep(DELAY)
    else:
        print("You're confused.")
        print("An invalid direction makes you bump your head into a wall again.")
        sleep(DELAY)
        print("You died from a concussion.")
        return False

    direction = input("You find yourself at a crossroad. You can go left or right. [Left/Right]: ")

    if direction == "Left":
        # Good choice
        print("You find a town full of dwarfs that are willing to help you find your way out.")
        return True
    elif direction == "Right":
        # Bad choice
        print("You get trapped by the land around you and suffocated.")
        return False
    else:
        print("You're confused. ")
        print("An invalid direction makes you bump your head into a wall.")
        sleep(DELAY)
        print("You died from a concussion.")
        return False

###################################################################################
def team_2_adv(username):
    pass

###################################################################################

def team_3_adv(username):
    pass

###################################################################################

def team_4_adv(username):
    pass

###################################################################################

def team_5_adv(username):
    pass

###################################################################################

def team_6_adv(username):
    pass

###################################################################################

def team_7_adv(username):
    pass

###################################################################################

def team_8_adv(username):
    pass

###################################################################################

def team_9_adv(username):
    pass

###################################################################################

def team_10_adv(username):
    pass

###################################################################################

def team_11_adv(username):
    pass

###################################################################################

def team_12_adv(username):
    pass


###################################################################################


def main():
    """
    Choose your own adventure!
    """
    paths = [scott_adventure, team_1_adv, team_2_adv,
             team_3_adv, team_4_adv, team_5_adv,
             team_6_adv, team_7_adv, team_8_adv,
             team_9_adv, team_10_adv, team_11_adv,
             team_12_adv]
    # Shuffles the order of paths, so each adventure is different
    random.shuffle(paths)

    user = start_story()
    for i in range(len(paths)):
        is_alive = paths[i](user)  # Runs each function in the paths list
        kill_if_dead(is_alive)

    end_story(user)


if __name__ == "__main__":
    main()