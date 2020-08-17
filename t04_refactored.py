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
# https://docs.google.com/document/d/12AqOblfS_IRP24dKtyJrNh9a8E8JcmrvfzseTkbixyU/edit#
https://docs.google.com/document/d/10pPuYIQyzvUHcUOLCjlP7qWjj2qGqdNFRzZIwPNPCWw/edit?usp=sharing

######################################################################
# Acknowledgements:
#   Original Author: Scott Heggen
######################################################################
import random
from time import sleep
from random import *  # Code needed to import randomness. Group 5
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
    # FIXME: TEAM 1
    """
    https://docs.google.com/document/d/1PixP7Zq24i3DuiMJ67AmIe1nz4II9zzSYyRtKpGpGfk/edit?usp=sharing
    Matthew Foti
    Bekzodjon Rakhimov
    :return: None
    """
    Answer = False
    print("\nYou have found a room that appears to be some goblin's kitchen.")
    print("Inside the kitchen are some strange meats, and a kiwi.")
    choice = input("Do you eat something, or continue on?[meat/kiwi/continue] ")
    if choice.lower() == "kiwi":
        print("\nYou feel revitalized. ")
    elif choice.lower() == "meat":
        while (Answer == False):
            print("\nDaring aren't you? You do understand goblins haven't invented refrigeration yet right?")
            choice = input("That meat looks rather spoiled, are you sure about eating it? [Yes, No] ")
            if "y" in choice.lower():
                sleep(delay * 3)
                print("\nYou have died of dysentery. ")
                quit()  # The player dies
                Answer = True
            elif "n" in choice.lower():
                print("Good call. You continue into the labyrinth.")
                Answer = True
            else:
                print("You hurt yourself thinking too hard. Answer my question again.")
        else:
            print("\nThat was probably wise. You continue into the labyrinth\n")


    # TODO Don't forget to check if your user is dead at the end of your chapter!


def team_2_adv():
    global dead

    print("\nThere is a thin beam of light coming from a hole near the top. From what you can tell, you're somewhere underground.\n")

    sleep(delay)
    print("""\n
    You can see a river in front of you. It's wide and fast, and the current looks dangerous.
    On the other side there is a passageway that leads to another room.
    There are some stepping stones, but they are far apart. It would be easy to miscalculate a jump.
    Far above your head, you see a stone bridge. You might be able to climb up to it and cross.
    \n""")
    sleep(delay * 3)
    print("You can only see three options.\n")
    sleep(delay)
    print("\n1- Try to wade across the river\n")
    sleep(delay)
    print("\n2- Try your luck hopping across the stepping stones.\n")
    sleep(delay)
    print("\n3- Try to climb your way to reach the stone bridge\n")
    direction = input("\nThrough which method do you wish to continue? \n[Wade/Hop/Climb]\n")

    if (direction == "Hop") or (direction ==  "hop"):
        print("You decide to cross the river to the passageway on the far side through using the stepping stones")
        sleep(delay)
        print("When crossing the stepping stones you are having some trouble")
        print("The river has made the stones slick and them being spaced apart makes them difficult to cross")
        sleep(delay * 2)
        print("Upon the jumping from the last stone to the riverbank closest to the far passageway you slip")
        sleep(delay * 3)
        print("Somehow, miraculously you manage to just barely grab the edge of the riverbank but the river is strong")
        sleep(delay * 4)
        print("Fighting the current you are close to being swept away, but your will to survive is stronger")
        print("You pull yourself onto the riverbank and take a deep breath knowing that you barely escaped death")
        print("You are tired, but you continue forward into the passageway in hopes of an escape")
        sleep(delay)

    elif (direction == "Climb") or (direction == "climb"):
        print("Knowing that it is perhaps the hardest way out you start climbing your way up to the stone bridge")
        sleep(delay)
        print(
            "It is a treacherous climb but you reach the stone bridge without too much trouble when you start feeling")
        print("A Crawling Sensation")
        sleep(delay * 3)
        print("A swarm of spiders starts climbs onto your hands and before you react they reach your elbows")
        print("Out of shock, fear and pain your grip on the bridge loosens and you start fall")
        sleep(delay)
        print("The light in the cavern is gone, you feel cold, and the pain fades away")
        dead = True
        sleep(delay * 5)
    else:
        print("Forgoing any other thoughts you decide to charge forth and wade through the river")
        sleep(delay)
        print("The river tries to sweep you away, but you are pretty sure you are better than it so you go on")
        sleep(delay * 2)
        print("Apparently you were wrong and you start getting swept downstream while uttering a string of curses")
        print("You pass out...")
        sleep(delay * 2)
        print("You wake up in a cavern full of glowing moss and only one entryway")
        print("In the room's center there is a fire pit with a blue flame within")
        print("You make use of the fire to dry off")
        sleep(delay * 3)
        print(
            "The sight of the beautiful moss fills you with determination, and the heat of the fire gives you strength.")
        sleep(delay * 3)
        print("Once you are well rested and dry you leave the cave")

    if dead == True:
        print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
        quit()

