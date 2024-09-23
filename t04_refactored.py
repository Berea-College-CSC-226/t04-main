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
    '''https://docs.google.com/document/d/1sKZjkZLcneOgKSvRHJKCQrmaeie3n3Okpfr3FIo-avQ/edit
    Charle Ryland
    Eber Lima
    SOURCE:
    https://stackoverflow.com/questions/39746427/expression-can-be-simplified-on-boolean-literal'''
    user_direction = input("You come at across three tunnels.... (Choose forward, left, or right): ")
    sleep(delay)

    if user_direction == "left" or user_direction == "Left":
        print("You hit a den a bear lives in...")
        sleep(delay)
        print("You get scared and the alert the bear!")
        sleep(delay)
        print("The bear then eats you...")
        sleep(delay)
        print("You have a chance to survive...")
        number_picked = input("The Eggmeister asks you to pick a number between 1 and 20.")
        number_picked = int(number_picked)
        if number_picked >= 14:
            sleep(delay)
            return True
        elif number_picked < 14:
            sleep(delay)
            return False

    elif user_direction == "right" or user_direction == "Right":
        sleep(delay)
        print("You find an exit and reach a hill that overlooks a waterfall")
        print("Everything seems peaceful.")
        return True
    else:
        print("You walk forward...")
        sleep(delay)
        print("Nothing happens...")
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
    """ https://docs.google.com/document/d/14o_900GCeVZEadcvwv_15i2ZS8oINYH6bJigpeGAsV8/edit?usp=sharing
    Dalmar- Julio
    :return: none """


    direction = input("which direction do you want to go North/South/East/West")

    if direction.lower() == "north":
        # Bad choice! Sacrifice room!
        print("The north room is dimly lit by lanterns with red fire.")
        print("Five people in black robes are gathered around an altar.")
        print("Their argument quiets as you walk in.")
        sleep(delay)
        print("'Oh, how perfect,' one says. 'You have been Forgiven, Yuxila.'")
        print("Stone rises from the floor to block your exit.")
        sleep(delay)
        print("You are captured by the cultists. You are dead.")
        return False
    elif direction.lower() == "south":
        # Bad choice! Ritual room!
        print("You see a glowing circle on the floor. Robed figures stand around it and chant.")
        print("You do not recognize their words.")
        sleep(delay)
        print("A pressure builds in the room. It is too much.")
        print("Your heart bursts open inside your chest.")
        print("You are dead.")
        return False
    elif direction.lower() == "east":
        # Good choice! Dorms!
        print("The room you emerge into has a low stone ceiling. Bunked beds line the walls for fifty meters.")
        print("You walk carefully down the length of the room. Your breath is the loudest sound you hear.")
        sleep(delay * 2)
        print("At the end of the room is a kitchen and a door. There is no window.")
        print("You steel yourself and open the door as quietly as you can.")
        sleep(delay)
        print("The door leads outside. You are free.")
    elif direction.lower() == "west":
        # Neutral choice. Armory.
        print("This room is lined with weapons. Most are ornate daggers, hundreds of them hang on hooks lining the walls.")
        print("You see glowing runes on many of the daggers. Several do not have runes.")
        dagger = input("Do you take a dagger? [Yes/No]")
        if dagger == "Yes":
            print("You observe several daggers without runes. You take the one that looks unassuming.")
            print("The sound of a bell rings through the caves. You tense.")
            sleep(delay)
            print("Robed figures flood the room. You attempt to fend them off, but you are overwhelmed.")
            print("You are dead.")
            return  False
        else:
            print("This room looks suspicious. You return quietly to previous room.")


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
    """ https://docs.google.com/document/d/1pagGD80WeZZPtCu2rmhw_abLWuwZWWwVawAJnmNB794/edit?usp=sharing
        Janee Amig
        :return: none """

    print("You're a lonely parakeet stuck in her cage. \nYou urge for freedom... \nYou heard from the local birds about a revolution to overthrow the humans, and to live among bird kind.")
    sleep(delay*3)
    print("Maybe you should take their wisdom and try to escape. But how?")
    sleep(delay*2)
    print("Get your owner's attention.")
    peck = int(input("How many times do you want to peck? [Enter a number]"))

    if peck > 6:
        print("Your owner takes notices and goes to your cage.")
        sleep(delay)
        print("'Do you want out?'")
        choice = (input("[yes/no]"))
        if choice == "no":
            print("Your owner leaves. Dang it. You could of escaped. Why didn't you say yes? (Replay to try again.)")
        else:
            print("Your owner opens the cage door. You are now free!")
            sleep(delay)
            print("Almost...")
            sleep(delay)
            print("Your owner picks you up and starts to pet you.")
            print("Should you accept the pets or bite? (Doing nothing is yes/Biting is no.)")
            choice = (input("[yes/no]"))
            if choice == "no":
                print("You bite your owner... 'OW! Why Pebbles?' ")
                sleep(delay)
                print("Biting is nice... ")
                sleep(delay*3)
                print("You keep on biting your owner's fingers.")
                sleep(delay*3)
                print("Ah yes... bloodshed... ")
                sleep(delay*4)
                print("Anyways your owner banned you in your cage. (Replay to try again.)")
            else:
                print("You like it when your owner spoils you with pets.")
                sleep(delay*2)
                print("Your owner puts you down on the dining table, and opens the window to let some fresh air in. \nYour owner has left the window opened multiple times and knows that you won't escape.")
                sleep(delay*3)
                print("Or will you?")
                sleep(delay*4)
                print("Should you escape to be free or stay? Do you want to leave?")
                choice = (input("[yes/no]"))
                if choice == "no":
                    print("You stay along with your owner. ")
                    sleep(delay*2)
                    print("Maybe freedom another day...)")
                    sleep(delay*2)
                    print("At least your safe from the outside and spoiled on the inside. \nThough will your brothern hate you for not wanting freedom you wonder?")
                else:
                    print("You made the choice to get outside of the house...")
                    sleep(delay*3)
                    print("Are you stupid?")
                    sleep(delay*2)
                    print("You think you could survive out there as a domestic animal?")
                    sleep(delay*2)
                    print("You fly around and try to begin your journey.")
                    sleep(delay)
                    print("Unforntaunly you get picked on by the local birds and get turned into a snack.")
                    sleep(delay*3)
                    print("Replay to try again to get a better ending.")
    else:
        print("Your owner doesn't hear you. Maybe try again? (Replay to try again).")

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
