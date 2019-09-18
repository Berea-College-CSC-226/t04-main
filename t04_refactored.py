######################################################################
# Author: Scott Heggen      TODO: Change this to your names
# Username: heggens             TODO: Change this to your usernames
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
    pass
    # TODO Add your code here


def team_6_adv():
    pass
    # TODO Add your code here


def team_7_adv():
    pass
    # TODO Add your code here


def team_8_adv():
    pass
    # TODO Add your code here


def team_9_adv():
    pass
    # TODO Add your code here


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
    pass
    # TODO Add your code here


def team_15_adv():
    pass
    # TODO Add your code here

def check_if_exist(string):
    """
    Checks to see if the direction the user choose exists, and if it does it continues the story line.
    :param string:

    """
    global dead
    available_inputs = ["right", "left", "backwards", "forwards"]  # Directions the user can choose
    given_input = string.lower()

    if given_input in available_inputs:
        if given_input == "right":
            # Good Choice!
            print("You rush into the nearby trees for cover. There you find a mystical coconut that will slay the"
                  + " dragon.")
            sleep(delay)

        elif given_input == "forwards":
            # Bad Choice
            # print("You almost made a bad choice! The dragon hasn't seen you yet! Pick a number.")
            integer = int(
                input(
                    "You have made a bad choice! You have one more chance to avoid being burnt alive. Pick a "
                    + "number. [1,2]"))
            if integer == 1:
                print("You have saved yourself and spared yourself from the dragon!")
            elif integer == 2:
                print("You failed to make a better decision and gave the dragon time to get the BBQ sauce.")
                print("You have decided to run towards the dragon. The dragon scoffs and burns you to a crisp.")
                dead = True
                sleep(delay * 2)
                # Finished!
        else:
            # Oh...Bad Choice
            print("You just got eaten by man-eating roaches!")
            sleep(delay * 2)
            print("Try to pick another direction to follow next time!")
            dead = True
            # Finished the user has died!
    else:
        print("I do not exist, choose another direction...")
        ask()

def ask():
    """
    asks a question about which direction the user wants to go

    """
    x = input("Which direction would you like to go? [Right/Forwards/Backwards/Left]")
    check_if_exist(x)

def team_16_adv():

    ######################################################################################################
    # Author: Zyshavia Garrett and Abe Moreno

    # Username: garrettz and morenoa

    # Assignment: T04_Adventures in Gitland

    # Google Drive Link: smallyourl.appspot.com/B5odmlCDM

    # Acknowledgements:

    ######################################################################################################
    global dead                                                        # If user chooses wrong direction they will die

    ask()

    if dead:
        print("Oh no! You died. Better luck next time! Try again by hitting the green play button.")
        quit()


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
