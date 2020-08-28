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
    pass
    # TODO Add your code here


def team_8_adv():
    pass
    # TODO Add your code here


def team_9_adv():
    global dead

    '''https://docs.google.com/document/d/1bg_pi6Ppelk9sGmtS5xqqHhjRkDXVK-UUTnPVsqcTa8/edit?ts=5f47a454# 
    Tyler and Dimond'''

    print("")
    print("")
    print("You wake up on the top of a very tall mountain")
    print("A storm is approaching and you have to get down as soon as possible")
    print("In front of you there is a motorcycle and jeep")
    sleep(delay)
    print("")
    print("")
    print("You quickly have to make the decision if you would rather walk and slowly but safely get to safety")
    print("take the motorcycle that would be quicker but more dangerous or take the jeep that will travel slowly")
    print("over the terrain but can probably withstand the storm")
    print("")
    print("")
    transportation = input("What form of transportation would you prefer? [walk/motorcycle]")
    if transportation == "walk" or transportation == "Walk":
        print("You start your walk and everything seems okay, but you can see the storm catching up rapidly")
        print("After a few minutes the rain catches up to you but you don't start to worry because you may be able to "
              "find shelter before the lightning commences")
        sleep(delay)
        print("Lightening starts and you are dead")
        print("After the storm is over you're still stuck and you have to wait for help")
        dead = True
    elif transportation == "motorcycle" or transportation == "Motorcycle":
        print("As the storm approaches rapidly, you quickly hop on the fastest vehicle")
        print("You have a couple close calls but you outpace the storm and make it to safety")
    else:
        print("You're traveling down the mountain")
        print("It's been hours but you don't seem to be getting anywhere")
        print("You decide you are lost")
        print("You need to find help quick!")
        print("")
        sleep(delay)
    if dead:
        sleep(delay)
        print("Unfortunately the storms rough conditions were too much for you")
        quit()


def team_10_adv():
    # TODO Add your code here
    """
    Introduction text for the story. Don't modify this function.

    :return: the user's name, captured from user input
    """
    dead = False
    username = input("What do they call you?")
    print()
    print("welcome", username, "to the forest leading to Grandmothers house.")
    sleep(delay)
    print("You are walking to grandmas house, in front of you lies three paths")
    print("In front of you there are three paths. One leads you safely, one is a shortcut, one is undiscovered")
    print("Choose wisely")
    sleep(delay * 2)
    print("It is getting dark so she wants you to hurry")
    sleep(delay)
    direction = input("Which path do you choose to get to grandmas house? [1,2,3]")
    if direction == "1":
        # Correct choice!
        print("You made it to grandmas house safely, and you managed to miss the hungry werewolf")
        sleep(delay)
    elif direction == "2":
        # Wrong path
        print("Along the path you encounter something that blurs your vision.")
        sleep(delay)
        print("You try to react in time but you hear a growl and snarling getting closer behind you.")
        print("You see its a werewolf and try to run but he grabs you and eats you whole")
        dead = True
    else:
        # neutral choice
        print("Still walking on the path, yet to encounter the wolf.")
        sleep(delay)

    if dead:
        print("The wolf ate you, Better luck next time. Click the green button to try again")
        quit()
def team_11_adv():
    """
    https://docs.google.com/document/d/1v83lJRU74lZzMNxzVc4nde8knyPJXT86-anQnVaxyns/edit?usp=sharing
        Ala Qasem
        Ahmed Abdulahi

        :return: None
    """
    # TODO Add your code here
    global dead
    if direction == "North":
        print("The stranger recognises this part of the cave. They could come in handy. ")
        sleep(delay)
        print()
        print("You have come across another split in the cave. The other person is starting to act weird. ")
        print("You can go East or West. The stranger seems to want to go West, but do you trust them? Choose wisely. ")
        sleep(delay)
        print()

    trustworthy = input("Do you find them trustworthy enough to trust their advice to go West? [Yes/No]")

    # Good choice
    if trustworthy == "Yes":
        print("Lets hope this is the right thing to do...")
        sleep(delay)
        print("You find a chest")
        sleep(delay)
        print()
        print("You open it. It's filled with treasure!")
        sleep(delay)
        print()
        print("When you open the treasure, a boulder moves and reveals another path with light at the end.")
        print()
        sleep(delay * 3)
    # Bad Choice
    if trustworthy == "No":
        print("You decide to not trust the stranger and head East instead. ")
        sleep(delay * 2)
        print("The cave seems to be unstable and weak compared to the previous part of the cave.")
        sleep(delay * 2)
        print("The stranger sees a pretty rock in the cave side and decides to try and pull it loose. ")
        print()
        sleep(delay * 3)
        print(
            "The rock comes loose. Suddenly rocks start coming loose from the ceiling of the cave. The stranger started "
            "a collapse in the cave system.")
        print("You can't move fast enough to escape the falling rocks and get crushed. ")
        print()
        dead = True

    if dead:
        print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
        quit()


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

