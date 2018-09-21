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
    # jamalie & juem
    # Refactored by nashab, stetzera
    #https://docs.google.com/document/d/17Yz7-0dx2HY8ysxpR5TYoAwOJzgdK63a0maeYIfQ8hM/edit?usp=sharing

    global dead           # You'll need this to be able to modify the dead variable

    direction = input("There is a river in your path, what would you do to cross the river? (Swim, Make a bridge,etc)")
    #this prompts user to pick a direction
    sleep(delay)
    if direction == "Make a bridge" or direction == "make a bridge":
    # this is the best choice!
        print("Well done, you have made a wise choice!")
        print("Your reward is that you will survive and explore more of the jungle!")
        sleep(delay)
    elif direction == "Swim" or direction == "swim":
    # surprisingly, this is a bad choice!
        print("Oh,no!! Just like Goblet of Fire, there are deadly mermaids looking for fresh blood!")
        print("You will be dragged down the ocean to be eaten at a feast!")
        sleep(delay*3)
        print("Now you're in their territory, you see some Gillyweeds just next to where you're trapped!")
        sleep(delay*3)
        print("You should be careful with eating Gillyweed")
        direction = int(input("You have the option to eat between 1-3 strands of Gillyweed, what will you do?"))
        if direction <= 2:
            # Good idea
            print("Good job! Now you have more strength and you can breath under water!")
            sleep(delay*3)
            print("Fight them and survive!")
        elif direction > 2 and direction <= 3:
            # this is a bad idea
            print("Too much Gillyweed will cause suffocation!")
            dead = True
            sleep(delay*5)
        else:
            # We would like the user to use whole number
            print("Since you did not choose from the given numbers, your only chance is to fight and survive.")
    else:
        # this is a neutral choice!
        print("Well done for the creativity! You crossed the river!")
        sleep(delay*3)
        print("But...")
        sleep(delay*3)
        print("You got injured for the hard work, so you can't move on and you need to rest by the river!")
        sleep(delay)

    if dead == True:
        print("oops.. I guess that's all for you!")
        sleep(delay*3)
        print("you were not very successful this time")
        sleep(delay*3)
        print("see you in your next journey")
        #This choice kills you

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