def team_3_adv():
    pass
    # TODO Add your code here


def team_4_adv():
    # FIXME: TEAM 4
# google doc link: https://docs.google.com/document/d/1FgbyorEA_6xrd24AsXFPcso7X90Ht89XLVXvtqT2oAU/edit?usp=sharing


direction = input(
        "You were walking and faced 5 portals in front of you with different colors. "
        "Which portals will you choose? [Blue/Red/Yellow/Black/White]")

    if direction == "Blue":
        print("Wooww! Great choice! There is a box of GOLD waiting for you behind this portal!")
        sleep(delay)

    elif direction == "Red":
        print("The sound of tigers deprived of food for weeks surrounds you.")
        sleep(5)
        print("The smallest footstep could trigger them and send them into a frenzy.")
        sleep(5)
        print("You try to step away but you trip and cut yourself.")
        sleep(5)
        print("With the smell of blood in the air, the tigers pounce, ripping apart your flesh.")
        sleep(5)
        print("You are dying, but you can still save your life by solving the challenge")
        sleep(5)
        print("If you are smart enough, you can still survive!")
        sleep(5)
        print("So, ready for the challenge?")
        sleep(5)
        logic = input("Look at this series: 80, 10, 70, 15, 60, ... What number should come next?")
        if logic == "20":
            print("Wonderful! With the help of your logical skills you survived!")
            sleep(5)
            print("You are in the farm now. Continue your journey!")
        else:
         dead = True

    else:
        print("You are in the farm now. Continue your journey!")

if dead:
    print("Sorry! You died and this is the end of your story////  Try again by hitting the green play button.")
    quit()


def team_5_adv():

    sleep(3)
    print("You close your eyes for a brief second. As you do, you feel the wind swirl violently around you.")
    sleep(4)
    print("You open your eyes to find yourself in the middle of a dark forest.")
    sleep(3)
    escape = False  # Used to check if the player has escaped yet
    while not dead and not escape:
        doora = randint(1, 3)  # Assigns a random number to DoorA
        doorb = randint(1, 3)  # Assigns a random number to DoorB
        doorc = randint(1, 3)  # Assigns a random number to DoorC
        while ((doora == doorb) or (doorb == doorc) or (
                doorc == doora)):  # Re-rolls all values of the doors until they aren't equal.
            doora = randint(1, 3)
            doorb = randint(1, 3)
            doorc = randint(1, 3)
            # print("Another Iteration" + "\n")
        # print(str(DoorA) + str(DoorB) + str(DoorC))
        print("Every instinct you have is telling you to get out.")
        print("You start walking through the forest until you spot something in the distance.")
        sleep(5)
        print("You see a row of doors in the bark of trees that could lead you out of the forest." +
              " Which door do you enter (Door A, B, or C)?")
        choice = input("Pick one ")
        if choice.upper() == "A":
            print("You go through Door A")
            sleep(2)
            if doora == 1:
                print("You find a long windy path and decide to follow it.")
                sleep(delay * 3)
                print("You've died of starvation")
                sleep(3)
                dead = True
            elif doora == 2:
                print(
                    "You can't seem to find an exit from the forest, however you do stumble upon a small picnic basket.")
                sleep(3)
                print("You open the basket and find a warm sandwich and a red and white blanket to hold you over "
                      "until the morning.")
                sleep(5)
                print("You wake up to find yourself in the middle of a dark forest.")
                sleep(1)
            else:
                sleep(1)
                print("You follow a long tunnel")
                sleep(2)
                escape = True
        elif choice.upper() == "B":
            print("You go through Door B")
            sleep(2)
            if doorb == 1:
                print("You find a long windy path and decide to follow it.")
                sleep(delay * 3)
                print("You've died of starvation")
                dead = True
            elif doorb == 2:
                print(
                    "You can't seem to find an exit from the forest, however you do stumble upon a small picnic basket.")
                sleep(3)
                print("You open the basket and find a warm sandwich and a red and white blanket to hold you over "
                      "until the morning.")
                sleep(5)
                print("You wake up to find yourself in the middle of a dark forest.")
                sleep(1)
            else:
                sleep(1)
                print("You follow a long tunnel")
                sleep(2)
                escape = True
        elif choice.upper() == "C":
            print("You go through Door C")
            sleep(2)
            if doorc == 1:
                print("You find a long windy path and decide to follow it.")
                sleep(delay * 3)
                print("You've died of starvation")
                dead = True
            elif doorc == 2:
                print(
                    "You can't seem to find an exit from the forest, however you do stumble upon a small picnic basket.")
                sleep(3)
                print("You open the basket and find a warm sandwich and a red and white blanket to hold you over "
                      "until the morning.")
                sleep(5)
                print("You wake up to find yourself in the middle of a dark forest.")
                sleep(1)
            else:
                sleep(1)
                print("You follow a long tunnel")
                sleep(2)
                escape = True
        else:
            print("You pass out from thinking too hard. Good job.")
            sleep(2)
            print("You wake up to find yourself in the middle of a dark forest.")
            sleep(2)
    if not dead:
        sleep(1)
        print("Yay you Escaped!")


