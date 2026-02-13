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
    pass
    # TODO Add your code here

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
    """https://docs.google.com/document/d/1W5mC3XMPa480TuDvvviUeIod912K9bwWdHfV991FpFc/edit?usp=sharing
    Mateo Andrade
    Neelima Matcha
    :return: True or False
    """
    # Mateo and Neelu are working on this function! :)

    direction = input("Where are you going? (Please just choose North) ")
    dead = False

    if direction == "North":
        print("You see an old man with three strands of fine gray hair. He seems to be blind. What should you do?")
        print('''A: Leave him alone in the cave
B: Approach him and ask him how to get out of this cave''')
        answer1 = input("Write the letter of your answer (A or B): ")
        if answer1 == "A":
            print("You are now forever trapped in the cave. Congrats.")
            dead = True
        elif answer1 == "B":
            print("The man growls. He can feel your presence, but apparently, he's also deaf. What should you do?")
            print('''A: Run away.
B: Run away!!!! ''')
            answer2 = input("Write the letter of your answer (A or B): ")
            print("The man says, 'How dare you leave me, lad? You'll pay for what you did to me!'")
            if answer2 == "A":
                print("He stands up and quickly comes up to you, jabbing your back until you die.")
                dead = True
            if answer2 == "B":
                print("He stands up and tries to run after you, but he accidentally breaks his ankle. He can't move, so you just run away.")
                print("Apparently, you see some light somewhere in the cave. You approach the light, and you see three doors. The doors have numbers on them?")
                number = input("Which door should you choose? 5, 6, or 7? ")
                if number == "6":
                    print("This is the wrong door. It shuts behind you, trapping you forever.")
                    dead = True
                elif number == "5":
                    print("Wow! Door 5 was actually the entrance to the underground shelter, and you find very friendly people, who lead you out of the cave.")
                    print("YOU HAVE ESCAPED THE CAVE!!! CONGRATS 🎉🎉🎉🎉🎉")
                elif number == "7":
                    print("The door suddenly closes, and you feel that your body elevates upward to heaven.")
                    dead = True
        else:
            print("I don't know WHAT you mean, but the old man noticed your presence. He runs to you and stabs you. You are DEAD!")
            dead = False
    else:
        print(
            "You see a ghost telling you that the only way out is the North. The ghost heads you to \nthe North of the cave. You see an old man with three strands of fine gray hair. He talks to the ghost and takes off his knife, stabbing you into your heart. You're dead :(")
        dead = True

    return dead


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