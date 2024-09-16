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


def team_2_adv(delay = 1.0, username = "Scott"):
    is_dead = False
    print("It's Wednesday morning. You wake up at 09:10am and see the sun through your window.")
    print("Suddenly, you realize that you are almost late for your CSC 226 class at 09:20am.")
    print("You know you need your morning coffee to get through the day, but you are almost late for class!")
    sleep(delay)
    decision = input("Coffee or class?").lower()

    if decision == "coffee":
        print("You drink your coffee and run to class.")
        sleep(delay)
        print("You are late, and awake. But the instructor is also late so he doesn't know.")

    elif decision == "class":
        print("You manage to arrive to class at 09:20am.")
        sleep(delay)
        is_dead = True

    if is_dead:
        print("Although you made it to class on time, you cannot stay awake.")
        sleep(delay)
        print()
        print("In an attempt to wake you up, Caleb throws scalding McDonald's coffee in your face.")
        print("He accidentally kills you.")
        quit()

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
        is_alive = paths[i](DELAY, user)  # Runs each function in the paths list
        kill_if_dead(is_alive)
    end_story(user)


main()