def team_6_adv():
    """
    Google Doc Link: https://docs.google.com/document/d/1w6XU_suOBSL9st5yvms3vZHbd9hZg8RCAYztqJXqp_E/edit#
    Refactored by Michale Hohl and Robert Dabbs
    :return:
    """
    # TODO Add your code here
    global dead
    import time
    doors = input("which doors you want to open? [A/B/C/D]")

    if doors == "A":
        # this is a very bad choice
        print("Samara is standing there with an axe, and she is not friendly.")  # Samara Morgan is a scary character from the ring movie
        print("It seems that she is very angry, and she start running towards you.")
        sleep(delay)
        print("You have been axed a question.")
        dead = True
    elif doors == "B":
        # this a good choice
        print("In this room there is a treasure hidden in one of a thousand boxes.")
        sleep(delay)
        print("Some of the boxes have warning signs on them.")
        print("It seems the best option is not to open the boxes.")
        print("You could stay in the room for safety or go back to the main area to choose another door.")
        # I believe the first group intended for the ability to choose a different option here
        print("You select a random box.")
        time.sleep(4)
        print("Congratulations! You have found the treasure.")
    elif doors == "C":
        # this door is another bad choice
        print("This room does not seem to be safe.")
        print("This is because there are groups of hungry zombies in with you, ready to attack.")
        print("The door is closed. There is no way out; you are trapped!")
        print("The only weapon in the room is a broom stick.")
        print("You attempt to fight the zombies off, however you are swept away.")
        print("The zombies eat you, and you are gone! However, they are still hungry.")
        print("Nice attempt though. Try to choose wisely next time!")
        print("You have been devoured by the zombies.")
        dead = True
    else:
        # This the exit
        print("This is the way out of this haunted house. Well done.")

    kill_if_dead(dead)


def team_7_adv():
    pass
    # TODO Add your code here


def team_8_adv():
    """
    https://docs.google.com/document/d/16zNYxRmG9FfWZs4yEuWvZWQFkVdXyBjzm4I6xY0lO1M/edit?usp=sharing
    """
    pass
    # TODO Add your code here


username = input("What is your name, idiot?")
print("Welcome ", username, "to the portal.")
direction = input("Before you stand two doors, pick your destiny, door 1 or door 2, what's it gonna be, stupid?")

if direction == "door 1":
    print("You ended up in an old shack infested with rabid raccoons.")
    sleep(delay)

    print("You were mauled, but you bravely fended them off.")
    sleep(delay*2)
    print("Losing a lot of blood and a finger in the process.")

elif direction == "door 2":
    print("You are in the house of sins, The Ladies of the Night")
    sleep(delay)
    print("You could not pay for the services")
    sleep(delay*5)
    print("Too bad, you got yourself killed")
    dead = True
if dead:
    print("Oh no! You died. Better luck next time! Try again by hitting the green play button. ")
    quit()

def team_9_adv():

    # TODO Add your code here

    print("You decided to go grave robbing and ran encounter a corridor with multiple directions")
    sleep(delay)
    direction = input("Which path will lead you to wealth untold? [North/South/East/West]")

    if direction == "West" or direction == "west":
        print("You stumble upon a pile of treasure")
        question = input("Do you take all the treasure? (Yes/No")
        if question == "Yes":
            print("You are greedy and get attacked by a mob of mummies.")
        if question == "No":
            print("You are encountered by a mummy that allows you to take as much gold as you can fit in your pockets. "
                  "Good job for not being greedy.")
    if direction == "North" or direction ==

