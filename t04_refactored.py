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
###################################################################################
###################################################################################

def team_1_adv():
    pass
    # TODO Add your code here


def team_2_adv():
    pass
    # TODO Add your code here


def team_3_adv():
    """
    https://docs.google.com/document/d/1cCI6qJccAZ0a4aUYRP5WJ6cyT9KNFdgn6KnQnzzbKg8/edit?usp=sharing
    Nancy Alvarado
    Katherine  Ayala
    """
    global dead
    print("\n")
    print("You find a room that contains two gold statues.")
    sleep(delay)
    statues = input("Do you take the left or right statue, or don't pick up the statue?: ")
    print("\n")

    if statues == "left":
        # good choice
        print("You pick up the statue on the left.")
        sleep(delay)
        print("A passageway opens and you see outside.")
        print("Congrats! You escaped the cave!")
        sleep(delay)
    elif statues == "right":
        # bad choice
        print("You pick up the statue on the right.")
        sleep(delay)
        print("A passageway opens above you.")
        sleep(delay)
        print("A bunch of snakes and spiders fall on you!")
        dead = True
        sleep(delay)
    else:
        # neutral choice
        print("You don't pick up either of the statues.")
        sleep(delay)
        print("Nothing happens... You are still stuck in the cave.")
        sleep(delay)

    # TODO Make sure to add the additional check if the user makes the "bad" choice!
    if dead:
        print("\n")
        print("One of the snakes asks you to pick a number 1 through 20.")
        sleep(delay)
        number = int(float(input("Which number do you pick? (only put whole numbers): ")))
        sleep(delay)
        if number >= 13:
            print("Congrats! The snake decided to spare you!")
            dead = False
            sleep(delay)
        else:
            print("You chose a wrong number, which angers the snake. He and the other snakes and spiders bite you!")

    # TODO Don't forget to check if your user is dead at the end of your chapter!
    if dead:
        print("Oh no! You died! Try again by hitting the green play button.")


def team_4_adv():
    pass
    # TODO Add your code here


def team_5_adv():
    """
    Bryanna Erickson
    Joyce Mukalamusi
    https://docs.google.com/document/d/1an5cbwsTIszH1yi1xa67ASP3e2HQ64IzTn83y70kgzI/edit?usp=sharing
    """
    # TODO Add your code here
    global dead
    print("\n")

    dead = False
    print("Hello intrepid explorer! You have stumbled upon The Flying Dutchman's lost treasure!")
    print("Before you lie 4 colored chalices, however, you can only choose one.")
    chalice = input("Choose wisely![Gold/Silver/Bronze/Brass]")

    if chalice == "Bronze":
        # Good choice!
        print("Excellent choice, wise explorer!")
        print("The Bronze chalice grants you a life filled with resilience and courage.")
        print("You have proven to have a heart as unyielding as bronze!")
        print("May you forge onwards with the spirit of a warrior.")
        sleep(delay)

    elif chalice == "Gold":
        # Oh... Bad choice
        print("As you reach out and touch the gold chalice, a chilling breeze fills the cavern.")
        sleep(delay)
        print("Suddenly, the cavern trembles and the chalice levitates, emitting a blinding light.")
        print("A voice booms, 'Dare you to tempt fate? Roll the dice and let destiny decide your path.'")

        roll = int(input("Roll the dice (enter a number between 1 and 20): "))

        if roll <= 5:
            print("You roll the dice... it's a low number.")
            sleep(delay)
            print("The ground shakes violently as the cave begins to collapse.")
            print("Unfortunately, you are unable to escape in time, meeting a tragic end. ")
            print("The treasure remains unclaimed, lying amidst the ruins of the cavern.")
            dead = True
        elif roll <= 10:
            print("You roll the dice... it's a moderate number.")
            sleep(delay)
            print("The cavern stops trembling and the path you came from reopens, allowing you a gracious escape.")
            print("It appears you've been given a second chance, but the golden chalice remains elusive.")
        else:
            print("You roll the dice... it's a high number!")
            sleep(delay)
            print("A hidden pathway illuminated by golden light suddenly appears.")
            print("This leads you to a secret chamber filled with unimaginable treasures.")
            print("It seems luck is on your side, brave explorer!")

    else:
        # Neutral choice
        print("You find yourself wandering into a hidden cove within the cave.")
        print("The ground here is covered in sand and you can hear the distant sound of lost souls.")
        sleep(delay)
        print("You see remnants of old pirate camps.")
        print(
            "There are signs of many stories that are untold in this isolated refuge of the Flying Dutchman's cavern.")

    kill_if_dead(dead)


