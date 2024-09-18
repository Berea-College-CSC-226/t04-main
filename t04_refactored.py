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
    return True
###################################################################################


def team_2_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_3_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_4_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_5_adv(username, delay):
    print("\n")

    chalice = input(
        "Hello intrepid explorer! You have stumbled upon The Flying Dutchman's lost treasure!" "\n"
        "Before you lie 4 colored chalices, however, you can only choose one."
        "Choose wisely! [Gold/Silver/Bronze/Brass]")
    chalice.lower()
    if chalice == "bronze":
        # Good choice!
        print(
            "Excellent choice, wise explorer! The Bronze chalice grants you a life filled with resilience and courage. You have proven to have a heart as unyielding as bronze! May you forge onwards with the spirit of a warrior.")
        sleep(delay)

    elif chalice == "gold":
        # Oh... Bad choice
        print("As you reach out and touch the gold chalice, a chilling breeze fills the cavern.")
        sleep(delay)
        print(
            "Suddenly, the cavern trembles and the chalice levitates, emitting a blinding light. " "\n"
            "A voice booms, 'Dare you to tempt fate? Roll the dice and let destiny decide your path.'")

        roll = int(input("Roll the dice (enter a number between 1 and 20): "))

        if roll <= 5:
            print("You roll the dice... it's a low number.")
            sleep(delay)
            print(
                "The ground shakes violently as the cave begins to collapse." "\n"
                "Unfortunately, you are unable to escape in time, meeting a tragic end." "\n"
                "The treasure remains unclaimed, lying amidst the ruins of the cavern.")

            return False
        elif roll <= 10:
            print("You roll the dice... it's a moderate number.")
            sleep(delay)
            print(
                "The cavern stops trembling and the path you came from reopens, allowing you a gracious yet narrow escape." "\n"
                "It appears you've been given a second chance, but the golden chalice remains elusive.")
        else:
            print("You roll the dice... it's a high number!")
            sleep(delay)
            print(
                "A hidden pathway illuminated by golden light suddenly appears, " "\n"
                "leading you to a secret chamber filled with unimaginable treasures." "\n"
                "It seems luck is on your side, brave explorer!")

    else:
        # Silver and Brass: Neutral choices
        print(
            "You find yourself wandering into a hidden cove within the cave," "\n"
            "the ground here is covered in sand and you can hear the distant sound of lost souls.")
        sleep(delay)
        print(
            "You see remnants of old pirate camps, " "\n"
            "and signs of many stories that remain untold in this isolated refuge of the Flying Dutchman's cavern.")

    # TODO Make sure to add the additional check if the user makes the "bad" choice!

    # TODO Don't forget to check if your user is dead at the end of your chapter!
    return True
###################################################################################


def team_6_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_7_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_8_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_9_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_10_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_11_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_12_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_13_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_14_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_15_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_16_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_17_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_18_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_19_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_20_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_21_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_22_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_23_adv(username, delay):
    pass
    # TODO Add your code here
    return True
###################################################################################


def team_24_adv(username, delay):
    pass
    # TODO Add your code here
    return True
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
