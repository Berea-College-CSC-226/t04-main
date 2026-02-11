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
    if not is_alive:
        quit()


###################################################################################
###################################################################################

def scott_adventure():
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
###################################################################################
###################################################################################

def team_1_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_2_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_3_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_4_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_5_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_6_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_7_adv(username):


    """
     TEAM 7

     Guy is friendly and rescues us from the cave. They take you back to the town famed to have a secret treasury
     of unimaginable worth. but first, he takes you to a tavern. he offers you two drinks, one is poisonous
     and the other one contains elixir of the gods which grants you immortality.
     you can choose either one or you refuse to drink and missout on the treasure.

     if you choose the poison, the mage offers you another attempt at assessing your intelligence
     he asks if you would like something sweet with it?
     option 1, he gives you molly to add to the drink which removes the poisonous effect
     option 2, you refuse the molly and drink the poisonous drink and die
     option 3, you change your mind and decide to leave the tavern and start a new life of peace instead

    """
    delay = 1


    print("There seems to be someone in the cave with you. He has sensed your presence here")
    sleep(delay)
    print("The man assures you that you are safe and casts a spell on you")
    sleep(delay * 3)
    print("You wake up in a busy tavern")
    print("'I'm the mage responsible for the security of this locked city', he says")
    sleep(delay)
    print("everyone you see here is allowed to live by our supreme commander based on their intelligence")
    sleep(delay * 2)
    print("but you're a guest, so it's okay. Here, have a drink")

    sleep(delay)

    while True:
        drink = input("Accept the drink from the stranger? There are two drinks 'red/blue/decline'")
        if drink == "red":
            print("It tastes disgusting, but you feel fine")
            sleep(delay)
            print("a wonderful strength courses through your body. you feel rested to continue your adventure")
            sleep(delay)
            is_alive = True
            break
        elif drink == "blue":
            print("You can physically feel your stomach burning down")
            sleep(delay)
            print("You look to the mage and he smirks at you. 'You unworthy fool', he says")
            sleep(delay)
            print("Enjoy your sweet death, you are not worthy to live in our evil society")
            is_alive = False
            break
        elif drink == "decline":
            print("The mage looks at you with surprise")
            sleep(delay)
            print("This tavern is famous for its drinks. but it's okay if you wish to deprive yourself")
            is_alive = True
            break
        else:
            print ("Wrong response. Please choose red, blue, or decline")

    if not is_alive:
        print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")

    return is_alive


###################################################################################


def team_8_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_9_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_10_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_11_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def team_12_adv(username):
    pass
    # TODO Add your code here

###################################################################################


def main():
    """
    The main function, where the program starts. No modifications are needed here!
    :return: None
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