def team_6_adv():
    """
    This makes the adventure choose which path they would like to embark on.
    Authors : Su Meh, Diliara Galieva
    Usernames : mehs, galievad
    https://docs.google.com/document/d/1XnrVcyAhCpQKZg5ZYEVoCZxQEXxvSNOm2K7M4Emmtkc/edit?usp=sharing
    :return:
    """

    Path = input("Which path will you take? [Left/Middle/Right]")

    if Path == "Left":
        # Wrong Path
        print("Sss....sss...sss...")
        sleep(delay)
        print("You have encountered a python.")
        print("Oh no! The python has bitten you.")
        print("You are now slowly dying from the poison.")
        kill_if_dead(dead)


    elif Path == "Middle":
        # Neutral Path
        print("The path is never-ending.")
        print("You continue walking through the cave.")

    else:
        # Correct Path
        print("drip...drip...drip")
        print("You arrived at a water faucet and met a fellow adventure!")
        print("You can now continue your adventure.")
        sleep(delay)

    kill_if_dead(dead)

def team_7_adv():
    """
    https://docs.google.com/document/d/1ksWilu6oBRWPoa5kZo2jyzkAOiAKqwtHYfMWGK7d27M/edit
    Hira Karim
    Claudia Pulido
    :return:
    """
    direction = input("Go with him further [Up, or Down]?")
    if direction == "Up":
        print("You've reached a large vault... a large console stands to its right...")
        print("The console lights up when you reach it... it asks for a passcode")
    else:
        if direction == "Down":
            print("you have reached the strongest creature in all of the lands..")
            sleep(delay * 3)
            print("It is the Teacher Assistant Silas! Do you fight or run?")
    answer = input("Ask for help or guess the code")
    if answer == "Ask for help":
        print("You ask Dr. Heggen for help")
        print("He pulls out a small electrical device and plugs it into the console")
        print("The console glows green and the vault opens up")
        print("you've found riches beyond your wildest dreams")
    elif "Guess the code":
        print("You type in '12345' and the console turns red")
        print("The walls close in on you, crushing you like a Wookie in a trash compactor")

    kill_if_dead(dead)

def team_8_adv():
    pass
    # TODO Add your code here


def team_9_adv():
    """
    https://docs.google.com/document/d/16JKlfHHU099gqHi_H4jkxpVHTIAot5AIVQJffD4_23Q/edit?usp=sharing
    Remi White
    Lizzie Manabat
    :return: none
    """
    dead = False
    direction = input("Which direction would you like to go? [North/South]")

    if direction == "North":
        print("Now you have to complete three treacherous trials with the other person in the cave.")
        print("Each more arduous than the last.")
        kill = input("The first trial is you must befriend and then destroy a sneaky salamander. [Yes, No]")

        if kill == "Yes":
            print("Congratulations you can proceed to the next trial. ")
            print("The next trial you have to go find the other person in the cave with you.")
            print("You make them poke a grizzly bear. [Yes, No]")

        elif kill == "No":
            print("Due to your declination, you will now be forced to leave the labyrinth.")
            dead = True

    # picking the neutral choice
    else:
        # neutral choice
        print("Now you are presented with two choices.")
        print("One direction could lead to your death and the other solution is unknown")

    kill_if_dead(dead)
    # TODO Add your code here


def team_10_adv():
    pass
    # TODO Add your code here


def team_11_adv():
    """https://docs.google.com/document/d/1W-UPVLjpRIZoil4edlCxl8Dkjj91P0ky9xb35G1L55g/edit?usp=sharing
    Frederick Oguine
    Yin Kyay Wai
    :return: none
    """

    delay1 = 2.0
    dead1 = False

    username = input("Hello player, why don't you start off by telling us what your favorite color is? ")

    print("Ok player! You will be driving a", username, "car.")

    sleep(delay1)

    print("You're heading to Walmart and you're low on gas, make the right turns to the gas station to fuel up!")
    print("\n")
    sleep(delay1)

    direction = input(
        "You're pulling up to Main st, the light is green. "
        "Would you like to take a left or right? [Left/Right/Continue] ")

    if direction == "Left":
        # Correct
        sleep(delay1)

        direction = input(
            "Great, you just took a shortcut! You're almost close. Would you like to continue straight? [Yes/No] ")
        print("\n")

    if direction == "Yes":
        # Correct
        print("Hooray! You have arrived at the gas station and were able to fuel up!")

    elif direction == "No":
        # Incorrect
        print("You missed the entrance to the gas station and ran out of gas. Better luck next time.")
        dead1 = True
        sleep(delay1)

    elif direction == "Right":
        # Incorrect
        print("Well looks like you took the wrong turn and ran out of gas sorry.")
        sleep(delay1)
        print("Try again next time!")
        dead1 = True

    else:
        # Neutral Choice..
        print("Oops, you missed the entrance and your gas is still running LOW! ")
        sleep(delay1)

        print("ALERT! You are out of gas, better luck next time taking turns correctly!")
        dead1 = True


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
    """
    https://docs.google.com/document/d/1bVDaDKwXmcbTNOW46uQGhc4a2Pgc4pIsxa2Wqp4heaU/edit?usp=sharing
    Beth Mason
    Monica Amaya Hernandez
    """
    global dead

    print()
    opponent = input("Who will you choose for your opponent? (Scott/Tojo/Bystander) ")
    print()

    sleep(2)

    if opponent == "Scott":
        # bad choice
        print("As he steps into the ring he make nervous eye contact with you.")
        print(''' He says "I was hoping no one would choose me, I didn't want it to come to this".''')
        sleep(3)
        print("Within a millisecond he teleports behind you wrapped around your waist and suplexes you,")
        print("snapping your neck on the hard cold unforgiving concrete floor.")
        print("Dr.Scott has killed you!")
        print("Hopefully there is no wrestling in the afterlife!")
        dead = True

    elif opponent == "Tojo":
        # good choice
        print("You get in the ring with Tojo. You notice he's moving a little slow and creaky.")
        print("Turns out he overdid it on the bench press before the fight. You easily throw him to the ground.")
        print("Unable to properly use his arms, he can't get up and is tapped out.")
        sleep(1)


    else:
        # neutral choice
        print("The fellow student you fight happens to be on the exact same level as you, so you tie.")
        print("You have to try fighting them again at the next BWT!")
        sleep(1)

    print()

    kill_if_dead(dead)


