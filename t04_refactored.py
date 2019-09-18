######################################################################
# Author: Scott Heggen      TODO: Change this to your names
# Username: heggens             TODO: Change this to your usernames
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

delay = 1.0  # change to 0.0 for testing/speed runs; larger for dramatic effect!
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
    print(
        "Congratulations, " + user + ", you have made it to the end of this... strange... adventure. I hope you feel accomplished.")
    print()
    print()
    print()
    sleep(delay * 5)
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
    global dead  # You'll need this to be able to modify the dead variable
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
        sleep(delay * 2)
        print("He eats you. You are delicious.")
        dead = True
    else:
        # Neutral choice
        print(
            "You're in another part of the cave. It is equally dark, and equally uninteresting. Please get me out of here!")
        sleep(delay)

    kill_if_dead(dead)


###################################################################################


def team_1_adv():
    pass
    # TODO Add your code here


def team_2_adv():
    ######################################################################
    # Author: Jose Zapata & Ben Maynard
    # Username: zapatamezaj & maynardb
    #
    # Assignment: T04: Adventure in Gitland
    #
    # Purpose: To recreate a choose-your-own-adventure style game
    # by refactoring T01.
    ######################################################################
    """
    Google Document Link:
    https://docs.google.com/document/d/1N2BXxH4VsnbuLDMHqq_gNpbawFb-_D3vbwr5oPuuR8g/edit?usp=sharing"""
    global dead
    print("Congratulations! \n"
          "You have survived so far. But the journey does not end for the gold still lays undiscovered. \n ")
    sleep(delay * 2)
    direction = input("Which way would you like to go now? Choose wisely North, East, West or South?\n")
    if direction == "East":
        # Good choice
        print("You have proven how worthy you are so the gods have decided to reward you with Gold. \n "
              "You are rich now go home and spread your wealth! \n")
    elif direction == "North":
        # Bad choice
        print("This trip is only for the worthy. You have been found unworthy and the gods have sacked your soul.\n")
        dead = True
    elif direction == "West":
        # Bad choice
        print("Some wolves come by and urinate all over your stuff, then eat your face off. \n"
              "Tragic, you could have been rich but now you're dead.")
        dead = True

    else:
        print("You were found by a group of robbers. They know you have enough food and gold to last you days. \n"
              "They loot you and leave you for the bears.")
        dead = True
    sleep(delay)
    kill_if_dead(dead)

    print("You're in the cave, its night time and you began to hear screams from one of two paths.")
    direction = input("Which path will you take, East or West? Choose wisely.")
    if direction == "East":
        print("""Congratulations! You have found the exit and have made it out with only a few scratches 
        and maybe some broken bones, but look on the bright side, at least you're alive.""")
    else:
        print("You become curious of the screams and follow them. \n"
              "You stumble upon a group of rich cave people that party and they invite you to join them")
    kill_if_dead(dead)


def team_3_adv():
    """
    Authors: Jeremy, Concepta
    Google Link: https://docs.google.com/document/d/1OFzXphHUyPa6YQpFq5rVqsW-1NFc8JwoCqsTKO79Lbw/edit?usp=sharing
    :return: N/A
    """
    username = input("What do you call yourself?")

    action = input_action()
    ask_action(username, action)

    sleep(delay)



def input_action():
    """
    Starts the story, asks user to select an option.
    :return: Returns the result of the variable 'action'.
    """
    print("You are being chased by a group of goblins.")
    print("You and your friend for some reason decide to run to a cliff. What do you do?")
    action = input("[Sleep | Jump | Do Nothing | Fight] ")
    return action