def team_10_adv():
    pass
    # TODO Add your code here


def team_11_adv():
    pass
    # TODO Add your code here


def team_12_adv():
    """
    https://docs.google.com/document/d/1itzDLd9k-uMVOzEaBe8qeuKqAc3WnSfrHQ2mQ50kWGc/edit?ts=5e3db5ed#heading=h.f6tumop9n7at
    Bedjinal
    Brandon Atu
    :return: none
    """
    # TODO Add your code here
    instrument = input("Which instrument would you like to play? [Piano/Guitar/Bass/Drums]")

    if instrument == "Piano":
        # Correct choice
        print("You have chosen the beautiful melodic instrument of Beethoven.")
        print("You will be able to seduce any woman or mans as soon as you play...")
        sleep(delay)
    elif instrument == "Bass":
        # Wrong choice
        print("You have chosen a demonic instrument. Begin to play the instrument you have chosen")
        sleep(delay)
        print("BOOM!!!!! As soon as you begin to play, the strings un-wire and wrap themselves around your neck")
        print("I bet you can't breathe now, can you? ah!")
        sleep(delay)
        dead = True
    else:
        # Regular choice
        print("The musician Gods have granted you passage to continue. Play on!")
        sleep(delay)

    if dead:
        print("Wow you suck! Too bad buddy. Next time don't die")
        quit()

def team_13_adv():
    # https://docs.google.com/document/d/12AqOblfS_IRP24dKtyJrNh9a8E8JcmrvfzseTkbixyU/edit#   # team 13 google doc
    #https://docs.google.com/document/d/17t-TbE-xSIDAhsHZjWQ9-ic5Pl7MzXLyaUHVXhLjnUE/edit?usp=sharing
    global dead
    direction = input("Which cave tunnel do you want to go down? [Left/Right/Straight]")
    if direction == "left" or "Left" or "LEFT" or "L" or "l":
        print("you have found a baby dragon.It's fire can keep you warm and it can lead you out of the cave. ")
    elif direction == "Right" or "right" or "RIGHT" or "r" or "R":
        print("Oh no. You have run into 100 duck-sized horses.")
        sleep(delay)
        print("They are vicious and out for blood.")
        print("They begin to stampede and knock you off your feet...never to be seen again.")
        dead = True
    else:
        print("You find yourself in a mineshaft, not seeing a way out. While quite interesting, still not the way out.")
        sleep(delay)
if dead == True:
    print("Oopsy. You made a whoopsy. Better luck next time! Play again by hitting the green play button.")
    quit()
        









    # TODO Add your code here



def team_14_adv():

    # FIXME: TEAM 14

    doors = input("You come across three doors. Which door will you open? The Left, Middle, or Right door?")
    print()
    if doors == "Left" or doors == "left" or doors == " Left" or doors == " left":
        print("As you walk, you trip on a rock.")
        print("In front of you, there was a water well.")
        print("You fall into the well and start calling for help.")

        print()
        dead = True
    elif doors == "Middle" or doors == "middle" or doors == " Middle" or doors == " middle":
        print("In front of you is a long tunnel.")
        print("You walk for hours and hours, but never come to an end.")
        print("Eventually, you pass out from exhaustion, and your world goes black.")
        print()
        sleep(delay)
    else:
        print("You walk into a grass field, and as you walk, you see a farm off into the distance.")
        print("You see people milling about near the farm, and decide to walk towards it.")
        print("Your journey takes a little bit of time.")
        print()
        sleep(delay)

    if dead:
        print("You've died. RIP")
        print("That's the end of your story.")
        quit()


def team_15_adv():
    pass
    # TODO Add your code here


def team_16_adv():
    """
    Roshan Adhikari, Anna Carrillo
    https://docs.google.com/document/d/1LqZGqpFp4Vl6KKXVov0_Osly4TciV_j3qubyKZJmhWw/edit?usp=sharing
    """

    # FIXME: TEAM 16


    wait = 2.0

    username = input("Who dares to enter this holy place?")
    print()
    print("Welcome,", username, "to Wakanda.")
    sleep(wait / 2)
    choice = input("What are you here for?")
    print()
    print("Oh!", username, " you are in luck, we happen to have", choice, "in Wakanda.")
    sleep(wait * 2)
    print("But before we attend to you, you must drink from these bowls.")
    print("The red bowl, the blue bowl, and the green bowl.")
    print("But beware!! One of these bowls will kill you. So, choose wisely!")
    print()
    sleep(wait)


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

