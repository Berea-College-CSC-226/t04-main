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
    """ https://docs.google.com/document/d/14o_900GCeVZEadcvwv_15i2ZS8oINYH6bJigpeGAsV8/edit?usp=sharing
    Dalmar- Julio
    :return: none """

    dead = False
    direction = input("which direction do you want to go North/South/East/West")

    if direction == "North":
        # Bad choice! Sacrifice room!
        print("The north room is dimly lit by lanterns with red fire.")
        print("Five people in black robes are gathered around an altar.")
        print("Their argument quiets as you walk in.")
        sleep(DELAY)
        print("'Oh, how perfect,' one says. 'You have been Forgiven, Yuxila.'")
        print("Stone rises from the floor to block your exit.")
        sleep(DELAY)
        print("You are captured by the cultists. You are dead.")
        dead = True
    elif direction == "South":
        # Bad choice! Ritual room!
        print("You see a glowing circle on the floor. Robed figures stand around it and chant.")
        print("You do not recognize their words.")
        sleep(DELAY)
        print("A pressure builds in the room. It is too much.")
        print("Your heart bursts open inside your chest.")
        print("You are dead.")
        dead = True
    elif direction == "East":
        # Good choice! Dorms!
        print("The room you emerge into has a low stone ceiling. Bunked beds line the walls for fifty meters.")
        print("You walk carefully down the length of the room. Your breath is the loudest sound you hear.")
        sleep(DELAY * 2)
        print("At the end of the room is a kitchen and a door. There is no window.")
        print("You steel yourself and open the door as quietly as you can.")
        sleep(DELAY)
        print("The door leads outside. You are free.")
    elif direction == "West":
        # Neutral choice. Armory.
        print("This room is lined with weapons. Most are ornate daggers, hundreds of them hang on hooks lining the walls.")
        print("You see glowing runes on many of the daggers. Several do not have runes.")
        dagger = input("Do you take a dagger? [Yes/No]")
        if dagger == "Yes":
            print("You observe several daggers without runes. You take the one that looks unassuming.")
            print("The sound of a bell rings through the caves. You tense.")
            sleep(DELAY)
            print("Robed figures flood the room. You attempt to fend them off, but you are overwhelmed.")
            print("You are dead.")
            dead = True
        else:
            print("This room looks suspicious. You return quietly to previous room.")

    if dead == True:
        print("You have been sacrificed to the Great Devourer.")
        quit()


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
             team_24_adv]
    # Shuffles the order of paths, so each adventure is different
    random.shuffle(paths)

    user = start_story()
    for i in range(len(paths)):
        is_alive = paths[i]()  # Runs each function in the paths list
        kill_if_dead(is_alive)
    end_story(user)


main()
