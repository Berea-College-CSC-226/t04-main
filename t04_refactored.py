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


def start_story(delay):
    """
    Introduction text for the story.
    Don't modify this function.

    :param delay: float representing pauses in the program
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


def end_story(user, delay):
    """
    This is the ending to the story.
    Don't modify this function, either.

    :param user: the user's name
    :param delay: float representing pauses in the program
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

def scott_adventure(username, delay):
    """
    My original adventure text I gave as an example. Leave it alone as well.

    :param username: the name of the user
    :param delay: float representing pauses in the program
    :return: None
    """

    direction = input(
        "Which direction would you like to go, " + username + "? [North/South/East/West]")

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
        return False     # kill the user!
    else:
        # Neutral choice
        print(
            '''You're in another part of the cave. It is equally dark, and equally uninteresting. 
            Please get me out of here!''')
        sleep(delay)
    return True       # User survives all other scenarios


###################################################################################
###################################################################################
###################################################################################

def team_1_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_2_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_3_adv(username, delay):
    print("\n")
    print("You find a room that contains two gold statues.")
    sleep(delay)
    statues = input("Do you take the left or right statue, or don't pick up the statue?: ")
    print("\n")

    if statues == "left":
        # good choice
        print("You pick up the statue on the left.")
        sleep(delay)
        print("A passageway opens and you see outside.")
        print("Congrats! You escaped the cave!")
        sleep(delay)
    elif statues == "right":
        # bad choice
        print("You pick up the statue on the right.")
        sleep(delay)
        print("A passageway opens above you.")
        sleep(delay)
        print("A bunch of snakes and spiders fall on you!")
        isDead = True
        sleep(delay)
    else:
        # neutral choice
        print("You don't pick up either of the statues.")
        sleep(delay)
        print("Nothing happens... You are still stuck in the cave.")
        sleep(delay)

    # TODO Make sure to add the additional check if the user makes the "bad" choice!
    if isDead == True:
        print("\n")
        print("One of the snakes asks you to pick a number 1 through 20.")
        sleep(delay)
        number = int(float(input("Which number do you pick? (only put whole numbers): ")))
        sleep(delay)
        if number >= 13:
            print("Congrats! The snake decided to spare you!")
            isDead = False
            sleep(delay)
        else:
            print("You chose a wrong number, which angers the snake. He and the other snakes and spiders bite you!")

###################################################################################


def team_4_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_5_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_6_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_7_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_8_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_9_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_10_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_11_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_12_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_13_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_14_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_15_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_16_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_17_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_18_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_19_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_20_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_21_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_22_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_23_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def team_24_adv(username, delay):
    pass
    # TODO Add your code here

###################################################################################


def main():
    """
    The main function, where the program starts. No modifications are needed here!
    :return: None
    """
    delay = 1.0  # change to 0.0 for testing/speed runs; larger for dramatic effect!

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

    user = start_story(delay)
    for i in range(len(paths)):
        is_alive = paths[i](user, delay)  # Runs each function in the paths list
        kill_if_dead(is_alive)
    end_story(user, delay)


main()