def ask_action(username, my_input):
    """
    This function will generate a set list of prompts based upon the my_input variable.
    :param username: Utilizes the users name in the print functions.
    :param my_input: Allows the user to input a finite selection of options to further the program.
    :return: N/A
    """
    if my_input == "sleep" or my_input == "Sleep":
        # Good choice
        sleep(delay)
        print("Amazing! Good job, ", username, "! You have found their weakness! Goblins can't see sleeping people...")
        sleep(delay)
        print("As you awake, you notice some golden coins one of the goblins left behind.")
        sleep(delay)
    elif my_input == "do nothing" or my_input == "Do nothing":
        # Bad choice
        print("Do nothing? YOU DIE!!!!")
        sleep(delay)
        if dead:
            print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
            kill_if_dead(dead)
    elif my_input == "fight" or my_input == "Fight":
        print("You have proved so brave", username, ". Go on with your journey!")
    elif my_input == "jump" or my_input == "Jump":
        print("At the bottom of this cliff lies waves of fast flowing water. Jumping was not a good choice!")
    else:
        print("The choice you entered is not available. Please enter a valid choice.")
# Finished, yay!


def team_4_adv():
    pass
    # TODO Add your code here


def test_the_rainbow(flavor):
    """
    Editors: Bryar Frank
             Shawn Villahermosa
     Function takes the input given by the user and checks to see if it is similar to one of the three options given.
     If it isn't, it returns "True" so the question can be repeated.
    :return: True
    """
    if len(flavor) == 9 and flavor[0] == "s" and flavor[8] == 'y':
        # Good choice!
        print("Good choice!This makes you feel a lot better")
        print("considering your friend disappeared mysteriously the other day.\n")
        sleep(delay)

    elif len(flavor) == 10 and flavor[0] == "p" and flavor[9] == 'o':
        # Neutral choice
        print("You feel a tingling sensation in your throat, and you start puking blood and pistachios.")
        print("As everything starts going black, you vaguely hear evil laughter. ")
        print("The ice cream van starts up and a merry song starts playing and slowly fades away \n")

    elif len(flavor) == 9 and flavor[0] == "c" and flavor[8] == 'e':
        # Oh... Bad choice
        print("Here you go, this is a van favorite!")
        sleep(delay)
        print("Oh it tastes so familiar but not in a good way")
        print("At first you don't realize it but then you start feeling nauseous")
        print("You start vomiting and ask 'What the hell was that?'")
        print("The ice cream people tells you: Don't worry! It's just your friend! \n")

        # Kill the player and end the program if this choice is made
        kill_if_dead(True)

    else:
        return True


def team_5_adv():
    """
    ######################################################################
    # Assignment: T04: Adventure in Gitland
    #    Editors: Bryar Frank
    #         Shawn Villahermosa
    #    Google Doc: https://docs.google.com/document/d/1icOBu4PV5DDGkWtmThEnmaj2JaOW1aoW9Yujh0_caLo/edit?usp=sharing
    ######################################################################
    :return:
    """
    typo = True

    while typo == True:
        flavor = input("Which flavor would you like? [Strawberry/Pistachio/Chocolate]")
        print()
        flavor.lower()
        typo = test_the_rainbow(flavor)
        if typo == True:
            print("Looks like the answer you provided isn't close to your choices")
            sleep(delay)
            print("Please try again unless you want to be stuck here forever... \n")


def team_6_adv():
    pass
    # TODO Add your code here


def team_7_adv():
    """
    https://docs.google.com/document/d/1Dh_Zd3X9bS8DijgocvDM0IqgX9UTT2eTzIUM_Pj_I-U/edit?ts=5d7ba1f3#heading=h.f6tumop9n7at
    :return: None
    """
    global dead
    direction = input("Which direction would you like to go? [Right/Forward/Backward/Left]")
    direction = direction.lower()  #changes the user's input to lowercase
    if direction == "right":
        # Good Choice!
        print("You rush into the nearby trees for cover. There you find a mystical coconut that will slay the dragon.")
        sleep(delay)
    elif direction == "forward":
        # Bad Choice
        integer = int(
            input(
                "You have made a bad choice! You have one more chance to avoid being burnt alive. Pick a number."))
        if integer <= 50:
            print("You have saved yourself and spared yourself from the dragon!")
        elif integer > 50:
            print("You failed to make a better decision and gave the dragon time to get the BBQ sauce.")
            print("You have decided to run towards the dragon. The dragon scoffs and burns you to a crisp.")
            dead = True
            kill_if_dead(dead)
            sleep(delay)
    else:
        pass
        # Oh...Bad Choice
        print("You reach the end of the cave uneventfully. Continue on!")





