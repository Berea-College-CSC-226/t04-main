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

    if is_alive is not None and is_alive == False:
        quit()

###################################################################################

def scott_adventure(username):
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

def team_1_adv(username):
    pass

###################################################################################

def team_2_adv(username):
    """
    https://docs.google.com/document/d/1zJS_Cxg4Jzp9z_NxLQ-2PFlvlQb04wrgZ4HA5WF6wFM/edit?usp=sharing
    Michael Damdinsuren
    Aryan Sehrawat
    """

    direction = input("Which direction would you like to go? [East/West]: ")

    if direction == "East":
        # Good choice!
        x = input("But don't worry, you're doing good, you've 2 paths in front of you. From first path you can hear the sound of water and the second path is full of Gems, make your choice wisely. Choose path 1 or 2?: ")

        sleep(DELAY)
        if x == "1":
            print("Great, you made it to the end of the story without dying! ")
            return True
        elif x == "2":
            print("Ah!!! there's the dragon of gems in front of you.")
            sleep(DELAY)
            print("You're dead(Loser😂)")
            print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
            return False

        else:
            print("Wrong input!")
            return True

    elif direction == "West":
        # Oh... Bad choice
        print("Oh there's some golden light to your left, can it be treasure or a way out")
        sleep(DELAY)
        print("and to your right it's still dark")
        y = input("Where will you go? right or left ")
        if y == "right":
            print("Wait, u see some light in front of you. ")
            sleep(DELAY)
            print("Booyah!! You made it to the end of the story without dying!")
            return True
        elif y == "left":
            print("OK sir you've jumped into the world of goblins")
            print("You're dead😂")
            sleep(DELAY)

            print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
            return False
        else:
            print("Wrong input!")
            return True

    else:
        x = input("You're in another part of the cave. Choose a path 1 or 2")
        if x == "1":
            print("Great, you made it to the end of the story without dying! ")
            return True
        elif x == "2":
            print("You fell in a pitt full of snakes")
            return False

        else:
            print("Wrong input!")
            return True



###################################################################################

def team_3_adv(username):
    pass

###################################################################################

def team_4_adv(username):
    # TEAM 4

from time import sleep

delay = 3.0

username = input("What is your name?")

print(username, "Is walking through the forest")
sleep(delay)
print("You see a bunch of people doing some sort of ritual around a campfire")
print("You have many choices to make")
sleep(delay)
print("Type ""A"" if you would like to hide behind a tree.")
print("Type ""B"" if you would like to make direct contact.")
print("Type ""C"" if you would like to turn around.")
sleep(delay)
direction = input("What are you going to do in this situation?")

if direction == "A":
    print("You hide behind a tree and watch from afar.")
    sleep(delay - 1.0)
    print("While you are behind the tree you overhear them talking about eating people")
    print("But for some reason there is an axe beside the tree you are hiding behind?")
    sleep(delay - 1.0)
    print()
    print("Type ""A"" if you want to grab the axe and make contact")
    print("Type ""C"" if you would like to go home.")
    behind_tree = input("Do you want to grab the axe and make direct contact or go home?")





elif direction == "B":
    print("You confronted them, and then they instantly kill you!")
    dead = True

elif direction == "C":
    print("You turn around a go home")
    dead = False

if behind_tree == "A":
    print("You go up to them and chop their heads off with axe.")
    print("Congrats you survived!")
    dead = False

elif behind_tree == "C":
    print("You turn around a go home")
    dead = False

#sleep(delay)
if dead == True:
    print("They turned out to be cannibals and they eat you.")
if dead == False:
    print("You are really smart, you weren't taking any chances of dying.")

###################################################################################

def team_5_adv(username):
    pass

###################################################################################

def team_6_adv(username):
    pass

###################################################################################

def team_7_adv(username):
    pass

###################################################################################

def team_8_adv(username):
    pass

###################################################################################

def team_9_adv(username):
    pass

###################################################################################

def team_10_adv(username):
    pass

###################################################################################

def team_11_adv(username):
    pass

###################################################################################

def team_12_adv(username):
    pass


###################################################################################


def main():
    """
    Choose your own adventure!
    """
    paths = [scott_adventure, team_1_adv, team_2_adv,
             team_3_adv, team_4_adv, team_5_adv,
             team_6_adv, team_7_adv, team_8_adv,
             team_9_adv, team_10_adv, team_11_adv,
             team_12_adv]
    # Shuffles the order of paths, so each adventure is different
    random.shuffle(paths)

    user = start_story()
    for i in range(len(paths)):
        is_alive = paths[i](user)  # Runs each function in the paths list
        kill_if_dead(is_alive)

    end_story(user)


if __name__ == "__main__":
    main()