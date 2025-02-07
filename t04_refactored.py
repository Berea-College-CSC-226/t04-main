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

def team_1_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_2_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_3_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_4_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_5_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_6_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_7_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_8_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_9_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_10_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_11_adv():
    pass
    # TODO Add your code here

###################################################################################

def team_12_adv():
    '''
    https://docs.google.com/document/d/1m20wqB7tPGW-MBtkiPPx4iQ3e2S5_ZisYlOv08lGwg4/edit?usp=sharing
    Gavin Miller
    Bryanna Moreno Casas
    :return: none
    '''

    direction = input("[Tavern/Inn/Reform/Run]")

    def direction_inn():
        if direction == "Inn":
            # Good choice!
            print("You wander into an Inn, where a gambling man at a corner table offers you "
                  "a gold nugget in exchange for playing a game of Russian Roulette.")
            sleep(DELAY)
            print("Upon closer inspection you realize the revolver's chambers are all full. "
                  "Regardless, you choose to entertain the idea.")
            print()
            '''
            Executes if inn is chosen
            '''

    def tavern():
        if direction == "Tavern":
            # Good choice!
            print("Although you referred to the building as a tavern initially, closer inspection reveals to you"
                  "that this particular subset of business is referred to as a 'saloon' in a western context.")
            sleep(DELAY)
            print()
            if direction == "Saloon":
                # Good choice!
                print(
                    "In your infinite wisdom you have chastised the narrator for their improper use of the term 'tavern'."
                    "He notes this and allows you to carry on.")
                sleep(DELAY)
                '''
                Executes if tavern is chosen
                '''

    def run():
        if direction == "Run":
            # Oh... Bad choice
            print("Your reputation proceeds you. Such is the shame of your cowardice that "
                  "you immediately suffer psychological strain.")
            sleep(DELAY)
            print("Like that television scene from the next century's hit movie 'Scanners' your "
                  "brain expands and presses against the wall of your skull.")
            sleep(DELAY * 2)
            print("Your death is instantaneous and cheesy as all get-out, yet you can't help but "
                  "wonder what impact your inexplicable headsplosion will have on creative writing "
                  "going into the future.")
            dead = True
        '''
        Executes if run is chosen, user dies
        '''

    def reform():
        if direction == "Reform":
            # Oh... Bad choice
            print("The powers of camaraderie, friendship and all adjacent terms for socially "
                  "agreeable behaviour come together to stop your tyranny before it begins.")
            sleep(DELAY * 2)
            print("Unfortunately, this also means you lose control of the player character.")
            sleep(DELAY * 2)
            print("They die of natural causes, lead poisoning, shortly after attempting "
                  "to intervene in a bank robbery sometime in the year 1890.")
            dead = True

    def when_dead():
        # Neutral choice
        sleep(DELAY)
        if dead == True:
            sleep(DELAY * 2)
            print("You are dead. This was probably fully deserved.")
            print("Hopefully the metaphysical emissary intervenes on your behalf in the Yama's courtroom.")
            print("Oh wait, nevermind, you've already been pardoned. Please restart.")
            quit()

    def main():
        direction_inn()
        tavern()
        run()
        reform()

    main()

###################################################################################


def team_13_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_14_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_15_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_16_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_17_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_18_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_19_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_20_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_21_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_22_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_23_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_24_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_25_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_26_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_27_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_28_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_29_adv():
    pass
    # TODO Add your code here

###################################################################################


def team_30_adv():
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
             team_12_adv, team_13_adv, team_14_adv,
             team_15_adv, team_16_adv, team_17_adv,
             team_18_adv, team_19_adv, team_20_adv,
             team_21_adv, team_22_adv, team_23_adv,
             team_24_adv, team_25_adv, team_26_adv,
             team_27_adv, team_28_adv, team_29_adv,
             team_30_adv]
    # Shuffles the order of paths, so each adventure is different
    random.shuffle(paths)

    user = start_story()
    for i in range(len(paths)):
        is_alive = paths[i]()  # Runs each function in the paths list
        kill_if_dead(is_alive)
    end_story(user)


main()
