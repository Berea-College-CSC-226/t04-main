######################################################################
# Author: The Fall 2018 226 Class!
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
    """
    Team 6's refactored chapter.
    Originally by lovelle, refactored by lovelle.

    :return: None
    """

    global dead
    direction = input("Which direction would you like to go? [North/South/East/West] ")

    if direction == "East":
        # Good choice
        print()
        print("You come upon an underground lake, fed by a glistening stream.")
        print()
        print("The sound of the water soothes your troubled nerves.")
        sleep(delay)
        print()
    elif direction == "South":
        # Bad choice
        print()
        print("Ever so suddenly, you find yourself surrounded by ogres twice your size.")
        print("They realize you are harmless and you catch your breath. It seems they might let you pass...")
        sleep(delay * 5)
        print()
        print("They strike up a song, ready to continue on their way.")
        print("Oh, but how loud their voices are! And you aren't feeling so good...")
        sleep(delay * 5)
        print()
        print("The leader asks you to rank the quality of their singing, on a scale of 1 to 10.")
        rating = int(input("What do you say? Choose wisely; your life depends on it... "))
        print()
        if rating < 10:
            print("You fall to the ground, feeling the power of a cursed song. Looks like your time is up, friend.")
            dead = True
            sleep(delay)
            print()
        else:
            print("The ogre thanks you for the complement and sends you on your merry way.")
            sleep(delay)
            print()
    else:
        # Neutral choice
        print()
        print("Phew, you're still on solid ground. But still in the dark. Think fast!")
        sleep(delay)
        print()

    if dead == True:
        print("Oh no! You died. And what a shame it had to happen this way.")
        print("Better luck next time - try again by hitting the green play button!")
        quit()


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


def team_11_adv(): # Refactored by Team 11
    """
    https://docs.google.com/document/d/1trPAy_4RAI__kv4UXJYL8SUDABny1Yp-sSZgqdX9sFE/edit?usp=sharing
    :return:
    """

    direction = input("What will you do? [House/Cat/Sleep]")

    if direction == "House":
        # bad choice
        print("You decide that you need help and make your way towards the house. The path is a bit rocky though...")
        sleep(delay)
        print("...")
        sleep(delay)
        print("......")
        sleep(delay)
        print(".........")
        sleep(delay * 2)
        print("Oh no! You tripped on a rock! It was so shocking, you die before you hit the ground.")
        dead = True

    elif direction == "Cat":
        # neutral choice
        print("The cat is just so damn intriguing, you can't help but examine it.")
        print("You stretch out your hand, and the cat nuzzles you, its several tails twitching affectionately.")
        print("This is nice, but accomplishes nothing.")
        sleep(delay)
        print()
        print("You waste time loving the cat, but nothing gets done.")
        sleep(delay)
        dead = False

    else:
        print("You disregard that because you fell asleep.")
        sleep(delay * 5)
        print("You awake feeling refreshed.")
        dead=False

    if dead:
        print("What a sad way to die.")
        quit()


def main():
    print()
    print("To your left, you notice a house. Curious,... Looking around more, you see a cat behind you.")
    print("The cat has seven tails and a missing eye. You ponder for a moment. You feel sleepy.")
    sleep(delay * 2)
    print()
    team_11_adv()


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
