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
    pass
    # TODO Add your code here

###################################################################################


def team_18_adv(username):
    pass
    # TODO Add your code here

# TEAM 18
# TEAM 18 — fixed & simplified

import time

delay = 1.0
dead = False
rich = False

def pause():
    time.sleep(delay)

# ---- Choice 1 ----
way = input("Which path do you want to go? [Left, Right, Forward] ").strip().lower()

if way == "left":
    # Bad choice
    print("\nYou walked on the left path. This was the wrong way and you are stuck inside.")
    pause()
    print("You have no food and slowly starve.")
    dead = True

elif way == "right":
    # Neutral choice
    print("\nYou continue walking on the right path and nothing happens.")
    pause()
    print("At least you are still alive!\n")

elif way == "forward":
    # Good choice
    print("\nYou chose the path forward and found $1,000,000!")
    pause()
    print("You can do anything you ever wanted with all the money.\n")
    rich = True

else:
    print("\nYou stand still, confused. Let's pretend you went right.\n")

# If dead, end early
if dead:
    print("GAME OVER.")
else:
    pause()
    print("You walk out into an opening and see a man sitting down.")
    pause()
    print("He has a lot of things next to him including bread and a knife.")
    pause()
    print("Buy the knife, steal the bread, or continue?")
    way = input("What are you gonna do? [Buy, Steal, Continue] ").strip().lower()

    if way == "buy":
        # Good choice only if rich
        if rich:
            print("\nYou bought all the bread. You're not hungry anymore.\n")
            pause()
            print("You survive the day. NICE!")
        else:
            print("\nYou don't have enough money to buy all this bread.\n")
            pause()
            print("The guy thinks you're trying to steal it and kills you.")
            dead = True

    elif way == "steal":
        # Bad choice
        print("\nYou tried to snatch the bread.")
        pause()
        print("Before you can run, the guy shoots you in the back of the head.")
        pause()
        print("So... no bread! And you died!")
        dead = True

    else:
        # Neutral choice
        print("\nYou just ignore him and continue walking.\n")
        pause()
        print("You live to explore another day.")

    if dead:
        print("\nGAME OVER.")
    else:
        print("\nTHE END.")

# TODO Make sure to add the additional check if the user makes the "bad" choice!

# TODO Don't forget to check if your user is dead at the end of your chapter!



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