def team_16_adv():
    pass
    # TODO Add your code here


def team_17_adv():
    pass
    # TODO Add your code here


def team_18_adv():

    """
    https://docs.google.com/document/d/1b4OuoXpOnB9RS-JyJPZ76MAif1p3_lXQNOYBUODDC18/edit?usp=sharing
    Mahak Kumawat 
    Tristian Razote
    :return: none
    """

    username = input("What is your name?")
    print("Welcome ", username, " to the woods.")
    sleep(delay * 3)
    print("Before you wait too long choose a direction that will let you escape.")
    print("You can take one of the four directions.")
    direction = input("Which direction in the woods would would you like to take? [North, South, East, West]")
    if direction == "North":
        print("You are safe, you get back home.")
        sleep(delay)
    elif direction == "South":
        print("You met the cannibal tribe")
        kill_if_dead(True)
    elif direction == "West":
        print("You fell off a cliff.")
        kill_if_dead(True)
    else:
        print("You got bitten by a poisonous snake. ")
        kill_if_dead(True)


def team_19_adv():
    """
    https://docs.google.com/document/d/1OEkYdYu1uXsIGk77mEY_yK1mmmlWFkW2xxwdVSZasCI/edit
    Sam Edelman
    Destiny White
    """
    dead = False
    username = input("What is your name? ")
    print()
    sleep(delay * 2)
    print("Welcome", username, "to Fruit Land!")
    print("You will be given the choice of three fruits and you can only choose one...")
    print("Be careful the choice you make!")
    print("One will give you fortune, one will lead to death, and one is just a normal fruit.")
    sleep(delay * 2)

    fruit = input("Which fruit would you like? [Banana, Orange, Apple] ")

    if fruit == "Banana":
        print("Unfortunately, you've chosen the rotten fruit, this is the end of your journey!")
        dead = True
    elif fruit == "Orange":
        print("You've chosen the special fruit, you've earned long-lasting prosperity!")
    else:
        print("Yummy! But not few and far between in these lands.")
    kill_if_dead(dead)


def team_20_adv():
    pass
    # TODO Add your code here


def team_21_adv():
    """
    https://docs.google.com/document/d/16WddE8AhpLg8duTmMrZPy8rBFTPxWAWdfpYzfPK1m_w/edit?usp=sharing
    Cole Collins
    """
    global dead

    print("\n")
    print("You find a room that contains two gold statues.")
    sleep(delay)
    statues = input("Do you take the left or right statue, or don't pick up the statue?: ")
    print("\n")

    if statues == "left":
        # good choice
        print("You pick up the statue on the left.")
        sleep(delay)
        print("A passageway opens and you see outside.")
        print("Congrats! You escaped the cave!")
        sleep(delay)
    elif statues == "right":
        # bad choice
        print("You pick up the statue on the right.")
        sleep(delay)
        print("A passageway opens above you.")
        sleep(delay)
        print("A bunch of snakes and spiders fall on you!")
        dead = True
        sleep(delay)
    else:
        # neutral choice
        print("You don't pick up either of the statues.")
        sleep(delay)
        print("Nothing happens... You are still stuck in the cave.")
        sleep(delay)
kill_if_dead(dead)


def team_22_adv():
    pass
    # TODO Add your code here


def team_23_adv():
    pass
    # TODO Add your code here


def team_24_adv():
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
             team_18_adv, team_19_adv, team_20_adv,
             team_21_adv, team_22_adv, team_23_adv,
             team_24_adv]
    random.shuffle(paths)  # Shuffles the order of paths, so each adventure is different

    for i in range(len(paths)):
        paths[i]()  # Runs each function in the paths list

    end_story(user)


main()
