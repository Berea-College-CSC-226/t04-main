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
    pass
    # TODO Add your code here
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
    """
    https://docs.google.com/document/d/1tpBnsiVxtpcC6sO9debi_r0aZpjHUot1gZv7d1fg4jg/edit?usp=sharing
    Cody Bandy
    CJ Spencer
    :param username: the user's name
    :param delay: float representing pauses in the program
    :return: None
    """
    is_dead = False
    is_free = False
    is_stranded = False

    print("\n")
    print("Up ahead is a lit chamber with 3 doors, one to the East, one to the North, and one to the West.")
    cardinal = input("Which door will you choose?")

    if cardinal == "East":
        # GOOD !!!
        print("Fortune favors you! The door you have chosen is filled to the brim with treasures unimaginable in this world! Also, you see an exit just beyond the treasure!")
        is_free = True
        sleep(delay)

    elif cardinal == "North":
        # Might be a good choice
        print("Behind the door lies a small snake that upon seeing you starts to grow!")
        print("As you run away, the snake chases you as it continues to grow, expanding to fill everything behind you as your path ahead leads to a dead end...")
        sleep(delay)
        luck = random.randint(0, 10)
        if luck <= 5:
            print("There is no escape...")
            is_dead = True
        elif luck >= 6:
            print("As the snake grows, the cave roof starts to collapse onto it, killing the snake, and opening a path to freedom.")
            is_free = True

    elif cardinal == "West":
        # I mean you're not dead
        print("You are now in the middle of an island alone forever, enjoy !!!")
        is_stranded = True
        sleep(delay)

    if is_dead:
        print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    if is_free:
        print("You escaped, congrats!")
    if is_stranded:
        print("Well, you're still trapped but at least you're not dead. Try again?")
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
