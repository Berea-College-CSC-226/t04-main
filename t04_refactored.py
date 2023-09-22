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
###################################################################################
###################################################################################

def team_1_adv():
    delay = 1.0
    dead = False


    username = input("What is your name?")
    print()
    print("welcome", username, "to fruit Land")
    sleep(delay * 2)
    print("you will be given three fruits and you can only choose one")
    print("Be careful the choice you make ")
    print("one will give you fortune, one will lead to death, and one is just a normal fruit")
    print()
    sleep(delay * 2)


    Fruit = input("which fruit would you like? [Banana, Orange, Apple] ")

    if Fruit == "Banana":
        print()
        print("unfortunately, you've chosen the rotten fruit, this is the end of your journey!")
        print()
        dead = True
    elif Fruit == "Orange":
        print()
        print("you've chosen the special fruit, you will have fortune and fame! ")
        print()
    elif Fruit == "Apple":
        print()
        print("you've chosen a normal fruit, you live! ")
        print()

    kill_if_dead(dead)
    # Leke
    #Chretien
    #https://docs.google.com/document/d/1QXaA19nUNTicZsD25AjPtgX2wO0SwZ51sTZ3tB-nnEc/edit?usp=sharing

def team_2_adv():
    pass
    # TODO Add your code here


def team_3_adv():
    pass
    # https://docs.google.com/document/d/1cCI6qJccAZ0a4aUYRP5WJ6cyT9KNFdgn6KnQnzzbKg8/edit?usp=sharing
    # Nancy Alvarado
    # Katherine Ayala
    global dead
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
        dead = True
        sleep(delay)
    else:
        # neutral choice
        print("You don't pick up either of the statues.")
        sleep(delay)
        print("Nothing happens... You are still stuck in the cave.")
        sleep(delay)

    # TODO Make sure to add the additional check if the user makes the "bad" choice!
    if dead:
        print("\n")
        print("One of the snakes asks you to pick a number 1 through 20.")
        sleep(delay)
        number = int(float(input("Which number do you pick? (only put whole numbers): ")))
        sleep(delay)
        if number >= 13:
            print("Congrats! The snake decided to spare you!")
            dead = False
            sleep(delay)
        else:
            print("You chose a wrong number, which angers the snake. He and the other snakes and spiders bite you!")

    # TODO Don't forget to check if your user is dead at the end of your chapter!
    if dead:
        print("Oh no! You died! Try again by hitting the green play button.")


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


def team_16_adv():
    pass
    # TODO Add your code here


def team_17_adv():
    pass
    # TODO Add your code here


def team_18_adv():
    pass
    # TODO Add your code here


def team_19_adv():
    """
    https://docs.google.com/document/d/1OEkYdYu1uXsIGk77mEY_yK1mmmlWFkW2xxwdVSZasCI/edit
    Sam Edelman
    Destiny White
    """
    dead = False
    username = input("What is your name? ")
    print()
    sleep(delay * 2)
    print("Welcome", username, "to Fruit Land!")
    print("You will be given the choice of three fruits and you can only choose one...")
    print("Be careful the choice you make!")
    print("One will give you fortune, one will lead to death, and one is just a normal fruit.")
    sleep(delay * 2)

    fruit = input("Which fruit would you like? [Banana, Orange, Apple] ")

    if fruit == "Banana":
        print("Unfortunately, you've chosen the rotten fruit, this is the end of your journey!")
        dead = True
    elif fruit == "Orange":
        print("You've chosen the special fruit, you've earned long-lasting prosperity!")
    else:
        print("Yummy! But not few and far between in these lands.")
    kill_if_dead(dead)

def team_20_adv():
    pass
    # TODO Add your code here


def team_21_adv():
    pass
    # TODO Add your code here


def team_22_adv():
    pass
    # TODO Add your code here


def team_23_adv():
    pass
    # TODO Add your code here


def team_24_adv():
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
             team_18_adv, team_19_adv, team_20_adv,
             team_21_adv, team_22_adv, team_23_adv,
             team_24_adv]
    random.shuffle(paths)                               # Shuffles the order of paths, so each adventure is different

    for i in range(len(paths)):
        paths[i]()                                      # Runs each function in the paths list

    end_story(user)


main()

