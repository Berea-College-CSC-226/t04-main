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
    pass

###################################################################################

def team_3_adv(username):
    pass

###################################################################################

def team_4_adv(username):
    pass

###################################################################################

def team_5_adv(username):
    pass
print("------ WELCOME TO THE TRANSPORT STATION -----")
sleep(1)
direction = input("Choose a direction to go [Japan, Ghana, Mongolia]: ")

if direction == "Mongolia":
    #Good choice
    print("YAYYYY!!!!")
    sleep(1)
    print("YOU GOT INTO GENGHIS KHAN'S ARMY...")
    sleep(1)
elif direction == "Japan":
    print("OHHH NOOO!!!")
    sleep(1 * 2)
    print("The moment you got on the island you heard footsteps from the dark jungle....")
    sleep(1 * 3)
    print("Ooops. They turns out to be a Samurai trying to hunt you down.")
    sleep(1 * 3)
    print("So after you see them you start running from them.")
    sleep(1 * 3)
    print("Then the Samurai overtakes you because they are fast.")
    sleep(1 * 3)
    print("And they pierce through your heart with their katana.")
    sleep(1 * 3)
    dead = True
else:
    #Neutral choice
    print("You are in Ghana now, and it's so hot. Go find some water....")
    sleep(1)
    dead = False

if dead == True:
    sleep(1 * 3)
    print()
    print()
    print("YOU DIED!!!!")
    sleep(1 * 3)
    print("BUT I GIVE YOU ONE MORE CHANCE")
    sleep(1 * 2)
    num1 = input("Choose a number between 1 and 20: ")
    num = int(num1)

    if num <= 6:
        print("You have been given a new life")
        direction = input("Choose a direction to go [USA, Finland]: ")

        if direction == "USA":
            print("YOU GOT SHOT BY A PERSON WITH A GUN")
            sleep(1 * 3)
            print()
            print("YOU DIED!!!!")
        else:
            print("YAY YOU HAVE FOUND THE ISLAND OF PEACE")
            sleep(1 * 2)
            print("NOW YOU CAN LIVE PEACEFULLY, GOODLUCK :)")
    else:
        print("OH NO YOU FAILED, NOW YOU ARE DEAD, THANKS FOR PLAYING.")
        quit()

sleep(1 * 4)
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