def team_8_adv():
    pass
    # TODO Add your code here


def team_9_adv():
    ######################################################################
    # Author: Taran Wells & Dakota Miller
    # Username: Wellst & Millerd2
    #
    # Assignment: T04: Adventure in Gitland
    #
    # Google docs: https://docs.google.com/document/d/1tQqF_Y0WmdpPVzTq3wAzf5_kX4x5tzHtdvdRv92qHp8/edit?usp=sharing
    ######################################################################

    death = False
    print("You see a dim light glowing behind a loose boulder. Do you choose to investigate?")
    choice = input("[Yes/no/leave]")
    sleep(delay)

    if choice == "Yes":
        print("You place your hand against the boulder and it dissipates into the air like fine mist. Behind it you")
        print("see a giant sword bigger than most men.")
        sleep(delay)
        print("A giant humanoid creature enters your view and begins to grab the sword.")
        sleep(delay * 2)
        print("He swings the sword in your direction causing the timid ceiling to collapse in between you saving ")
        print("yourself from the giant beast. ")
        print("You are safe for now, and you begin to search for a way out..")
        #
        #
        sleep(delay)
    elif choice == "no":
        print("You choose to hastily run away from the boulder and you begin to lose your footing.")
        sleep(delay)
        print("You trip and fall forward breaking your neck in the most boring possible fashion")
        death = True
    else:
        print("You decide against your gut and move away from the glowing boulder.")
        sleep(delay)
        print("You leave the cave by following the sounds of wilderness outside. You begin to hear some disgruntled")
        print("shuffling in the cave as you leave.")

    kill_if_dead(death)

    pass


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

####################################################################################################################


def team_14_adv():
    """
    Google Drive:   https://docs.google.com/document/d/1hVrBRHrbbXxCU74zEOyzQhHAzuYbB5O3eAddp6hoWnw/edit?usp=sharing
    Partner 1: Thy Nguyen
    Partner 2: Jenifer Fidelia
    :return:
    """


    global dead
    print("\nYou stumble into the woods. \nThere are three paths in front of you.\n")

    answer = input( "Which direction do you want to go? [North (N) /East (E) /West(W)] ")

    if answer.lower() == "north" or answer.lower() == "n":
        # Bad choice
        print("\n You are being chased by wolves.")
        sleep(1)
        print("Try to run away! Good luck!")
        sleep(1)
        safe = input("How long do want to run? [1-10]")
        try:
            a = int(safe)
            if int(safe) >= 7:
                print("\nThe wolves get tired of chasing you.")
            else:
                print("Oh no. They caught you.")
        except ValueError:
                print("\nOh no. They caught you.")
                dead = True
    elif answer.lower() == "west" or answer.lower() =="w":
        # Good choice
        print("You stumbled into a clearing. \nYou escape the woods.")

    elif answer.lower() == "east" or answer.lower() == "e":
        # Neutral choice
        print("The path leads you deeper into the woods. \nYou are now lost.")
    else:
        print("You can't think clearly. \nYou sit there for eternity.")
        dead = True

    if dead:
        kill_if_dead(dead)

    else:
        print("Keep going. You are still alive.")

############################################################################################################
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
    random.shuffle(paths)  # Shuffles the order of paths, so each adventure is different

    for i in range(len(paths)):
        paths[i]()  # Runs each function in the paths list

    end_story(user)


main()
