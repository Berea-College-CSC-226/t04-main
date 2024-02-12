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

delay = 1.0  # change to 0.0 for testing/speed runs; larger for dramatic effect!
isDead = False


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
        "Congratulations, " +
        user +
        ", you have made it to the end of this... strange... adventure. I hope you feel accomplished.")
    print()
    print()
    print()
    sleep(delay * 5)
    print("Now go play again.")


def kill_if_dead(dead):
    """
    Simple function to check if you're dead

    :param dead: A boolean value where false lets the story continue, and true ends it.
    :return: None
    """
    if dead:
        quit()


###################################################################################
###################################################################################

def scott_adventure():
    """
    My original adventure text I gave as an example. Leave it alone as well.

    :return: None
    """
    global isDead  # You'll need this to be able to modify the dead variable
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
        isDead = True
    else:
        # Neutral choice
        print(
            '''You're in another part of the cave. It is equally dark, and equally uninteresting. 
            Please get me out of here!''')
        sleep(delay)

    kill_if_dead(isDead)


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
    """
    https://docs.google.com/document/d/1Dia-EWKe0B6cUXtTikF31o4zMbq7qywwdQU7uX0No8k/edit\
    Malak Mohamed
    Eric Sparks
    :return: none
    """
    print("\n")
    print("You find a room that contains two gold statues.")
    statues = input("Do you take the left or right statue, or don't pick up the statue? [left/right/none]: ")
    print("\n")
    is_dead = False
    if statues == "left":
        # good choice
        print("You pick up the statue on the left.")
        print("A passageway opens and you see outside.")
        print("Congrats! You escaped the cave!")
    elif statues == "right":
        # bad choice
        print("You pick up the statue on the right.")
        print("A passageway opens above you.")
        print("A bunch of snakes and spiders fall on you!")
        is_dead = True
    else:
        # neutral choice
        print("You don't pick up either of the statues.")
        print("Nothing happens... You are still stuck in the cave.")
    if is_dead:
        print("\n")
        print("One of the snakes asks you to pick a number 1 through 20.")
        number = int(input("Which number do you pick? (only put whole numbers): "))
        if number >= 13:
            print("Congrats! The snake decided to spare you!")
            is_dead = False
        else:
            print("You chose a wrong number, which angers the snake. He and the other snakes and spiders bite you!")
    if is_dead:
        print("Oh no! You died! Try again by hitting the green play button.")
        kill_if_dead(True)
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
    """
      https://docs.google.com/document/d/1_Mulz2V_XX3iT_2uww3kEXaV_afgQuEou-YcxEW0sHo/edit?usp=sharing
      Langston Hill
      Eric Cruz-Mendez

      starts/ continues the story
    """
    pass
    global isDead  # You'll need this to be able to modify the dead variable

    sleep(delay * 2)
    print()

    print("Up ahead is a lit chamber with 3 doors, one to the West, one to the North, and one to the East.")
    cardinal = input("Which door will you choose? [West/North/East]")
    print()
    if cardinal == "East":
        # GOOD !!!
        print("Fortune favors you!")
        print("The door you have chosen is filled to the brim with treasures unimaginable in this world!")
        print("You take what you can and continue your adventure. What else will you find?")
        print()
        sleep(delay)
    elif cardinal == "North":
        # Bad choice, feeling lucky?
        print("Behind the door lies a small snake that upon seeing you starts to grow!")
        print("As you run away, the snake chases you as it continues to grow")
        print("The snake expands to fill everything behind you as your path ahead leads to a dead end...")
        sleep(delay)
        luck = random.randint(0, 10)

        if luck <= 5:   # Worst Luck
            print("There is no escape...")
            isDead = True
        elif luck >= 8:  # Good Luck
            print("As the snake grows, the cave roof starts to collapse onto it")
            print("this kills the snake, but you are without the riches promised to you on this adventure")
            print("You pull the snakes fang from its maw as a small prize for your troubles ")
            print("You decide to press on")
            print()

        else:  # Bad Luck
            print("As you press against the wall, you feel it fade away")
            print("you are transported to nothingness as you slowly become part of it...")
            isDead = True
    else:
        # Neutral
        print("You enter the door and see the light of the bright sun beaming down on you")
        print("As you walk out and feel the warmth on your face, the cave behind you collapses")
        print("Unfortunately, you are in a closed off area.")
        print("you are surrounded on all sides with tall, impassable walls of dirt and stone")
        print("All that lies ahead is... an entrance to another cave...")
        print()
        print("The light of the warm sun has only strengthened your resolve and you decide to press on")
        print("You enter the second dark cave only to find yourself lost once again")
        print()
        sleep(delay)


    if isDead == True:
        print()
        print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
        kill_if_dead(isDead)


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
    """https://docs.google.com/document/d/13xlcbGqW_CVr6wpsi9CH2nEjf8Qk6_S0cyVs3417i_I/edit?usp=sharing
    Baella Morgan, Ariana Meatchem, Jaren Vessels"""
    global HasSword
    global goblindead
    ######Intro
    print("You stand in your makeshift campsite, a pitiful fire smoulders, sending black smoke to the sky.")
    sleep(delay)
    print("To the North: The Mystic Wood lies, fabeled to hold a great treasure.")
    sleep(delay)
    print("To the South: The Mouth of a cave, you can hear noises creep from within.")
    sleep(delay)
    print("To the West: A long road that you came from.")
    sleep(delay)
    print("To the East: A vast meadow of yellow flowers.")
    sleep(delay)
    ############
    direction = input("Choose a direction or action[Search the camp/North/South/East/West]: ")
    ###CHECK FOR VALID INPUT###
    while direction != "north" and direction != "south" and direction != "east" and direction != "west" and direction != "search camp":
        print("Now", username, " That wasn't a valid option.")
        direction = input("Choose a direction or action[Search the camp/North/South/East/West]: ")

    ###Print string based on input###
    if direction == "north":

            if goblindead == False:
               print("You go north.")
               sleep(delay)
               print("The trees tower over you almost nearly blocking out the sun.")
               sleep(delay)
               print("Suddenly a large goblin bandit jumps from the bushes roaring")
            sleep(delay * 3)
            ##check if user has sword
            if HasSword == True:
                print("The goblin lunges at you, your swords clash.")
                sleep(delay)
                print("You best the goblin, stabbing him in the chest.")
                print("You step over the goblins corpse, procceding deeper into the forest.")
                goblindead = True
                sleep(delay * 3)
                room2()

            elif HasSword == False:
                print("The goblin rushes you, pulling back his arm for a mighty swing.")
                print("His sword makes contact with your neck, chopping it clean off.")
                death()
        elif goblindead == True:
            print("You go north.")
            sleep(delay)
            print("The trees tower over you almost nearly blocking out the sun.")
            sleep(delay * 2)
            room2()

    elif direction == "south":
        print("You go south.")
        sleep(delay)
        print("You approach the cave, and as you enter you here a loud growl.")
        print("A vicious bear appreaches from the darkness.")
        sleep(delay * 3)
        if HasSword == True:
            print("You swing your sword, plunging it into the bear.")
            print("The bear screams in pain as it swats you like a fly, slinging against the cave wall.")
            print("Your head makes first contact with the wall, the blow kills you instantly")
            sleep(delay * 4)
            death()
        elif HasSword == False:
            print("The bear roars and swats you like a fly, slinging against the cave wall.")
            print("Your head makes first contact with the wall, the blow kills you instantly")
            death()
    elif direction == "east":
        print("You go east")
        room3()


    elif direction == "west":
        print("You look at the road to the west, this is where you came from.")
        sleep(delay)
        print("There's no turning back now. You must find the treasure hidden in the forest")
        sleep(delay)
        room1()

    elif direction == "search camp":
        print("You look around the camp for anything of interest.")

        sleep(delay)
        if HasSword == True:
            print("You don't see anything of interest - there's nothing here.")
            sleep(delay * 3)
            room1()
        elif HasSword == False:
            print("You find your sword laying on a rock near the fire.")
            print(">>sword obtained!<<")
            HasSword = True
            sleep(delay * 3)
            room1()

    else:
        room1()
    pass
    # TODO Add your code here

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


def main():
    """
    The main function, where the program starts. No modifications are needed here!
    :return: None
    """

    user = start_story()
    paths = [scott_adventure, team_1_adv, team_2_adv,
             team_3_adv, team_4_adv, team_5_adv,
             team_6_adv, team_7_adv, team_8_adv,
             team_9_adv, team_10_adv, team_11_adv,
             team_12_adv, team_13_adv, team_14_adv,
             team_15_adv, team_16_adv, team_17_adv,
             team_18_adv, team_19_adv, team_20_adv,
             team_21_adv, team_22_adv, team_23_adv,
             team_24_adv]
    random.shuffle(paths)  # Shuffles the order of paths, so each adventure is different

    for i in range(len(paths)):
        paths[i]()  # Runs each function in the paths list

    end_story(user)


main()
