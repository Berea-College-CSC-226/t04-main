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
    print("Welcome,", user, ", to the labyrinth!")
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
    print("Congratulations, " + user + ", you have made it to the end of this... strange... adventure. "
                                       "I hope you feel accomplished.")
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
        print("You're in another part of the cave. "
              "It is equally dark, and equally uninteresting. Please get me out of here!")
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

    # TODO Add your code here
    """https://docs.google.com/document/d/10pEc9bcpgOZhSS1SZtIzj-PTrpJctsmpJ8HEyq_491I/edit?usp=sharing, 
        nakajk, stewartd"""
    user = input("What do they call you, unworthy adversary? \n")
    print("Welcome,", user, ", to the labyrinth!")
    print("Suddenly the earth beneath you rumbles..out of thin air three radiant portals emerge. \n")
    sleep(delay*2)
    print("The light from the portals illuminates the cave"
          ",but you reflexively close your eyes in response to the harsh light. \n")
    print("Few minutes pass and attempt again to get a better look at the portals."
          "Light permeates through your partially opened eyes."
          "To your surprise, the portals each lead to luxury stores. \n")
    sleep(delay*2)
    print("A voice bellows to you, leaving you slightly shaken. \n")
    sleep(delay*2)
    print("Choose your luxury store wisely, unworthy adversary! \n")
    store = input("Which store would you like to go? [Gucci / Chanel / Prada]")
    if store == "Gucci" or "gucci" or "GUCCI":
        # Bad choice
        print("Welcome to the Gucci store,", user, "!")
        print("You begin to search for your wallet...")
        wallet_location = input("Where is your wallet? [Pocket/Purse/Hand]")
        if wallet_location == "Pocket" or "Purse" or "pocket" or "purse" or "POCKET" or "PURSE":
            print("Tough luck! You do not have any money! Please leave the store!")
        elif wallet_location == "Hand":
            print("You just spent $100,000 at Gucci...Your mom killed you!"
                  "Please wear black at the funeral.")
            quit()
    elif store == "Chanel" or "chanel" or "CHANEL":
        sale = input("Chanel is having a massive sale! Which items are you buying? [Shirts/Purses/Perfumes]")
        if sale == "Shirts" or "shirts" or "SHIRTS" or "Purses" or "purses" or "PURSES" or "Perfumes" or "perfumes" or \
                "PERFUMES":
            print("You got over $40,000 worth of luxury items, for only $10,000. \n You are so lucky!!!")
    else:
        print("You have entered Prada.")
    if store == "Prada" or "PRADA" or "prada":
        print("Welcome to Prada,", user, "!" "Let me check to see if you have a membership with us? \n")
        sleep(delay*2)
        print("It appears that you do not have a membership with us..")
        sleep(delay*2)
    enroll = input("Would you like to enroll?[Yes/No]")
    if enroll == "Yes" or "yes" or "YES":
        print("The entry fee is $3000 and we have many on sale.\n")
        print("Thank you for your membership!")
        print("You shop around the store and gather your items and prepare to pay.. \n")
        sleep(delay*2)
        print("Welcome 50th customer, as a reward all of your items are free of charge!")
    elif enroll == "No" or "no" or "NO":
        print("Thank you for your time. \n")
        sleep(delay)
        print("As you make your way out of the store, a loose the ceiling of slap breaks apart from the topmost floor"
              "and it instantly flattens you. \n")
        print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
        quit()


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
